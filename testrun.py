# import milesToMuppets as muppet
from src import milesToMuppets as muppet

foo = muppet.MilesToMuppets(
    client_id='0c8bb718abf34741b5378e4c2e5fd306',
    client_secret='09cf579bfdf24781adf80a251e0f6628' 
)

foo.set_mile_distance(60)
foo.set_speed(30)
foo.set_album(0)
results = foo.evaluate_album(print_cycle=True)
print(results)