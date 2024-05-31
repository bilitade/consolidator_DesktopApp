import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QFileDialog, QMessageBox
from PySide6.QtCore import Qt
import csv
import os

from branch_list import get_branches
from data_processor import DataProcessor
from ConsolidatorApp_ui import Ui_MainWindow
from About import AboutDialog
from date_range_dialog import DateRangeDialog

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
        headers = ["Last 4digit + CVV", "PAN", "Expire Date", "Customer Name", "Encrypted PAN", "Product Type", "Branch Code", "Branch Name", "District", "Request Date"]
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
        self.district_comboBox.currentIndexChanged.connect(self.filter_table)
        self.search_line_edit.textChanged.connect(self.search_table)
        self.reset_filter.clicked.connect(self.reset_filters)
        self.actionSave_as_CSV.triggered.connect(self.save_as_csv)
        self.actionExit.triggered.connect(self.exit_application)
        self.actionDeveloper.triggered.connect(self.show_about_dialog)
        self.actionBy_Date.triggered.connect(self.merge_files)
        self.actionBy_Date_Range.triggered.connect(self.show_date_range_dialog)
        self.actionBy_Product.triggered.connect(self.merge_files_by_product)
    def load_csv(self):
        filename = "./output.csv"
        if os.path.exists(filename):
            try:
                with open(filename, "r", newline="") as file:
                    csv_reader = csv.reader(file)
                    selected_columns = [0, 1, 2, 3, 7, 9, 10, 11, 12, 13]

                    self.tableWidget.clearContents()
                    self.tableWidget.setRowCount(0)

                    for row_data in csv_reader:
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
        result = self.data_processor.process(source_dir)
        if result == "No folder exists. Please select the appropriate folder.":
            QMessageBox.critical(self, "Error", result)
        elif result == "The folder is empty or does not contain embossing files.":
            QMessageBox.critical(self, "Error", result)
        else:
            self.load_csv()
            self.statusBar().showMessage(result, 5000)

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
        self.product_combobox.clear()
        product_options = ["All Product", "GAMTA", "HAIFB"]
        self.product_combobox.addItems(product_options)

    def populate_branch_filter(self):
        self.branch_comboBox.clear()
        branch_options = ["All Branches"]
        all_branches = get_branches()
        all_branches.sort()
        branch_options.extend(all_branches)
        all_districts = ["ADAMA DISTRICT", "ASELLA DISTRICT", "BAHIRDAR AREA BR RELATIONSHIP OFFICE",
                         "BALE DISTRICT", "CENTRAL FINFINE DISTRICT", "CHIRO DISTRICT", "DIRE DAWA DISTRICT",
                         "EASTERN FINFINE DISTRICT", "HAWASSA DISTRICT", "HEAD OFFICE", "HOSSANA DISTRICT",
                         "JIMMA DISTRICT", "MEKELE AREA BR RELATIONSHIP OFFICE", "NEKEMTE DISTRICT",
                         "NORTH FINFINE DISTRICT", "SHASHEMENE DISTRICT", "SOUTH FINFINE DISTRICT",
                         "WESTERN FINFINE DISTRICT"]
        all_districts.sort()
        district_options = ["All Districts"]
        district_options.extend(all_districts)
        self.district_comboBox.addItems(district_options)
        self.branch_comboBox.addItems(branch_options)

    def filter_table(self):
        product_filter = self.product_combobox.currentText()
        branch_filter = self.branch_comboBox.currentText()
        district_filter = self.district_comboBox.currentText()

        for row in range(self.tableWidget.rowCount()):
            product = self.tableWidget.item(row, 5).text()
            branch = self.tableWidget.item(row, 7).text()
            district = self.tableWidget.item(row, 8).text()

            product_match = (product_filter == "All Product" or product == product_filter)
            branch_match = (branch_filter == "All Branches" or branch == branch_filter)
            district_match = (district_filter == "All Districts" or district == district_filter)

            self.tableWidget.setRowHidden(row, not (product_match and branch_match and district_match))

    def reset_filters(self):
        self.product_combobox.setCurrentIndex(0)
        self.branch_comboBox.setCurrentIndex(0)
        self.district_comboBox.setCurrentIndex(0)
        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHidden(row, False)

    def save_as_csv(self):
        save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "CSV Files (*.csv);;All Files (*)")
        if save_path:
            if not save_path.endswith(".csv"):
                save_path += ".csv"
            try:
                with open(save_path, "w", newline="") as file:
                    writer = csv.writer(file)
                    headers = [self.tableWidget.horizontalHeaderItem(i).text() for i in range(self.tableWidget.columnCount())]
                    writer.writerow(headers)

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

    def merge_files(self):
        source_dir = self.source_directory_line_edit.text()
        result = self.data_processor.merge_files_by_date(source_dir)
        if "successfully" in result.lower():
            QMessageBox.information(self, "Success", "Emboss merged by Date Successfully")
        else:
            QMessageBox.critical(self, "Error", result)
    def show_date_range_dialog(self):
        dialog = DateRangeDialog(self)
        if dialog.exec():
            start_date = dialog.start_date_edit.date().toPython()
            end_date = dialog.end_date_edit.date().toPython()
            self.merge_files_by_date_range(start_date, end_date)

    def merge_files_by_date_range(self, start_date, end_date):
        source_dir = self.source_directory_line_edit.text()
        result = self.data_processor.merge_files_by_date_range( start_date, end_date,source_dir)
        if "successfully" in result.lower():
            QMessageBox.information(self, "Success", "Files merged by date range successfully")
        else:
            QMessageBox.critical(self, "Error", result)



    def merge_files_by_product(self):
        source_dir = self.source_directory_line_edit.text()
        result = self.data_processor.merge_files_by_product(source_dir)
        if "successfully" in result.lower():
            QMessageBox.information(self, "Success", "Files merged by product successfully")
        else:
            QMessageBox.critical(self, "Error", result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConsolidatorApp()
    window.show()
    sys.exit(app.exec())
