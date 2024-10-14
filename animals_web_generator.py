import json


def load_data(file_path):
    """
    Load data from a JSON file.

    Parameters:
    file_path (str): The path to the JSON file.

    Returns:
    dict: Parsed JSON data.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """
    Serialize a single animal object to HTML list item format.

    Parameters:
    animal_obj (dict): Dictionary containing animal data.

    Returns:
    str: HTML string representing the animal.
    """
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'

    if 'diet' in animal_obj['characteristics']:
        output += f'    <strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    if 'locations' in animal_obj:
        output += f'    <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'  # Only the first location
    if 'type' in animal_obj['characteristics']:
        output += f'    <strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'

    output += '  </p>\n</li>\n'
    return output


def generate_html(animals_data, template_path, output_path):
    """
    Generate an HTML file with serialized animal data.

    Parameters:
    animals_data (list): List of animal dictionaries.
    template_path (str): Path to the HTML template file.
    output_path (str): Path to save the generated HTML file.
    """
    # Serialize each animal object and concatenate the results
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    # Read the HTML template and replace the placeholder with the serialized animals data
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    new_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', output)

    # Write the new HTML content to the output file
    with open(output_path, 'w') as output_file:
        output_file.write(new_html_content)

    print(f"HTML file '{output_path}' has been created successfully.")



animals_data = load_data('animals_data.json')


generate_html(animals_data, 'animals_template.html', 'animals.html')
