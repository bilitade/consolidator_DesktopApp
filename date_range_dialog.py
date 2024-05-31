from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QDateEdit, QDialogButtonBox
from PySide6.QtCore import Qt, QDate

class DateRangeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Date Range")
        self.setModal(True)

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Start Date"))
        self.start_date_edit = QDateEdit(self)
        self.start_date_edit.setDisplayFormat("MMM d, yyyy")  # Expanded format
        self.start_date_edit.setMinimumDate(QDate(2024, 1, 1))  # Minimum date set to January 2024
        self.start_date_edit.setCalendarPopup(True)  # Show date picker on field click
        layout.addWidget(self.start_date_edit)

        layout.addWidget(QLabel("End Date"))
        self.end_date_edit = QDateEdit(self)
        self.end_date_edit.setDisplayFormat("MMM d, yyyy")  # Expanded format
        self.end_date_edit.setMinimumDate(QDate(2024, 1, 1))  # Minimum date set to January 2024
        self.end_date_edit.setCalendarPopup(True)  # Show date picker on field click
        layout.addWidget(self.end_date_edit)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(self.button_box)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
