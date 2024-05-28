import csv
import json
import os
import sys
from datetime import datetime


class DataProcessor:
    def __init__(self, base_directory=None):
        self.base_directory = base_directory or os.getcwd()
        self.base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

    def get_input_directory(self, specified_directory=None):
        if specified_directory:
            return specified_directory
        else:
            return os.path.join(self.base_directory, "inputfiles")

    def load_json_data(self, filename):
        try:
            with open(os.path.join(self.base_path, filename)) as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            print(f"Error: '{filename}' file not found.")
            return {}

    def load_branch_data(self):
        branches = self.load_json_data('branches.json')
        districts = self.load_json_data('districts.json')

        branch_data = {}

        for branch_code, branch_name in branches.items():
            district = self.find_district(branch_code, districts)
            branch_data[branch_code] = {'name': branch_name, 'district': district}

        return branch_data

    def find_district(self, branch_code, districts):
        for district, branch_codes in districts.items():
            if branch_code in branch_codes:
                return district
        return 'Unknown District'

    def parse_file(self, file_name, input_directory, branch_data):
        file_path = os.path.join(input_directory, file_name)

        file_parts = file_name.split('_')
        if len(file_parts) < 5:
            print(f"Error: Filename '{file_name}' does not have the expected format.")
            return []

        product_name = file_parts[2]
        branch_code = file_parts[3]
        date_part = file_parts[4].split('.')[0]
        date = f"20{date_part[:2]}/{date_part[2:4]}/{date_part[4:]}"

        try:
            with open(file_path, 'r') as file:
                data = file.read()
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            return []

        cleaned_data = data.replace('~', '').replace('^', '  ')
        rows = cleaned_data.split('\n')
        cleaned_rows = [row.split(',') for row in rows if row.strip()]

        branch_info = branch_data.get(branch_code, {'name': 'Unknown Branch', 'district': 'Unknown District'})
        branch_name = branch_info['name']
        branch_district = branch_info['district']
        processed_rows = []

        for row in cleaned_rows:
            row = [column.strip() for column in row if column.strip()]
            row.extend([product_name, branch_code, branch_name, branch_district, date])
            processed_rows.append(row)

        return processed_rows

    def get_input_file_names(self, input_directory):
        return [file for file in os.listdir(input_directory) if file.startswith('PersoFile_')]

    def save_to_csv(self, output_file_name, all_rows):
        try:
            with open(output_file_name, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(all_rows)
        except IOError as e:
            print(f"Error: Unable to save to '{output_file_name}'. {e}")

    def process(self, specified_directory=None):
        input_directory = self.get_input_directory(specified_directory)
        if not os.path.exists(input_directory):
            return "No folder exists. Please select the appropriate folder."

        input_file_names = self.get_input_file_names(input_directory)
        if not input_file_names:
            return "The folder is empty or does not contain embossing files."

        branch_data = self.load_branch_data()
        all_rows = []

        for input_file_name in input_file_names:
            rows = self.parse_file(input_file_name, input_directory, branch_data)
            all_rows.extend(rows)

        output_file_name = os.path.join(self.base_directory, './output.csv')
        self.save_to_csv(output_file_name, all_rows)

        print(f"All data has been processed and saved to '{output_file_name}'.")
        return "Process completed successfully"
    
    def merge_files_by_date(self, specified_directory=None):
        input_directory = self.get_input_directory(specified_directory)
        if not os.path.exists(input_directory):
            return "No folder exists. Please select the appropriate folder."

        # Get all files in the input directory
        all_files = os.listdir(input_directory)
        if not all_files:
            return "The folder is empty or does not contain any files."

        # Dictionary to hold merged data categorized by date
        merged_data = {}

        for file_name in all_files:
            # Extract the date from the file name
            date_str = file_name.split('_')[4].split('.')[0]  # Assuming the date is the fifth part of the file name
            try:
                # Correct the year by adding "20" prefix
                corrected_date_str = '20' + date_str[:6]
                # Parse the date string to ensure it's valid
                date = datetime.strptime(corrected_date_str, '%Y%m%d').date()
            except ValueError:
                continue  # Skip files with invalid date formats

            # Read the file content
            file_path = os.path.join(input_directory, file_name)
            try:
                with open(file_path, 'r') as file:
                    file_data = file.read().strip()  # Strip any leading/trailing whitespace/newlines
            except FileNotFoundError:
                continue  # Skip files that can't be found

            # Add data to the corresponding date's list
            if date not in merged_data:
                merged_data[date] = []
            merged_data[date].append(file_data)

        # Create the merged output directory if it doesn't exist
        merged_output_directory = os.path.join(self.base_directory, "Merged_embosses")
        os.makedirs(merged_output_directory, exist_ok=True)

        # Merge files for each date and write to output files
        for date, data_list in merged_data.items():
            output_file_name = f"Emboss_file_{date.strftime('%Y_%m_%d')}.txt"
            output_file_path = os.path.join(merged_output_directory, output_file_name)

            try:
                with open(output_file_path, 'w') as output_file:
                    for data in data_list:
                        output_file.write(data + '\n')  # Ensure each data block is separated by a newline
            except IOError as e:
                return f"Error: Unable to write to '{output_file_path}'. {e}"

        return "All files have been merged and saved successfully."
        input_directory = self.get_input_directory(specified_directory)
        if not os.path.exists(input_directory):
            return "No folder exists. Please select the appropriate folder."

        # Get all files in the input directory
        all_files = os.listdir(input_directory)
        if not all_files:
            return "The folder is empty or does not contain any files."

        # Dictionary to hold merged data categorized by date
        merged_data = {}

        for file_name in all_files:
            # Extract the date from the file name
            date_str = file_name.split('_')[4].split('.')[0]  # Assuming the date is the fifth part of the file name
            try:
                # Correct the year by adding "20" prefix
                corrected_date_str = '20' + date_str[:6]
                # Parse the date string to ensure it's valid
                date = datetime.strptime(corrected_date_str, '%Y%m%d').date()
            except ValueError:
                continue  # Skip files with invalid date formats

            # Read the file content
            file_path = os.path.join(input_directory, file_name)
            try:
                with open(file_path, 'r') as file:
                    file_data = file.read().strip()  # Strip any leading/trailing whitespace/newlines
            except FileNotFoundError:
                continue  # Skip files that can't be found

            # Add data to the corresponding date's list
            if date not in merged_data:
                merged_data[date] = []
            merged_data[date].append(file_data)

        # Create the merged output directory if it doesn't exist
        merged_output_directory = os.path.join(self.base_directory, "Merged_embosses")
        os.makedirs(merged_output_directory, exist_ok=True)

        # Merge files for each date and write to output files
        for date, data_list in merged_data.items():
            output_file_name = f"Emboss_file_{date.strftime('%Y_%m_%d')}.txt"
            output_file_path = os.path.join(merged_output_directory, output_file_name)

            try:
                with open(output_file_path, 'w') as output_file:
                    for data in data_list:
                        output_file.write(data)
            except IOError as e:
                return f"Error: Unable to write to '{output_file_path}'. {e}"

        return "All files have been merged and saved successfully."