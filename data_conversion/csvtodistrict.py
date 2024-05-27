import pandas as pd
import json

# Load the CSV file into a DataFrame
csv_file_path = 'branch_district_id.csv'
df = pd.read_csv(csv_file_path)

# Create a dictionary to hold the data
districts_dict = {}

# Group the DataFrame by 'District' and aggregate the 'Branch Code' into lists
for district, group in df.groupby('District'):
    # Convert branch codes to integers (removing decimals) and then to strings
    branch_codes = group['Branch Code'].dropna().astype(int).astype(str).tolist()
    districts_dict[district] = branch_codes

# Save the dictionary as a JSON file
json_file_path = 'districts.json'
with open(json_file_path, 'w') as json_file:
    json.dump(districts_dict, json_file, indent=4)

print(f'Districts JSON file saved to {json_file_path}')
