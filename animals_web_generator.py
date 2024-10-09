import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

# Load animal data
animals_data = load_data('animals_data.json')

# Generate output string with animal information
output = '' "\n"
for animal_data in animals_data:
    output += f"Name: {animal_data['name']}\n"
    if 'diet' in animal_data['characteristics']:
        output += f"Diet: {animal_data['characteristics']['diet']}\n"
    if 'locations' in animal_data:
        output += f"Location: {animal_data['locations'][0]}\n"  # First location
    if 'type' in animal_data['characteristics']:
        output += f"Type: {animal_data['characteristics']['type']}\n"
    output += "\n"  # New line for separation

# Read the HTML template
with open('animals_template.html', 'r') as template_file:
    template_content = template_file.read()

# Replace placeholder with the generated animal info
new_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', output)

# Write the new HTML content to animals.html
with open('animals.html', 'w') as output_file:
    output_file.write(new_html_content)

print("HTML file 'animals.html' has been created successfully.")
