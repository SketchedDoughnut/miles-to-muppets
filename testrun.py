# import milesToMuppets as muppet
from src import milesToMuppets as muppet

foo = muppet.MilesToMuppets(
    client_id=input('-> '),
    client_secret=input('-> ')
)

foo.set_mile_distance(120)
# foo.set_mile_distance(60)
# foo.set_mile_distance(4.17)
foo.set_speed(30)
foo.set_album(0)
results = foo.evaluate_album(print_cycle=True)
print(results)

# # testing math
# miles = 120
# mph = 60

# # how many minutes it takes to travel a mile
# minutes_per_mile = mph / 60

# # how many minutes it takes to travel a mile * how many miles you have to travel
# minute_distance = minutes_per_mile * miles
# ms_distance = minute_distance * 1000
# print('minutes per mile:', minutes_per_mile)
# print('minute distance found:', minute_distance)
# print('ms distance found:', ms_distance)

# print('----------------------------------------------')
# leftover_minutes = 3.1 # how much time we have left
# n_minute_distance = leftover_minutes * miles
# print('new minute distance:', n_minute_distance)