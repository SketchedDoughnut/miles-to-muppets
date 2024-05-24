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
def hourToMs(num: float) -> float:
    '''
    converts hours to milliseconds
    '''

    # hour to min
    output = num * 60
    # min to second
    output = output * 60
    # second to ms
    output = output * 1000
    return output

# converts milliseconds to hour
def msToHour(num: float) -> float:
    '''
    converts milliseconds to hours
    '''

    # ms to second
    output = num / 1000
    # second to minute
    output = output / 60
    # minute to hour
    output = output / 60
    return output

# converts minutes to milliseconds
def minuteToMs(num: float) -> float:
    '''
    converts minutes to milliseconds
    '''

    # minute to second
    output = num * 60
    # second to ms
    output = output * 1000
    return output

# converts milliseconds to minutes
def msToMinute(num: float) -> float:
    '''
    converts milliseconds to minutes
    '''

    # ms to second
    output = num / 1000
    # second to minute
    output = output / 60
    return output