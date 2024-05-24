'''
This is the main file for managing the other folders, and controls all the main functions.
'''

# builtins
import sys
import time
import os

# installed
import requests

# files
from .data import data

# the general class for milesToMuppets
class MilesToMuppets:
    '''
    This is the main class for use for setting up and using Miles To Muppets.
    All functions you need will be provided by this class.
    If you want the help functions, you can access them from:
    -> milesToMuppets.get_(help, license, credits)()
    '''

    # sets up spotify API connection, gets data from that (as well as loads data from data file)
    def __init__(self, client_id: str, client_secret: str, do_print: bool = False) -> None:
        # imports
        from .functions import get_token, get_auth_header

        # set up internal 
        DATA = data
        CONSTANTS = DATA['constants']
        KEY_LIST = DATA['key_list']
        ALBUM_LIST = DATA['songs']
        self.data = DATA
        self.constants = CONSTANTS
        self.key_list = KEY_LIST
        self.album_list = ALBUM_LIST


        # get token, auth_header
        self.TOKEN = get_token(client_id, client_secret)
        self.AUTH_HEADER = get_auth_header(self.TOKEN)

        # set up numbers for calculations later
        self.mph_speed = CONSTANTS['defMphSpeed']
        self.min_per_mile = CONSTANTS['defMinPerMile']

        # print the session data, if requested
        if do_print == True:
            print('-----------------------------')
            print("SESSION DATA:")
            print("Token:", self.TOKEN)
            print("Auth header:", self.AUTH_HEADER)
            print('-----------------------------')

    


    # sets the distance they intend to travel, in miles
    def set_mile_distance(self, distance: float) -> None:
        '''
        set the distance you intend to travel, in miles
        '''

        # imports
        from .functions import minuteToMs
        # calculations, conversions
        self.mile_distance = distance
        self.minute_distance = self.min_per_mile * self.mile_distance
        self.ms_distance = minuteToMs(self.minute_distance)

    # sets the average speed they are traveling at, in mph
    def set_speed(self, speed: float) -> None:
        '''
        sets the speed at which you are traveling, in mph
        '''

        self.constants['defMphSpeed'] = speed
        self.constants['defMinPerMile'] = 60 / speed

    # sets the active album to the one of their choosing
    def set_album(self, song_choice: int) -> dict:
        '''
        chooses a song from the "key_list" dictionary
        '''

        album_id = self.album_list[self.key_list[song_choice]]
        self.ALBUM_DATA = requests.get(f'https://api.spotify.com/v1/albums/{album_id}', headers=self.AUTH_HEADER).json()
        self.album_name = self.ALBUM_DATA['name']
        self.song_count = self.ALBUM_DATA['total_tracks']
        self.tracks = self.ALBUM_DATA['tracks']['items']
        return {
            "album name": self.album_name,
            "total songs": self.song_count
        }
    
    # evaluates the album chosen, with options to print if they want to
    def evaluate_album(self, print_cycle: bool = False, do_delay: bool = True) -> dict:
        '''
        evaluates the album
        '''
        

        # imports
        from .functions import msToMinute

        # initially set up numbers
        total_ms = 0
        song_amount = 0
        found_max = False
        if print_cycle:
            width = os.get_terminal_size()[0]
            spacing = " " * width
            print('-----------------------------\n')
        for track in self.tracks:
            name = track['name']
            duration_ms = track['duration_ms']
            # fancy printing, re-writing the same lines over and over
            if print_cycle:
                sys.stdout.write("\033[F")
                sys.stdout.write(f"{spacing}\n{spacing}")
                sys.stdout.write("\033[F")
                sys.stdout.write(f"\rsong name: {name}\nduration: {duration_ms}ms")
                sys.stdout.flush()
                if do_delay:
                    time.sleep(0.15)

            # break if we have met / exceeded the target time
            if total_ms >= self.ms_distance:
                found_max = True
                break
            else:
                total_ms += duration_ms
                song_amount += 1
            
        # calculate the leftover time
        ms_leftover = self.ms_distance - total_ms
        minute_leftover = round(msToMinute(ms_leftover), 2)
        if print_cycle:
            print(" ")
            print('-----------------------------')
        # return all of the data
        return { 
            'finished album': found_max,
            'average speed': self.mph_speed,
            'minute(s) per mile': self.min_per_mile,
            'songs listened': song_amount,
            'mile distance': self.mile_distance,
            'minute distance': self.minute_distance,
            'ms distance': self.ms_distance,
            'leftover minute(s)':  minute_leftover
        }