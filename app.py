from PySide6.QtWidgets import QMainWindow,QApplication
from  consolidator_app import ConsolidatorApp
from PySide6.QtGui import QIcon
app=QApplication()
app.setWindowIcon(QIcon(":/icon.ico"))
window= ConsolidatorApp()
window.show()
app.exec()
