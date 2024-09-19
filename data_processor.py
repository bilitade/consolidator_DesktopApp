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

        output_file_name = os.path.join(self.base_directory, 'output.csv')
        self.save_to_csv(output_file_name, all_rows)

        print(f"All data has been processed and saved to '{output_file_name}'.")
        return "Process completed successfully"

    def merge_files_by_date(self, specified_directory=None):
        input_directory = self.get_input_directory(specified_directory)
        if not os.path.exists(input_directory):
            return "No folder exists. Please select the appropriate folder."

        all_files = os.listdir(input_directory)
        if not all_files:
            return "The folder is empty or does not contain any files."

        merged_data = {}

        for file_name in all_files:
            date_str = file_name.split('_')[4].split('.')[0]
            try:
                corrected_date_str = '20' + date_str[:6]
                date = datetime.strptime(corrected_date_str, '%Y%m%d').date()
            except ValueError:
                continue

            file_path = os.path.join(input_directory, file_name)
            try:
                with open(file_path, 'r') as file:
                    file_data = file.read().strip()
            except FileNotFoundError:
                continue

            if date not in merged_data:
                merged_data[date] = []
            merged_data[date].append(file_data)

        merged_output_directory = os.path.join(self.base_directory, "Merged_by_Date")
        os.makedirs(merged_output_directory, exist_ok=True)

        timestamp = datetime.now().strftime('%H%M%S')
        for date, data_list in merged_data.items():
            output_file_name = f"PersoFile_00006_BYDATE_10000_{date.strftime('%y%m%d')}.{timestamp}"
            output_file_path = os.path.join(merged_output_directory, output_file_name)

            try:
                with open(output_file_path, 'w') as output_file:
                    for data in data_list:
                        output_file.write(data + '\n')
            except IOError as e:
                return f"Error: Unable to write to '{output_file_path}'. {e}"

        return "All files have been merged and saved successfully."

    def merge_files_by_product(self, specified_directory=None):
        input_directory = self.get_input_directory(specified_directory)
        if not os.path.exists(input_directory):
            return "No folder exists. Please make sure the 'inputfiles' folder exists."

        merged_data = {}
        all_files = os.listdir(input_directory)

        for file_name in all_files:
            parts = file_name.split('_')
            if len(parts) < 5:
                continue  # Skip files that don't match the expected format
            
            product_name = parts[2]
            file_path = os.path.join(input_directory, file_name)

            try:
                with open(file_path, 'r') as file:
                    file_data = file.read().strip()
            except FileNotFoundError:
                continue  # Skip files that can't be found

            if product_name not in merged_data:
                merged_data[product_name] = []
            merged_data[product_name].append(file_data)

        output_directory = os.path.join(self.base_directory, "Merged_By_Product")
        os.makedirs(output_directory, exist_ok=True)
        datestamp = datetime.now().strftime('%y%m%d')
        timestamp = datetime.now().strftime('%H%M%S')
        for product, data_list in merged_data.items():
            output_file_name = f"PersoFile_00006_{product}_10000_{datestamp}.{timestamp}"
            output_file_path = os.path.join(output_directory, output_file_name)

            try:
                with open(output_file_path, 'w') as output_file:
                    for data in data_list:
                        output_file.write(data + '\n')  # Ensure each data block is separated by a newline
            except IOError as e:
                return f"Error: Unable to write to '{output_file_path}'. {e}"

        return "All files have been merged by product successfully."

    def merge_files_by_date_range(self, start_date, end_date, specified_directory=None):
        input_directory = self.get_input_directory(specified_directory)
        if not os.path.exists(input_directory):
            return "No folder exists. Please select the appropriate folder."

        all_files = os.listdir(input_directory)
        if not all_files:
            return "The folder is empty or does not contain any files."

        merged_data = []

        for file_name in all_files:
            date_str = file_name.split('_')[4].split('.')[0]
            try:
                corrected_date_str = '20' + date_str[:6]
                date = datetime.strptime(corrected_date_str, '%Y%m%d').date()
            except ValueError:
                continue

            if start_date <= date <= end_date:
                file_path = os.path.join(input_directory, file_name)
                try:
                    with open(file_path, 'r') as file:
                        file_data = file.read().strip()
                        merged_data.append(file_data)
                except FileNotFoundError:
                    continue

        output_directory = os.path.join(self.base_directory, "Merged_by_date_range")
        os.makedirs(output_directory, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        output_file_name = f"PersoFile_00006_{start_date.strftime('%Y%m%d')}-{end_date.strftime('%Y%m%d')}.{timestamp}"
        output_file_path = os.path.join(output_directory, output_file_name)

        try:
            with open(output_file_path, 'w') as output_file:
                for data in merged_data:
                    output_file.write(data + '\n')
        except IOError as e:
            return f"Error: Unable to write to '{output_file_path}'. {e}"

        return f"All files within the date range have been successfully merged and saved to '{output_file_path}'."




