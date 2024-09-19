import json

# Path to your JSON file
json_file_path = 'new_branch.json'

# Read JSON data from the file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Convert the values (branch names) to a list
branch_list = list(data.values())

# Path to the output Python list file
output_file_path = 'branch_list.py'

# Write the list to a Python file
with open(output_file_path, 'w') as file:
    file.write(f"branch_list = {branch_list}")

print(f"Branch list has been successfully saved to {output_file_path}")
