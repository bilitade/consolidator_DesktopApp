import csv
import json

# Define the input and output file paths
csv_file_path = 'branch_code_latest.csv'
json_file_path = 'new_branch.json'

# Initialize an empty dictionary to hold the JSON data
data = {}

# Read the CSV file and populate the dictionary
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        branch_name, branch_code = row
        data[branch_code] = branch_name

# Write the dictionary to a JSON file
with open(json_file_path, mode='w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"CSV data has been successfully converted to {json_file_path}")
