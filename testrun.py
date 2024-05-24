import milesToMuppets as muppet

foo = muppet.MilesToMuppets(
    client_id='x',
    client_secret='x' 
)

foo.set_mile_distance(60)
foo.set_speed(30)
albums = foo.get_albums()
foo.set_album(0)
foo.evaluate_album(print_cycle=True)



