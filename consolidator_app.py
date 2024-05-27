import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QHeaderView, QFileDialog, QHBoxLayout,QDialog,QLabel,QVBoxLayout,QPushButton,QMessageBox
from PySide6.QtCore import Qt
import csv
import os
from branch_list import get_branches
from data_processor import DataProcessor
from ConsolidatorApp_ui import Ui_MainWindow
from About import AboutDialog

class ConsolidatorApp(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Card File Consolidator App")
        self.data_processor = DataProcessor()
        self.source_directory_line_edit.setText("./inputfile")
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setStyleSheet(
            "QHeaderView::section {"
            "background-color: #00AEEF;"
            "color: white;"
            "font-size: 14px;"
            "padding: 2px;"
            "border: none;"
            "border-right: 1px solid #ffffff;"
            "}")

        self.init_ui()
        self.load_csv()
        

    def init_ui(self):
        headers = ["4digit + CVV", "PAN", "Expire Date", "Customer Name", "Encrypted PAN", "Product Type", "Branch Code", "Branch Name", "Request Date"]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.sort_order = Qt.AscendingOrder
        self.process_button.clicked.connect(self.process_data)
        self.browse_button.clicked.connect(self.browse_folder)
        self.search_button.clicked.connect(self.search_table)
        self.search_line_edit.setPlaceholderText("Search Anything...")
        self.populate_branch_filter()
        self.populate_product_filter()
        self.product_combobox.currentIndexChanged.connect(self.filter_table)
        self.branch_comboBox.currentIndexChanged.connect(self.filter_table)
        self.search_line_edit.textChanged.connect(self.search_table)
        self.reset_filter.clicked.connect(self.reset_filters)
        self.actionSave_as_CSV.triggered.connect(self.save_as_csv)
        self.actionExit.triggered.connect(self.exit_application) 
        self.actionDeveloper.triggered.connect(self.show_about_dialog)

        

    # def load_csv(self):
    #     filename = "./output.csv"
    #     if os.path.exists(filename) and os.path.getsize(filename) > 0:
    #         with open(filename, "r", newline="") as file:
    #             csv_reader = csv.reader(file)
    #             selected_columns = [0, 1, 2, 3, 7, 9, 10, 11, 12]

    #             self.tableWidget.clearContents()
    #             self.tableWidget.setRowCount(0)

    #             for row_data in csv_reader:
    #                 row = [row_data[col] for col in selected_columns]
    #                 row_position = self.tableWidget.rowCount()
    #                 self.tableWidget.insertRow(row_position)
    #                 for col, data in enumerate(row):
    #                     self.tableWidget.setItem(row_position, col, QTableWidgetItem(data))

    #         self.tableWidget.horizontalHeader().sectionClicked.connect(self.sort_by_column)
    #     else:
    #         print("CSV file is empty or does not exist.")
    
    def load_csv(self):
        filename = "./output.csv"
        if os.path.exists(filename):
            try:
                with open(filename, "r", newline="") as file:
                    csv_reader = csv.reader(file)
                    selected_columns = [0, 1, 2, 3, 7, 9, 10, 11, 12]

                    self.tableWidget.clearContents()
                    self.tableWidget.setRowCount(0)

                    for row_data in csv_reader:
                        if row_data:
                            row = [row_data[col] for col in selected_columns]
                            row_position = self.tableWidget.rowCount()
                            self.tableWidget.insertRow(row_position)
                            for col, data in enumerate(row):
                                self.tableWidget.setItem(row_position, col, QTableWidgetItem(data))

                self.tableWidget.horizontalHeader().sectionClicked.connect(self.sort_by_column)
            except Exception as e:
                print(f"Error reading CSV file: {e}")
        else:
            print("CSV file does not exist.")




    def sort_by_column(self, logical_index):
        self.tableWidget.sortItems(logical_index, self.sort_order)
        self.sort_order = Qt.DescendingOrder if self.sort_order == Qt.AscendingOrder else Qt.AscendingOrder

    def process_data(self):
        source_dir = self.source_directory_line_edit.text()
        self.data_processor.process(source_dir)
        self.load_csv()
        self.statusBar().showMessage("Process completed successfully", 5000)

    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            self.source_directory_line_edit.setText(folder_path)
    def search_table(self):
        search_query = self.search_line_edit.text().lower()
        for row in range(self.tableWidget.rowCount()):
            match = False
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item and search_query in item.text().lower():
                    match = True
                    break
            self.tableWidget.setRowHidden(row, not match)


    def populate_product_filter(self):
        # Clear existing items
        self.product_combobox.clear()

        # Add product options
        product_options = ["All Product", "GAMTA", "HAIFB"]
        self.product_combobox.addItems(product_options)

    def populate_branch_filter(self):
        # Clear existing items
        self.branch_comboBox.clear()

        # Add branch options
        branch_options = ["All Branches"]
        all_branches=get_branches()
        all_branches.sort()
        branch_options.extend(all_branches)
       
        self.branch_comboBox.addItems(branch_options)

    def filter_table(self):
        product_filter = self.product_combobox.currentText()
        branch_filter = self.branch_comboBox.currentText()

        for row in range(self.tableWidget.rowCount()):
            product = self.tableWidget.item(row, 5).text()
            branch = self.tableWidget.item(row, 7).text()

            product_match = (product_filter == "All Product" or product == product_filter)
            branch_match = (branch_filter == "All Branches" or branch == branch_filter)

            self.tableWidget.setRowHidden(row, not (product_match and branch_match))

    def reset_filters(self):
        # Clear the selected product filter
        self.product_combobox.setCurrentIndex(0)  # Assuming the "All" option is at index 0

        # Clear the selected branch filter
        self.branch_comboBox.setCurrentIndex(0)  # Assuming the "All" option is at index 0

        # Show all rows in the table
        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHidden(row, False)


    def save_as_csv(self):
        # Open a file dialog to get the save location
        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "CSV Files (*.csv);;All Files (*)")
        
        if save_path:
            # Ensure the file has the .csv extension
            if not save_path.endswith(".csv"):
                save_path += ".csv"
                
            try:
                with open(save_path, "w", newline="") as file:
                    writer = csv.writer(file)
                    headers = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
                    writer.writerow(headers)

                    # Write only visible (not hidden) rows to the CSV
                    for row in range(self.tableWidget.rowCount()):
                        if not self.tableWidget.isRowHidden(row):
                            row_data = []
                            for column in range(self.tableWidget.columnCount()):
                                item = self.tableWidget.item(row, column)
                                row_data.append(item.text() if item else "")
                            writer.writerow(row_data)

                QMessageBox.information(self, "Success", f"Data successfully saved to {save_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {e}")

    def exit_application(self):
        QApplication.quit()
    def show_about_dialog(self):
        about_dialog = AboutDialog(self)
        about_dialog.exec()

