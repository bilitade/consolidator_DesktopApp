from PySide6.QtWidgets import QMainWindow,QApplication
from  consolidator_app import ConsolidatorApp

app=QApplication()
window= ConsolidatorApp()
window.show()

app.exec()
