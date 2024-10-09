import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


# Load the data from the JSON file
animals_data = load_data('animals_data.json')

# Iterate over each animal in the data
for animal in animals_data:
    # Check and print each field if it exists
    if "name" in animal:
        print(f"Name: {animal['name']}")

    if "characteristics" in animal:
        characteristics = animal["characteristics"]
        if "diet" in characteristics:
            print(f"Diet: {characteristics['diet']}")

        if "type" in characteristics:
            print(f"Type: {characteristics['type']}")

    if "locations" in animal and animal["locations"]:
        print(f"Location: {animal['locations'][0]}")

    print()  # Print a blank line after each animal's details
