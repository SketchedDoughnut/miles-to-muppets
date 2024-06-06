# imports
# from pyscript import document
import milesToMuppets

def run_muppet():
    # get document data
    client_id_in = document.getElementById('spotify_id').innerText
    client_secret_in = document.getElementById('spotify_secret').innerText
    song_selection = document.getElementById('song_selection').innerText
    mile_distance = document.GetElementById('mile_distance').innerText
    mph_speed = document.GetElementById('mph_speed').innerText

    # convert necessary to int
    song_selection = int(song_selection)
    mile_distance = float(mile_distance)
    mph_speed = float(mph_speed)

    # set up class object
    muppet = milesToMuppets.MilesToMuppets(
        client_id=client_id_in, 
        client_secret=client_secret_in
    )

    # config
    muppet.set_album(song_selection)
    muppet.set_mile_distance(mile_distance)
    muppet.set_speed(mph_speed)

    # valuate album
    results = muppet.evaluate_album(do_delay=False)

    # display results
    #results = 'uwu'
    x = document.GetElementById('results')
    x.innerText = results