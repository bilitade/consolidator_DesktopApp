import csv
import json
import os

# Get the current working directory
current_directory = os.getcwd()

# Define the directory containing input files
input_directory = os.path.join(current_directory, 'inputfile')

# Load branch data from JSON file
with open(os.path.join(current_directory, 'branches.json')) as json_file:
    branch_data = json.load(json_file)

# Initialize an empty list to hold all rows from all files
all_rows = []


# Function to process each file
def process_file(file_name):
    # Construct the absolute path for the file
    file_path = os.path.join(input_directory, file_name)

    # Extract the product name, branch code, and date from the file name
    file_parts = file_name.split('_')
    product_name = file_parts[2]
    branch_code = file_parts[3]
    date_part = file_parts[4].split('.')[0]
    date = f"20{date_part[:2]}/{date_part[2:4]}/{date_part[4:]}"

    # Read the input data from the file
    try:
        with open(file_path, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

    # Remove the '~' characters
    cleaned_data = data.replace('~', '')

    # Replace '^' with two white spaces
    cleaned_data = cleaned_data.replace('^', '  ')

    # Split the data into rows and columns
    rows = cleaned_data.split('\n')
    cleaned_rows = [row.split(',') for row in rows if row.strip()]

    # Get the branch name from the branch code
    branch_name = branch_data.get(branch_code, 'Unknown Branch')

    # Append the extracted information to each row
    processed_rows = []
    for row in cleaned_rows:
        # Remove empty columns
        row = [column.strip() for column in row if column.strip()]
        row.append(product_name)
        row.append(branch_code)
        row.append(branch_name)
        row.append(date)
        processed_rows.append(row)

    return processed_rows

# Get list of files in the input directory
input_file_names = [file for file in os.listdir(input_directory) if file.startswith('PersoFile_')]

# Loop through each file and process it
for input_file_name in input_file_names:
    rows = process_file(input_file_name)
    all_rows.extend(rows)

# Save the concatenated data to a CSV file
output_file_name = 'all_data_output.csv'
with open(output_file_name, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(all_rows)

print(f"All data has been processed and saved to '{output_file_name}'.")
