# builtins
import sys
import time

# imports
import requests

# files
from data import *
from functions import *

# set up client details (moved down from above)
# client_id = input('Please enter your client_id: ')
# client_secret = input('Please enter your client secret: ')

# set up overrulling dict, constants
DATA = data
CONSTANTS = DATA['constants']
KEY_LIST = DATA['key_list']
ALBUM_LIST = DATA['songs']
KEY_ITER = KEY_LIST.keys()
ALBUM_ITER = ALBUM_LIST.keys()

class MilesToMuppets:
    def __init__(self, client_id: str, client_secret: str, output_mode: str= 'null') -> None:
        # get token, auth_header
        self.TOKEN = get_token(client_id, client_secret)
        self.AUTH_HEADER = get_auth_header(self.TOKEN)

        # set up vals
        self.mph_speed = CONSTANTS['defMphSpeed']
        self.min_per_mile = CONSTANTS['defMinPerMile']

        # set up internal 
        self.data = DATA
        self.constants = CONSTANTS
        self.key_list = KEY_LIST
        self.album_list = ALBUM_LIST

        # print DATA
        if output_mode == 'print':
            print('-----------------------------')
            print("SESSION DATA:")
            print("Token:", self.TOKEN)
            print("Auth header:", self.AUTH_HEADER)
            print('-----------------------------')
        # else:
        #     return {
        #         "token": self.TOKEN,
        #         "auth header": self.AUTH_HEADER
        #     }
        
        # print('-----------------------------')
        # if input(f'Override default speed of {mph_speed}mph? (y/n) ').lower() == 'y':
        #     mph_speed = float(input('Enter new speed (mph) \n--> '))
        #     min_per_mile = 60 / mph_speed

    def set_mile_distance(self, speed: float) -> None:
        '''set the distance you intend to travel, in mph'''
        self.mile_distance = speed
        # print('-----------------------------')
        # mile_distance = float(input('How far is your destination, in miles? \n--> '))
        self.minute_distance = self.min_per_mile * self.mile_distance
        self.ms_distance = minuteToMs(self.minute_distance)

    def choose_song(self, song_choice: int) -> dict:
        '''chooses a song from the "self.key_list" dictionary'''
        # print('-----------------------------')
        # print('Please choose from the following albums:')
        # for key, album in zip(KEY_ITER, ALBUM_ITER):
        #     print(f"- {key}: {album}")
        # song_choice = int(input('--> '))
        album_id = ALBUM_LIST[KEY_LIST[song_choice]]
        self.ALBUM_DATA = requests.get(f'https://api.spotify.com/v1/albums/{album_id}', headers=self.AUTH_HEADER).json()
        self.album_name = self.ALBUM_DATA['name']
        self.song_count = self.ALBUM_DATA['total_tracks']
        self.tracks = self.ALBUM_DATA['tracks']['items']
        # print('-----------------------------')
        # print('Album name:', album_name)
        # print('Total amount of songs:', song_count)
        return {
            "album name": self.album_name,
            "total songs": self.song_count
        }
    
    def evaluate_album(self) -> dict:
        '''evaluates the album'''
        total_ms = 0
        song_amount = 0
        found_max = False
        leng = "                                                                                      "
        print('-----------------------------\n')
        for track in self.tracks:
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

            if total_ms >= self.ms_distance:
                found_max = True
                break
            else:
                total_ms += duration_ms
                song_amount += 1
            
        ms_leftover = self.ms_distance - total_ms
        minute_leftover = round(msToMinute(ms_leftover), 2)
        print(" ")
        print('-----------------------------')
        return {
            'finished album': found_max,
            'average speed': self.mph_speed,
            'minute(s) per mile': self.min_per_mile,
            'songs listened': song_amount,
            'mile distance': self.mile_distance,
            'minute distance': self.minute_distance,
            'ms distance': self.ms_distance
        }
        # if found_max:
        #     print(f"""Here is the results:
        #     - average speed: {self.mph_speed}mph
        #     - minute(s) per mile: {self.min_per_mile}
        #     - songs listened: {song_amount}
        #     - album name: {self.album_name}
        #     - mile distance: {self.mile_distance}
        #     - minute distance: {self.minute_distance}
        #     - ms distance: {self.ms_distance}""")
        # else:
        #     print('Here is the results:')
        #     print(f"""You would have finished this playlist on the drive to your destination.
        # There would be: {minute_leftover} minute(s) left on your trip.""")
        #     print(f"""Other data:
        #     - average speed: {self.mph_speed}mph
        #     - minute(s) per mile: {self.min_per_mile}
        #     - songs listened: {song_amount}
        #     - album name: {self.album_name}
        #     - mile distance: {self.mile_distance}
        #     - minute distance: {self.minute_distance}
        #     - ms distance: {self.ms_distance}""")