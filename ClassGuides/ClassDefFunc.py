import json
from class_guides import class_guides
from define_classguide import Define_ClassGuide
from define_heroes import *
from define_ocs import *
from define_mm1thru6 import *
from define_crossover import *
from define_misc import *

# Convert the list to a JSON array
with open("./ClassGuides/class_guides.json", "w") as f:
    f.write(json.dumps(class_guides, indent=4))

print("updated class guides!")