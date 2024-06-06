# mtm
import milesToMuppets

# pyscript config
from pyscript import document

# grab assets from document
def run_muppet():
    # global client_id, client_secret
    # global song_selection
    # global mile_distance, mph_speed
    # client_id = document.getElementById('spotify_id').innerText
    # client_secret = document.getElementById('spotify_secret').innerText
    # song_selection = int(document.getElementById('song_selection').innerText)
    # mile_distance = int(document.GetElementById('mile_distance').innerText)
    # mph_speed = int(document.GetElementById('mph_speed').innerText)


    # muppet = milesToMuppets.MilesToMuppets(
    #     client_id=client_id, 
    #     client_secret=client_secret
    # )

    # muppet.set_album(song_selection)
    # muppet.set_mile_distance(mile_distance)
    # muppet.set_speed(mph_speed)
    # results = muppet.evaluate_album(do_delay=False)
    results = 'uwu'
    x = document.GetElementById('results')
    x.innerText = results