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
    redirect_uri: str
        The redirect URI that you registered when creating your Spotify For Developers App. Help can be found [here](https://developer.spotify.com/documentation/web-api/concepts/apps).
    unit: Unit
        The distance unit that you prefer to use
    '''

    # sets up spotify API connection, gets data from that (as well as loads data from data file)
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, unit: Unit) -> None:
        # all our urls
        self._auth_url = 'https://accounts.spotify.com/authorize'
        self._token_url = 'https://accounts.spotify.com/api/token'
        self._base_url = 'https://api.spotify.com/v1/'
        # our unit preference, token, and auth header
        self._unit = unit
        self._client_id = client_id
        self._client_secret = client_secret
        self._redirect_uri = redirect_uri
        self._credentials = base64.b64encode((client_id + ':' + client_secret).encode()).decode()


    # authorize
    def _authorize(self):
        # get our auth code
        auth_payload = {
            'client_id': self._client_id,
            'response_type': 'code',
            'redirect_uri': self._redirect_uri
        }
        res = requests.get(url=self._auth_url, params=auth_payload)
        if res.status_code != 200: raise Exceptions.InvalidAuthorizationError(f'Your authorization credentials were invalid! {res.status_code}')
        # get our access token
        token_payload = {
            'grant_type': 'authorization_code',
            'code': res,
            'redirect_uri': self._redirect_uri
        }
        token_header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + self._credentials
        }
        res = requests.post(url=self._token_url, data=token_payload,headers=token_header)
        if res.status_code != 200: raise Exceptions.InvalidAuthorizationError(f'Your authorization credentials were invalid! {res.status_code}')