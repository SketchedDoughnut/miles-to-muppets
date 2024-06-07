# imports
# from pyscript import document
import milesToMuppets
import js 

def run_muppet(why_do_I_need_this_input):
    # get document data
    client_id_in = js.document.getElementById('spotify_id').value
    client_secret_in = js.document.getElementById('spotify_secret').value
    song_selection = js.document.getElementById('song_selection').value
    mile_distance = js.document.getElementById('mile_distance').value
    mph_speed = js.document.getElementById('mph_speed').value
    output_buffer = js.document.getElementById('results')

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
    # results = 'uwu'
    # string = f'results: {results}'
    string = 'Results'
    output_buffer.innerText = string

    template = [
        "Finished album",
        "Finished trip",
        "Average speed",
        "Average minutes per mile",
        "Songs listened to",
        "Miles distance",
        "Minutes distance",
        "Millisecond distance",
        "Counted ms distance",
        "Leftover minutes",
        "Leftover miles"
    ]
    for key, prefix in zip(results, template):
        current_element = js.document.getElementById(key)
        results_val = results[key]
        output_string = f"{prefix}: {results_val}"
        current_element.innerText = output_string