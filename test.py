from src import milesToMuppets

m = milesToMuppets.Muppet("0c8bb718abf34741b5378e4c2e5fd306", "62d4f6d0b2c5472fb9992555fe484d4f", 'http://localhost:8000/callback', milesToMuppets.Unit.MILES)
m._authorize()