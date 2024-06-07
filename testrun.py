# import milesToMuppets as muppet
from src import milesToMuppets as muppet

foo = muppet.MilesToMuppets(
    client_id=input('-> '),
    client_secret=input('-> ')
)

foo.set_mile_distance(120)
foo.set_speed(30)
foo.set_album(0)
results = foo.evaluate_album(print_cycle=True)
print(results)
