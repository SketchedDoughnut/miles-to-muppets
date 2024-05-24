# Miles to Muppets
A calculator that converts mile distance to how many Muppets songs you can listen to.

# Setup

- first, install milesToMuppets with pip.
    - `pip install milesToMuppets`
    - `python3 -m pip install milesToMuppets`

- next, import milesToMuppets (in this case, we rename it to muppet) <br>
`import milesToMuppets as muppet` <br>

- in the code, set up your class object, passing in your Spotify client id and client secret (which can be obtained from Spotify for Developers for free) <br>
`foo = muppet.MilesToMuppets(client_id = client_id, client_secret = client_secret)` <br>

    - When initializing the class, if you want it to print its session data, initialize the class as so. <br>
`foo = muppet.MilesToMuppets(client_id = client_id, client_secret = client_secret, do_print = True)`

- next, set the distance you are going, in miles. This number can be anything, but 60 is used as an example here. <br>
  `foo.set_mile_distance(60)`

- set the speed at which you are traveling, in mph. This number can be anything, but 30 is used as an example here. If you do not set a speed, it defaults to 60. <br>
`foo.set_speed(30)`

- choose what album you want to use. To do this, you need to print out the list of valid albums and pick the number associated with it. You can do this by requesting the current album dictionary, as shown below. <br>
`albums = foo.get_albums()` <br>

- then, put your selection into the following function. In this case, we are using 0. <br>
`foo.set_album(0)`

- finally, run the function to evaluate the album and return a dictionary with the results.<br>
`foo.evaluate_album()`
    - If you want to enable printing, set "print_cycle" to false. <br>
    `foo.evaluate_album(print_cycle = True)`
    - If you want to disable the delay between prints, set "do_delay" to false. <br>
    `foo.evaluate_album(do_delay = False)`


# Other functions

- `muppet.get_help()` - Will print out some information to help you.

- `muppet.get_session_data()` - will return your session token, and your auth header in a dict.
  
- `muppet.get_license()` - Will print out what license this project is using.

- `muppet.get_credits()` - Will print out the credits for the development of this project.