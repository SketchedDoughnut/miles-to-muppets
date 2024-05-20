# install
import requests

# builtins
import base64


# SPOTIFY SYSTEMS

# get token from spotify
def get_token(client_id, client_secret) -> str:
    ''' get the token from spotify, passing in the client id and secret '''
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
    results = requests.post(url, headers=headers, data=data).json()
    token = results['access_token']

    return token

# get auth header from spotify
def get_auth_header(token: str) -> dict:
    ''' gets the authorization header from spotify '''
    return {
        "Authorization": "Bearer " + token
    }




# UNIT CONVERSIONS
def hourToMs(num: float) -> float:
    # hour to min
    output = num * 60
    # min to second
    output = output * 60
    # second to ms
    output = output * 1000
    return output

def msToHour(num: float) -> float:
    # ms to second
    output = num / 1000
    # second to minute
    output = output / 60
    # minute to hour
    output = output / 60
    return output

def minuteToMs(num: float) -> float:
    # minute to second
    output = num * 60
    # second to ms
    output = output * 1000
    return output

def msToMinute(num: float) -> float:
    # ms to second
    output = num / 1000
    # second to minute
    output = output / 60
    return output