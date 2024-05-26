import csv
import json
import os
import sys

class DataProcessor:
    base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    def __init__(self, base_directory=None):
        self.base_directory = base_directory or os.getcwd()


    def get_input_directory(self, specified_directory=None):
        if specified_directory and os.path.isabs(specified_directory):
            return specified_directory
        else:
            relative_path = "./inputfiles"
            if not os.path.exists(relative_path):
                os.makedirs(relative_path)
            return relative_path



    def load_branch_data(self):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        with open(os.path.join(base_path, 'branches.json')) as json_file:
            return json.load(json_file)

    def parse_file(self, file_name, input_directory, branch_data):
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

        # Clean and process the data
        cleaned_data = data.replace('~', '').replace('^', '  ')
        rows = cleaned_data.split('\n')
        cleaned_rows = [row.split(',') for row in rows if row.strip()]

        branch_name = branch_data.get(branch_code, 'Unknown Branch')

        processed_rows = []
        for row in cleaned_rows:
            row = [column.strip() for column in row if column.strip()]
            row.append(product_name)
            row.append(branch_code)
            row.append(branch_name)
            row.append(date)
            processed_rows.append(row)

        return processed_rows

    def get_input_file_names(self, input_directory):
        return [file for file in os.listdir(input_directory) if file.startswith('PersoFile_')]

    def save_to_csv(self, output_file_name, all_rows):
        with open(output_file_name, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(all_rows)

    def process(self, specified_directory=None):

        input_directory = self.get_input_directory(specified_directory)
        branch_data = self.load_branch_data()
        all_rows = []

        input_file_names = self.get_input_file_names(input_directory)

        for input_file_name in input_file_names:
            rows = self.parse_file(input_file_name, input_directory, branch_data)
            all_rows.extend(rows)

        output_file_name='./output.csv'
        self.save_to_csv(output_file_name, all_rows)

        print(f"All data has been processed and saved to '{output_file_name}'.")

if __name__ == "__main__":
    processor = DataProcessor()
    processor.process(r"C:\Users\coop\Documents\automation projects\embossing\source_directory")
