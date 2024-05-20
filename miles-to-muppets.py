# builtins
import os
import base64
import sys
import time

# imports
import requests
import dotenv

# load environment variables
# dotenv.load_dotenv()
# client_id = os.getenv("CLIENT_ID")
# client_secret = os.getenv("CLIENT_SECRET")

# set up client details (moved down from above)
client_id = input('Please enter your client_id: ')
client_secret = input('Please enter your client secret: ')

# main data (stats, songs, etc)
data = {
        "songs": {
            "Muppets Most Wanted": "3Z1dw9cLeFAyhvkXdn6P5G",
            "The Muppets": "0mahHDhPnuYMbo3sXOEW50"
        },

        "key_list": {
            1: "Muppets Most Wanted",
            2: "The Muppets"
        },
        "constants": {
            "speed": 60,
            "minPerMile": 1
        }
    }

# get token
def get_token() -> None:
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

# get auth header
def get_auth_header(token: str) -> dict:
    ''' gets the authorization header from spotify '''
    return {
        "Authorization": "Bearer " + token
    }






# get token, auth_header
token = get_token()
auth_header = get_auth_header(token)
print('-----------------------------')
print("DATA:")
print("Token:", token)
print("Auth header:", auth_header)
print('-----------------------------')

# establish song dict data
dat = data
key_list = dat['key_list']
key_iter = key_list.keys()
album_list = dat['songs']
album_iter = album_list.keys()

# establish constants
constants = dat['constants']
speed = constants['speed']
minPerMile = constants['minPerMile']

# get destination info (use google API later?)
distance = int(input('How far is your destination, in miles? \n-> '))

# get album choice
print('-----------------------------')
print('Please choose from the following albums:')
for key, album in zip(key_iter, album_iter):
    print(f"- {key}: {album}")
choice = int(input('-> '))
album_id = album_list[key_list[choice]]
print('-----------------------------')

album_data = requests.get(f'https://api.spotify.com/v1/albums/{album_id}', headers=auth_header).json()
album_name = album_data['name']
print('Album name:', album_name)
print('Total amount of songs:', album_data['total_tracks'])
# print('Album type:', album_data['album_type'])
# print('Base keys:', album_data.keys())
# print('Track keys:', album_data['tracks'].keys())
# print('Track items:', album_data['tracks']['items'])

# start loop
print('-----------------------------')
input('Enter anything to start evaluation...')

total_time = 0
song_amount = 0
found_max = False
mileTominLength = minPerMile * distance
mileToMsLength = (mileTominLength * 60) * 1000

print("-----------------------------\n ")
for track in album_data['tracks']['items']:
    name = track['name']
    duration_ms = track['duration_ms']
    leng = "                                                                           " * 2
    sys.stdout.write("\033[F")
    sys.stdout.write(f"{leng}\n{leng}")
    sys.stdout.write("\033[F")
    sys.stdout.write(f"\rsong name: {name}\nduration: {duration_ms}ms")
    sys.stdout.flush()
    time.sleep(0.1)
    
    total_time += duration_ms
    song_amount += 1
    if total_time >= mileToMsLength:
        found_max = True
        break
print(" ")
print('-----------------------------')
if found_max:
    print(f'At an average speed of {speed}mph, taking {minPerMile} minute per mile, it will take you roughly {song_amount} muppet songs from the album "{album_name}" to reach your destination.')
else:
    print(f'At an average speed of {speed}mph, taking {minPerMile} minute per mile, you would have completed this album ({song_amount} songs) on the trip to your destination.')