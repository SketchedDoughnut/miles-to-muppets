# import milesToMuppets as muppet
from src import milesToMuppets as muppet

foo = muppet.MilesToMuppets(
    client_id='x',
    client_secret='x' 
)

foo.set_mile_distance(60)
foo.set_speed(30)
foo.set_album(0)
results = foo.evaluate_album(print_cycle=True)
print(results)