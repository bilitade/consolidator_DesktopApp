# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFrame(True)

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(2)
        self.dateEdit.setTimeSpec(Qt.TimeSpec.UTC)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFlat(False)

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Branch", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Product ", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFrame(True)

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(2)
        self.dateEdit.setTimeSpec(Qt.TimeSpec.UTC)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFlat(False)

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Branch", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Product ", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 0;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFrame(True)

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(2)
        self.dateEdit.setTimeSpec(Qt.TimeSpec.UTC)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFlat(False)

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Branch", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Product ", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 0;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
"QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #00AEEF;\n"
"                border-radius: 5px;\n"
"                font-size: 16px;\n"
"            }\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFrame(True)

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(2)
        self.dateEdit.setTimeSpec(Qt.TimeSpec.UTC)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFlat(False)

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Branch", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Product ", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFrame(True)

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(2)
        self.dateEdit.setTimeSpec(Qt.TimeSpec.UTC)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFlat(False)

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Branch", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Product ", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"          ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFrame(True)

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(2)
        self.dateEdit.setTimeSpec(Qt.TimeSpec.UTC)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFlat(False)

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Branch", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Product ", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"          ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFrame(True)

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(2)
        self.dateEdit.setTimeSpec(Qt.TimeSpec.UTC)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFlat(False)

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Branch", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Product ", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"          ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFrame(True)

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(2)
        self.dateEdit.setTimeSpec(Qt.TimeSpec.UTC)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Branch", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Product ", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFrame(True)

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(2)
        self.dateEdit.setTimeSpec(Qt.TimeSpec.UTC)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Branch", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Product ", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFrame(True)

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(2)
        self.dateEdit.setTimeSpec(Qt.TimeSpec.UTC)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Branch", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Product ", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFrame(True)

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(2)
        self.dateEdit.setTimeSpec(Qt.TimeSpec.UTC)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Branch", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Product ", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFrame(True)

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(2)
        self.dateEdit.setTimeSpec(Qt.TimeSpec.UTC)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Branch", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Product ", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_6.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFrame(True)

        self.horizontalLayout_6.addWidget(self.comboBox)

        self.dateEdit = QDateEdit(self.frame_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(2)
        self.dateEdit.setTimeSpec(Qt.TimeSpec.UTC)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Branch", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Product ", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.filter_date = QDateEdit(self.frame_4)
        self.filter_date.setObjectName(u"filter_date")

        self.horizontalLayout_6.addWidget(self.filter_date)

        self.filterButton = QPushButton(self.frame_4)
        self.filterButton.setObjectName(u"filterButton")

        self.horizontalLayout_6.addWidget(self.filterButton)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.filterButton.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 16px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.filter_date = QDateEdit(self.frame_4)
        self.filter_date.setObjectName(u"filter_date")

        self.horizontalLayout_6.addWidget(self.filter_date)

        self.filterButton = QPushButton(self.frame_4)
        self.filterButton.setObjectName(u"filterButton")

        self.horizontalLayout_6.addWidget(self.filterButton)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.filterButton.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 16px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.filter_date = QDateEdit(self.frame_4)
        self.filter_date.setObjectName(u"filter_date")
        self.filter_date.setDate(QDate(2024, 4, 1))

        self.horizontalLayout_6.addWidget(self.filter_date)

        self.filterButton = QPushButton(self.frame_4)
        self.filterButton.setObjectName(u"filterButton")

        self.horizontalLayout_6.addWidget(self.filterButton)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.filter_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.filterButton.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 16px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.filter_date = QDateEdit(self.frame_4)
        self.filter_date.setObjectName(u"filter_date")
        self.filter_date.setCalendarPopup(True)
        self.filter_date.setDate(QDate(2024, 4, 1))

        self.horizontalLayout_6.addWidget(self.filter_date)

        self.filterButton = QPushButton(self.frame_4)
        self.filterButton.setObjectName(u"filterButton")

        self.horizontalLayout_6.addWidget(self.filterButton)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.filter_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.filterButton.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 16px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.filter_date = QDateEdit(self.frame_4)
        self.filter_date.setObjectName(u"filter_date")
        self.filter_date.setCalendarPopup(True)
        self.filter_date.setDate(QDate(2024, 2, 17))

        self.horizontalLayout_6.addWidget(self.filter_date)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_6.addWidget(self.pushButton)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.filter_date.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset Filters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 16px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_6.addWidget(self.pushButton)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset Filters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 16px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_6.addWidget(self.pushButton)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset Filters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 16px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_6.addWidget(self.pushButton)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Reset Filters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 16px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.reset_filter = QPushButton(self.frame_4)
        self.reset_filter.setObjectName(u"reset_filter")

        self.horizontalLayout_6.addWidget(self.reset_filter)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.reset_filter.setText(QCoreApplication.translate("MainWindow", u"Reset Filters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 16px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionSave_as_CSV = QAction(MainWindow)
        self.actionSave_as_CSV.setObjectName(u"actionSave_as_CSV")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.reset_filter = QPushButton(self.frame_4)
        self.reset_filter.setObjectName(u"reset_filter")

        self.horizontalLayout_6.addWidget(self.reset_filter)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave_as_CSV)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionSave_as_CSV.setText(QCoreApplication.translate("MainWindow", u"Save as CSV", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit ", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.reset_filter.setText(QCoreApplication.translate("MainWindow", u"Reset Filters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1213, 935)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 16px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionSave_as_CSV = QAction(MainWindow)
        self.actionSave_as_CSV.setObjectName(u"actionSave_as_CSV")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionDeveloper = QAction(MainWindow)
        self.actionDeveloper.setObjectName(u"actionDeveloper")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.reset_filter = QPushButton(self.frame_4)
        self.reset_filter.setObjectName(u"reset_filter")

        self.horizontalLayout_6.addWidget(self.reset_filter)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1213, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave_as_CSV)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionDeveloper)
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionSave_as_CSV.setText(QCoreApplication.translate("MainWindow", u"Save as CSV", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit ", None))
        self.actionDeveloper.setText(QCoreApplication.translate("MainWindow", u"Developer", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.reset_filter.setText(QCoreApplication.translate("MainWindow", u"Reset Filters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1161, 751)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 2px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AEEF; /* Blue border "
                        "when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 16px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionSave_as_CSV = QAction(MainWindow)
        self.actionSave_as_CSV.setObjectName(u"actionSave_as_CSV")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionDeveloper = QAction(MainWindow)
        self.actionDeveloper.setObjectName(u"actionDeveloper")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.reset_filter = QPushButton(self.frame_4)
        self.reset_filter.setObjectName(u"reset_filter")

        self.horizontalLayout_6.addWidget(self.reset_filter)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1161, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave_as_CSV)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionDeveloper)
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionSave_as_CSV.setText(QCoreApplication.translate("MainWindow", u"Save as CSV", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit ", None))
        self.actionDeveloper.setText(QCoreApplication.translate("MainWindow", u"Developer", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.reset_filter.setText(QCoreApplication.translate("MainWindow", u"Reset Filters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1439, 895)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"              \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 1px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AE"
                        "EF; /* Blue border when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 14px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionSave_as_CSV = QAction(MainWindow)
        self.actionSave_as_CSV.setObjectName(u"actionSave_as_CSV")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionDeveloper = QAction(MainWindow)
        self.actionDeveloper.setObjectName(u"actionDeveloper")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.reset_filter = QPushButton(self.frame_4)
        self.reset_filter.setObjectName(u"reset_filter")

        self.horizontalLayout_6.addWidget(self.reset_filter)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1439, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave_as_CSV)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionDeveloper)
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionSave_as_CSV.setText(QCoreApplication.translate("MainWindow", u"Save as CSV", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit ", None))
        self.actionDeveloper.setText(QCoreApplication.translate("MainWindow", u"Developer", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.reset_filter.setText(QCoreApplication.translate("MainWindow", u"Reset Filters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1439, 895)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"              \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 1px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AE"
                        "EF; /* Blue border when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 14px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionSave_as_CSV = QAction(MainWindow)
        self.actionSave_as_CSV.setObjectName(u"actionSave_as_CSV")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionDeveloper = QAction(MainWindow)
        self.actionDeveloper.setObjectName(u"actionDeveloper")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.reset_filter = QPushButton(self.frame_4)
        self.reset_filter.setObjectName(u"reset_filter")

        self.horizontalLayout_6.addWidget(self.reset_filter)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1439, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave_as_CSV)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionDeveloper)
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionSave_as_CSV.setText(QCoreApplication.translate("MainWindow", u"Save as CSV", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit ", None))
        self.actionDeveloper.setText(QCoreApplication.translate("MainWindow", u"Developer", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.reset_filter.setText(QCoreApplication.translate("MainWindow", u"Reset Filters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1439, 895)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"              \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 1px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AE"
                        "EF; /* Blue border when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 14px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionSave_as_CSV = QAction(MainWindow)
        self.actionSave_as_CSV.setObjectName(u"actionSave_as_CSV")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionDeveloper = QAction(MainWindow)
        self.actionDeveloper.setObjectName(u"actionDeveloper")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")
        icon = QIcon(QIcon.fromTheme(u"edit-find"))
        self.search_button.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.reset_filter = QPushButton(self.frame_4)
        self.reset_filter.setObjectName(u"reset_filter")
        icon1 = QIcon(QIcon.fromTheme(u"view-refresh"))
        self.reset_filter.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.reset_filter)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")
        icon2 = QIcon(QIcon.fromTheme(u"folder"))
        self.browse_button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        icon3 = QIcon(QIcon.fromTheme(u"document-properties"))
        self.process_button.setIcon(icon3)
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1439, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave_as_CSV)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionDeveloper)
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionSave_as_CSV.setText(QCoreApplication.translate("MainWindow", u"Save as CSV", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit ", None))
        self.actionDeveloper.setText(QCoreApplication.translate("MainWindow", u"Developer", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.reset_filter.setText(QCoreApplication.translate("MainWindow", u"Reset Filters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConsolidatorApp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1439, 895)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"                background-color: #00AEEF;  /* Primary color */\n"
"                color: #ffffff;  /* Text color */\n"
"                padding: 5px 10px;  /* Padding */\n"
"                border: none;  /* No border */\n"
"                border-radius: 2px;  /* Remove border radius */\n"
"                font-size: 1rem;  /* Font size */\n"
"                margin: 0;  /* Remove margin */\n"
"              \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0099CC;  /* Slightly darker blue for hover */\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #0088BB;  /* Even darker blue for pressed */\n"
"            }\n"
"\n"
" QLineEdit {\n"
"                padding: 1px;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 10px; /* Rounded corners */\n"
"                font-size: 16px;\n"
"            }\n"
"            QLineEdit:focus {\n"
"                border: 1px solid #00AE"
                        "EF; /* Blue border when focused */\n"
"            }\n"
"\n"
"QComboBox,QDateEdit{\n"
"   font-size: 14px;\n"
"\n"
"\n"
"}\n"
"\n"
"          ")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionSave_as_CSV = QAction(MainWindow)
        self.actionSave_as_CSV.setObjectName(u"actionSave_as_CSV")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionDeveloper = QAction(MainWindow)
        self.actionDeveloper.setObjectName(u"actionDeveloper")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_line_edit = QLineEdit(self.frame_3)
        self.search_line_edit.setObjectName(u"search_line_edit")

        self.horizontalLayout_2.addWidget(self.search_line_edit)

        self.search_button = QPushButton(self.frame_3)
        self.search_button.setObjectName(u"search_button")
        icon = QIcon(QIcon.fromTheme(u"edit-find"))
        self.search_button.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, -1, -1, -1)
        self.branch_comboBox = QComboBox(self.frame_4)
        self.branch_comboBox.setObjectName(u"branch_comboBox")

        self.horizontalLayout_6.addWidget(self.branch_comboBox)

        self.product_combobox = QComboBox(self.frame_4)
        self.product_combobox.setObjectName(u"product_combobox")

        self.horizontalLayout_6.addWidget(self.product_combobox)

        self.reset_filter = QPushButton(self.frame_4)
        self.reset_filter.setObjectName(u"reset_filter")
        icon1 = QIcon(QIcon.fromTheme(u"view-refresh"))
        self.reset_filter.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.reset_filter)


        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.source_directory_line_edit = QLineEdit(self.frame_2)
        self.source_directory_line_edit.setObjectName(u"source_directory_line_edit")

        self.horizontalLayout.addWidget(self.source_directory_line_edit)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")
        icon2 = QIcon(QIcon.fromTheme(u"folder"))
        self.browse_button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.browse_button)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.process_button = QPushButton(self.frame_2)
        self.process_button.setObjectName(u"process_button")
        icon3 = QIcon(QIcon.fromTheme(u"document-properties"))
        self.process_button.setIcon(icon3)
        self.process_button.setFlat(False)

        self.horizontalLayout_5.addWidget(self.process_button)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(156, 146))
        self.label.setMaximumSize(QSize(156, 156))
        self.label.setPixmap(QPixmap(u":/images/images/companylogo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(156, 156))
        self.label_3.setMaximumSize(QSize(156, 156))
        self.label_3.setPixmap(QPixmap(u":/images/images/applogo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1439, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave_as_CSV)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionDeveloper)
        self.menuHelp.addAction(self.actionDocumentation)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionSave_as_CSV.setText(QCoreApplication.translate("MainWindow", u"Save as CSV", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit ", None))
        self.actionDeveloper.setText(QCoreApplication.translate("MainWindow", u"Developer", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.branch_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Branch", None))
        self.product_combobox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.reset_filter.setText(QCoreApplication.translate("MainWindow", u"Reset Filters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Source Directory ", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.process_button.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"4-digit + CVV", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PAN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Expiry Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        self.label.setText("")
        self.label_3.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

