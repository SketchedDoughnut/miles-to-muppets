'''
this file hosts a majority of the functions used in the muppet.py file. 
The helper functions are in helpers.py.'''

# builtins
import base64

# install
import requests



## SPOTIFY SYSTEMS
# get token from spotify
def get_token(client_id, client_secret) -> str:
    '''
    get the token from spotify, passing in the client id and secret
    '''

    auth_string: str = client_id + ":" + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 =  str(base64.b64encode(auth_bytes), 'utf-8')

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    results = requests.post(url, headers=headers, data=data).json() # post data, get back results
    token = results['access_token']
    return token



# get auth header from spotify
def get_auth_header(token: str) -> dict: # essentially just sets up a formatted header for future requests
    '''
    gets the authorization header from spotify
    '''

    return {
        "Authorization": "Bearer " + token
    }





## UNIT CONVERSIONS
# converts hours to millisecond
def hourToMs(hour: float) -> float:
    '''
    converts hours to milliseconds
    '''

    # hour to min
    minute = hour * 60
    # min to second
    second = minute * 60
    # second to ms
    ms = second * 1000
    return ms

# converts milliseconds to hour
def msToHour(ms: float) -> float:
    '''
    converts milliseconds to hours
    '''

    # ms to second
    second = ms / 1000
    # second to minute
    minute = second / 60
    # minute to hour
    hour = minute / 60
    return hour

# converts minutes to milliseconds
def minuteToMs(minute: float) -> float:
    '''
    converts minutes to milliseconds
    '''

    # minute to second
    second = minute * 60
    # second to ms
    ms = second * 1000
    return ms

# converts milliseconds to minutes
def msToMinute(ms: float) -> float:
    '''
    converts milliseconds to minutes
    '''

    # ms to second
    second = ms / 1000
    # second to minute
    minute = second / 60
    return minute

# converts minutes to hours
def minuteToHour(minute: float) -> float:
    '''
    converts minutes to hours
    '''

    # minute to hour
    hour = minute / 60
    return hour