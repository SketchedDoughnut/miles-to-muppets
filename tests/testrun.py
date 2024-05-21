# please move this into the root directory, the same one where "src" is when running this test.

from src.milesToMuppets import muppet

foo = muppet.MilesToMuppets(
    client_id="x",
    client_secret="x",
    do_print=False
)

foo.set_mile_distance(60)
foo.set_speed(30)
foo.choose_album(1)

foo.evaluate_album()

foo.get_help()
foo.get_license()