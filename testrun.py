# please move this into the root directory, the same one where "src" is when running this test.

from src.milesToMuppets import muppet


foo = muppet.MilesToMuppets(
    client_id="x",
    client_secret="x"
)

foo.set_mile_distance(60)
foo.set_speed(30)
foo.set_album(0)
foo.evaluate_album()