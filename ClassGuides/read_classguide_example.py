import json

# Load the class guides from the JSON file
with open("class_guides.json") as f:
    class_guides = json.load(f)

# Prompt the user for a class name
class_name = input("Enter a class name: ")

# Find the class guide with the matching name
for class_guide in class_guides:
    if class_guide["name"].lower() == class_name.lower():
        print(f"Description: {class_guide['desc']}")
        print(f"Main attack: {class_guide['main']}")
        print(f"Alt attack: {class_guide['alt']}")
        print(f"Item: {class_guide['item']}")
        print(f"Reloadable: {class_guide['reload']}")
        print(f"User1: {class_guide['user1']}")
        print(f"User2: {class_guide['user2']}")
        print(f"Passive ability: {class_guide['passive']}")
        print(f"Wall jumps: {class_guide['wallJumps']}")
        print(f"Air jumps: {class_guide['airJumps']}")
        break
else:
    print(f"No class guide found with the name '{class_name}'.")
