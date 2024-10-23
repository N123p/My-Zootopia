import json
import data_fetcher

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
        output += f'    <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'
    if 'type' in animal_obj['characteristics']:
        output += f'    <strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'

    output += '  </p>\n</li>\n'
    return output

def generate_html(animals_data, template_path, output_path, animal_name):
    """
    Generate an HTML file with serialized animal data or a message if the animal doesn't exist.

    Parameters:
    animals_data (list): List of animal dictionaries.
    template_path (str): Path to the HTML template file.
    output_path (str): Path to save the generated HTML file.
    animal_name (str): The name of the animal that was searched for.
    """
    output = ''

    if animals_data:
        # Serialize each animal object
        for animal_obj in animals_data:
            output += serialize_animal(animal_obj)
    else:
        # Display a message if animal is not exits
        output = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>\n'

    # Reads the HTML template and replace the placeholder with the serialized animals data or the message
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    new_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', output)

    # Writes the new HTML content to the output file
    with open(output_path, 'w') as output_file:
        output_file.write(new_html_content)

    print(f"Website was successfully generated to the file '{output_path}'.")

def main():
    try:
        # Ask user for an animal name
        animal_name = input("Enter a name of an animal: ")

        # Fetch data from the API using the user-provided animal name
        animals_data = data_fetcher.fetch_data(animal_name)

        # Generate HTML file
        generate_html(animals_data, 'animals_template.html', 'animals.html', animal_name)

    except FileNotFoundError as file_error:
        print(f"Error: {file_error}")
    except json.JSONDecodeError as json_error:
        print(f"Error decoding JSON: {json_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
