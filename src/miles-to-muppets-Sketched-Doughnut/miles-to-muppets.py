# builtins
import sys
import time

# imports
import requests

# files
from data import *
from functions import *

# set up client details (moved down from above)
client_id = input('Please enter your client_id: ')
client_secret = input('Please enter your client secret: ')

# set up overrulling dict, constants
DATA = data
CONSTANTS = DATA['constants']
KEY_LIST = DATA['key_list']
ALBUM_LIST = DATA['songs']
KEY_ITER = KEY_LIST.keys()
ALBUM_ITER = ALBUM_LIST.keys()

# get token, auth_header
TOKEN = get_token(client_id, client_secret)
AUTH_HEADER = get_auth_header(TOKEN)

# print DATA
# print('-----------------------------')
# print("SESSION DATA:")
# print("Token:", TOKEN)
# print("Auth header:", AUTH_HEADER)






mph_speed = CONSTANTS['defMphSpeed']
min_per_mile = CONSTANTS['defMinPerMile']
print('-----------------------------')
if input(f'Override default speed of {mph_speed}mph? (y/n) ').lower() == 'y':
    mph_speed = float(input('Enter new speed (mph) \n--> '))
    min_per_mile = 60 / mph_speed
print('-----------------------------')
mile_distance = float(input('How far is your destination, in miles? \n--> '))
minute_distance = min_per_mile * mile_distance
ms_distance = minuteToMs(minute_distance)

print('-----------------------------')
print('Please choose from the following albums:')
for key, album in zip(KEY_ITER, ALBUM_ITER):
    print(f"- {key}: {album}")
song_choice = int(input('--> '))
album_id = ALBUM_LIST[KEY_LIST[song_choice]]
ALBUM_DATA = requests.get(f'https://api.spotify.com/v1/albums/{album_id}', headers=AUTH_HEADER).json()
album_name = ALBUM_DATA['name']
song_count = ALBUM_DATA['total_tracks']
tracks = ALBUM_DATA['tracks']['items']
print('-----------------------------')
print('Album name:', album_name)
print('Total amount of songs:', song_count)
total_ms = 0
song_amount = 0
found_max = False
leng = "                                                                                      "
print('-----------------------------\n')
for track in tracks:
    name = track['name']
    duration_ms = track['duration_ms']
    # total_ms += duration_ms
    # song_amount += 1
    sys.stdout.write("\033[F")
    sys.stdout.write(f"{leng}\n{leng}")
    sys.stdout.write("\033[F")
    sys.stdout.write(f"\rsong name: {name}\nduration: {duration_ms}ms")
    sys.stdout.flush()
    time.sleep(0.15)

    if total_ms >= ms_distance:
        found_max = True
        break
    else:
        total_ms += duration_ms
        song_amount += 1
    
ms_leftover = ms_distance - total_ms
minute_leftover = round(msToMinute(ms_leftover), 2)
print(" ")
print('-----------------------------')
if found_max:
    print(f"""Here is the results:
    - average speed: {mph_speed}mph
    - minute(s) per mile: {min_per_mile}
    - songs listened: {song_amount}
    - album name: {album_name}
    - mile distance: {mile_distance}
    - minute distance: {minute_distance}
    - ms distance: {ms_distance}""")
else:
    print('Here is the results:')
    print(f"""You would have finished this playlist on the drive to your destination.
There would be: {minute_leftover} minute(s) left on your trip.""")
    print(f"""Other data:
    - average speed: {mph_speed}mph
    - minute(s) per mile: {min_per_mile}
    - songs listened: {song_amount}
    - album name: {album_name}
    - mile distance: {mile_distance}
    - minute distance: {minute_distance}
    - ms distance: {ms_distance}""")


# print(f"""At an average speed of {mph_speed}mph, taking {min_per_mile} minute(s) per mile, it will take you roughly {song_amount} muppet songs from the album"{album_name}" to reach your destination of {mile_distance} miles.""")
# else:
#     print(f'At an average speed of {mph_speed}mph, taking {min_per_mile} minute per mile, you would have completed this album ({song_amount} songs) on the trip to your destination.')