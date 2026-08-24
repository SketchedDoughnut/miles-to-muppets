'''
This is the main file for managing the other folders, and controls all the main functions.
'''

# libraries
from enum import Enum
import requests
import base64
import time
import sys
import os

# files
from .conversions import *


# class for different unit enums
class Unit(Enum):
    MILES = 'miles'
    KILOMETERS = 'kilometers'


# class for exceptions
class Exceptions:
    # authorization was invalid in some way
    class InvalidAuthorizationError(BaseException): 
        def __init__(self, *args): super().__init__(*args)


# the general class for milesToMuppets
class Muppet:
    '''
    This class allows you to interact with Spotify and find out how many albums you can listen to on your trip.

    Parameters
    ----------
    client_id: str
        The Spotify client ID
    client_secret: str
        The spotify client secret
    unit: Unit
        The distance unit that you prefer to use
    '''

    # sets up spotify API connection, gets data from that (as well as loads data from data file)
    def __init__(self, client_id: str, client_secret: str, unit: Unit) -> None:
        # all our urls
        self._token_url = 'https://accounts.spotify.com/api/token'
        # our unit preference, token, and auth header
        self._unit = unit
        self._credentials = base64.b64encode((client_id + ':' + client_secret).encode()).decode()
        self._token = self._authorize()
        self._header = {
            'Authorization': 'Bearer ' + self._token['access_token']
        }


    # authorize
    def _authorize(self) -> dict:
        # get our access token
        token_payload = {
            'grant_type': 'client_credentials',
            # 'code': auth_res,
            # 'redirect_uri': self._redirect_uri
        }
        token_header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + self._credentials
        }
        token_res = requests.post(url=self._token_url, data=token_payload,headers=token_header)
        if token_res.status_code != 200: raise Exceptions.InvalidAuthorizationError(f'Your authorization credentials were invalid! {token_res.status_code}')
        return token_res.json()


    # fetch all relevant muppets albums
    def fetch_albums(self) -> str:
        query = 'https://api.spotify.com/v1/search?q=The+Muppets&type=album&limit=5'
        res = requests.get(url=query, headers=self._header)
        if res.status_code != 200: raise Exceptions.InvalidAuthorizationError(f'Your authorization credentials were invalid! {res.status_code}')
        albums = []
        for album in res.json()['albums']['items']:
            if 'muppet' not in album['name'].lower(): continue
            albums.append(album)
        return albums