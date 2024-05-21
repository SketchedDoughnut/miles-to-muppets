import src.milesToMuppets as m

foo = m.MilesToMuppets(
    client_id='x',
    client_secret='x'
)

foo.set_mile_distance(1.1)
foo.set_speed(2.2)
foo.set_album(0)
foo.evaluate_album()