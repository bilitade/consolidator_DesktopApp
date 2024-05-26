import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QHeaderView,QFileDialog
from PySide6.QtCore import Qt
import csv
import os 
from data_processor import DataProcessor;

from ConsolidatorApp_ui import Ui_MainWindow

class ConsolidatorApp(QMainWindow, Ui_MainWindow):

    base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.data_processor=DataProcessor()
        self.source_directory_line_edit.setText("./inputfile")
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setStyleSheet(
                                        "QHeaderView::section {"
                                        "background-color: #00AEEF;"
                                        "color: white;"
                                        "font-size: 14px;"
                                    
                                        "padding: 2px;"
                                        "border: none;"  # First remove any existing borders
                                        "border-right: 1px solid #ffffff;"  # Then apply the right border
                                        "}")

        # Manually set the column headers
        headers = ["4digit  CVV", "PAN ", "Expire Date", "Customer Name", "Encrypted PAN", "Product Type", "Branch Code", "Branch Name", "Request Date"]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)

        # Stretch columns to fit the width of the table
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Load CSV data
       
        self.load_csv()

        # Initialize sort order
        self.sort_order = Qt.AscendingOrder
        self.process_button.clicked.connect(self.process_data)
        self.browse_button.clicked.connect(self.browse_folder)
    def load_csv(self):
        filename=os.path.join(self.base_path,'output.csv')
        with open(filename, "r", newline="") as file:
            csv_reader = csv.reader(file)
            selected_columns = [0, 1, 2, 3, 7, 9, 10, 11, 12]

            # Add data rows to the table
            for row_data in csv_reader:
                row = [row_data[col] for col in selected_columns]
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                for col, data in enumerate(row):
                    self.tableWidget.setItem(row_position, col, QTableWidgetItem(data))

        # Connect sectionClicked signal to sorting function
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.sort_by_column)

    
    def sort_by_column(self, logical_index):
        self.tableWidget.sortItems(logical_index, self.sort_order)
        # Toggle sort order for next click
        self.sort_order = Qt.DescendingOrder if self.sort_order == Qt.AscendingOrder else Qt.AscendingOrder
       
    def process_data(self):
         source_dir = self.source_directory_line_edit.text()
         self.data_processor.process(source_dir)
         self.load_csv()

    def browse_folder(self):
        # Open a file dialog to browse for a folder
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")

        # If a folder is selected, set the path to the QLineEdit
        if folder_path:
            self.source_directory_line_edit.setText(folder_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConsolidatorApp()
    window.show()
    sys.exit(app.exec())
