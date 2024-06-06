'''
this file just makes it more helpful to seperate data from code, given I ever put more data in
'''

# default_mph_speed = 670_616_629
default_mph_speed = 60.0
data = {
        "albums": { # song name, spotify URI
            "Muppets Most Wanted": "3Z1dw9cLeFAyhvkXdn6P5G",
            "The Muppets": "0mahHDhPnuYMbo3sXOEW50"
        },

        "key_list": { # a key_list for peoples selections, just translates nums into song names for above
            0: "Muppets Most Wanted",
            1: "The Muppets"
            # also add "muppets electric mayhem"
        },
        "constants": { # constants used for calculations
            "defMphSpeed": float(default_mph_speed),
            # "defMinPerMile": float(60 / default_mph_speed)
            "defMinPerMile": float(default_mph_speed / 60)
        }
    }