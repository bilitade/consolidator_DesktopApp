from PySide6.QtWidgets import QDialog
from About_ui import Ui_Dialog  # Import the generated UI class

class AboutDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("About")
   

        # Connect the OK button to close the dialog
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
