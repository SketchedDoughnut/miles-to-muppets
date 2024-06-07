'''
This is the main file for managing the other folders, and controls all the main functions.
'''

# builtins
import sys
import time
import os

# installed
import requests

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
        from .data import data

        # set up internal 
        self.data = data
        self.constants = self.data['constants']
        self.key_list = self.data['key_list']
        self.album_list = self.data['albums']


        # get token, auth_header
        self.token = get_token(client_id, client_secret)
        self.auth_header = get_auth_header(self.token)

        # set up numbers for calculations later
        self.mph_speed = self.constants['defMphSpeed']
        self.min_per_mile = self.constants['defMinPerMile']

        # print the session data, if requested
        if do_print == True:
            print('-----------------------------')
            print("SESSION DATA:")
            print("Token:", self.token)
            print("Auth header:", self.auth_header)
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

        # imports
        from .functions import minuteToMs
        self.constants['defMphSpeed'] = speed
        self.constants['defMinPerMile'] = speed / 60
        self.mph_speed = self.constants['defMphSpeed']
        self.min_per_mile = self.constants['defMinPerMile']
        self.minute_distance = self.min_per_mile * self.mile_distance
        self.ms_distance = minuteToMs(self.minute_distance)

    # sets the active album to the one of their choosing
    def set_album(self, song_choice: int) -> dict:
        '''
        chooses a song from the "key_list" dictionary
        '''

        album_id = self.album_list[self.key_list[song_choice]]
        self.album_data = requests.get(f'https://api.spotify.com/v1/albums/{album_id}', headers=self.auth_header).json()
        self.album_name = self.album_data['name']
        self.song_count = self.album_data['total_tracks']
        self.tracks = self.album_data['tracks']['items']
        return {
            "album name": self.album_name,
            "total songs": self.song_count
        }
    
    # make sure everything is updated before running
    def _initialize(self):
        pass

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

            # backwards compatible dictionary data
            # 'average speed': self.mph_speed,
            # 'minute(s) per mile': self.min_per_mile,
            # 'songs listened': song_amount,

            # active dictionary data
            'finished album': found_max,
            'avg. mph speed': self.mph_speed,
            'avg. minute(s) per mile': self.min_per_mile,
            'songs listened to': song_amount,
            'mile distance': self.mile_distance,
            'minute distance': self.minute_distance,
            'ms distance': self.ms_distance,
            'counted ms distance': total_ms,
            'leftover minute(s)':  minute_leftover
        }