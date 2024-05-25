import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
import csv

class CSVTableView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSV Table Viewer")

        # Create a QTableView
        self.table_view = QTableView()

        # Set sorting behavior for the table view
        self.table_view.setSortingEnabled(True)

        # Create a layout for the central widget
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Load CSV data
        self.load_csv("all_data_output.csv")

    def load_csv(self, filename):
        with open(filename, "r", newline="") as file:
            csv_reader = csv.reader(file)
            self.model = QStandardItemModel()
            for row_num, row_data in enumerate(csv_reader):
                # Only add desired columns
                selected_columns = [0, 1, 2, 3, 7, 8, 9, 10, 11, 12]
                items = [QStandardItem(row_data[col]) for col in selected_columns]
                self.model.appendRow(items)
        
        # Set the model for the table view
        self.table_view.setModel(self.model)

        # Connect sectionClicked signal to sorting function
        self.table_view.horizontalHeader().sectionClicked.connect(self.sort_by_column)

    def sort_by_column(self, logical_index):
        self.table_view.sortByColumn(logical_index, Qt.AscendingOrder)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CSVTableView()
    window.show()
    sys.exit(app.exec())
