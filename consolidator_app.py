import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QHeaderView
from PySide6.QtCore import Qt
import csv
from ConsolidatorApp_ui import Ui_MainWindow

class ConsolidatorApp(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setStyleSheet(
    "QHeaderView::section {"
    "background-color: #00AEEF;"
    "color: white;"
    "font-size: 14px;"
  
    "padding: 2px;"
    "border: none;"  # First remove any existing borders
    "border-right: 1px solid #ffffff;"  # Then apply the right border
    "}"
)

        # Manually set the column headers
        headers = ["4digit  CVV", "PAN ", "Expire Date", "Customer Name", "Encrypted PAN", "Product Type", "Branch Code", "Branch Name", "Request Date"]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)

        # Stretch columns to fit the width of the table
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Load CSV data
        self.load_csv("output.csv")

        # Initialize sort order
        self.sort_order = Qt.AscendingOrder

    def load_csv(self, filename):
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConsolidatorApp()
    window.show()
    sys.exit(app.exec())
