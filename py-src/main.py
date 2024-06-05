# mtm
import milesToMuppets

# pyscript config
import pyscript as js

# grab assets from document
def run():
    global client_id, client_secret
    global song_selection
    global mile_distance, mph_speed
    client_id = js.document.getElementById('spotify_id')
    client_secret = js.document.getElementById('spotify_secret')
    song_selection = int(js.document.getElementById('song_selection'))
    mile_distance = int(js.document.GetElementById('mile_distance'))
    mph_speed = int(js.document.GetElementById('mph_speed'))


    muppet = milesToMuppets.MilesToMuppets(
        client_id=client_id, 
        client_secret=client_secret
    )

    muppet.set_album(song_selection)
    muppet.set_mile_distance(mile_distance)
    muppet.set_speed(mph_speed)
    results = muppet.evaluate_album(do_delay=False)