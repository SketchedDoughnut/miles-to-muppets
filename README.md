# Miles to Muppets
A calculator that converts mile distance to how many Muppets songs you can listen to.

# Setup

- first, import **miletomuppets** <br>
`import milestomuppets` <br>

- in the code, set up your class object, passing in your Spotify client id and client secret (which can be obtained from Spotify for Developers for free) <br>
`foo = milestomuppets.MilesToMuppets(client_id = client_id, client_secret = client_secret)` <br>

    - When initializing the class, if you want it to print data, initialize the class as so. <br>
`foo = MilesToMuppets(client_id = client_id, client_secret = client_secret, output_mode = 'print')`

- next, set the distance you are going, in miles. This number can be anything, but 60 is used as an example here. <br>
  `foo.set_mile_distance(60)`

- set the speed at which you are traveling, in mph. This number can be anything, but 30 is used as an example here. <br>
`foo.set_speed(30)`

- choose what album you want to use. To do this, you need to print out the list of valid albums and pick the number associated with it. You can do this by requesting the current album dictionary, as shown below. <br>
    - `albums = foo.key_list` <br>

- then, put your selection into the following function. In this case, we are using 1. <br>
`foo.choose_album(1)`

- finally, run the function to evaluate the album and return a dictionary with the results.<br>
`foo.evaluate_album()`
    - If you want to disable printing, set "print_cycle" to false. <br>
    `foo.evaluate_album(print_cycle = False)`


# Other functions

- `foo.get_session_data()` - will return your session token, and your auth header in a dict.
