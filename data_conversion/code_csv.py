import pandas as pd
import json

# Load the CSV file into a DataFrame
csv_file_path = 'branches.csv'
df = pd.read_csv(csv_file_path)

# Load the JSON file into a dictionary
json_file_path = 'branches.json'
with open(json_file_path, 'r') as f:
    branches_dict = json.load(f)

# Reverse the dictionary to match branch names to codes
branches_reverse_dict = {v: k for k, v in branches_dict.items()}

# Add a new column 'Branch Code' to the DataFrame by mapping the 'Branch Name'
df['Branch Code'] = df['Branch Name'].map(branches_reverse_dict)

# Save the updated DataFrame to a new CSV file
new_csv_file_path = 'updated_branches.csv'
df.to_csv(new_csv_file_path, index=False)

print(f'Updated CSV file saved to {new_csv_file_path}')
