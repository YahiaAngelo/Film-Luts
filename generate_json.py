import json
import os

# Assuming thumbnails have been generated and follow a specific naming convention,
# e.g., "{LUT name}.jpg" in a directory named "thumbnails" within each category folder
extract_path = "luts"

# Function to list all LUTs across categories and prepare JSON structure
def list_luts_with_thumbnails(base_path):
    categories = os.listdir(base_path)
    luts_list = []

    for category in categories:
        luts_path = os.path.join(base_path, category)
        if os.path.isdir(luts_path):  # Ensure it's a directory
            luts = os.listdir(luts_path)
            for lut in luts:
                lut_name = os.path.splitext(lut)[0]
                lut_file = f"luts/{category}/{lut}"  # Removing the file extension
                thumbnail_path = f"thumbnails/{category}/{lut_name}.jpg"  # Hypothetical thumbnail path
                luts_list.append({
                    "name": lut_name.replace('_', ' ').title(),
                    "lut_file": lut_file,
                    "category": category.replace('_', ' ').title(),
                    "thumbnail": thumbnail_path
                })

    return luts_list

# Generate the list
film_luts = list_luts_with_thumbnails(extract_path)

# Preparing the JSON structure
json_data = {
    "filmLUTs": film_luts
}

# JSON file path
json_file_path = 'film_luts.json'

# Writing the JSON data to a file
with open(json_file_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

json_file_path
