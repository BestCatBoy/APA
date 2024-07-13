# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10

from PyQt5 import QtCore, QtGui, QtWidgets

from gui_add_component import *
from gui_add_project import *
from gui_add_product import *
import gui_utils

import sys
sys.path.append('../core')
from database_interface import connect

sys.path.pop()

class Ui_MainWindow(object):

    RIKOR = connect()
    data = {
        'комплектующие':                RIKOR.DATA.COMPONENTS,
        'выпускаемая продукция':        RIKOR.DATA.PROJECTS,
        'готовые изделия':              RIKOR.DATA.PRODUCTS}

    tables = list(data.keys())
    table = tables[0]

    def setupUi(self, MainWindow):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        palette = QtGui.QPalette()
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/rikor_ico.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableLabel = QtWidgets.QLabel(self.centralwidget)
        self.tableLabel.setGeometry(QtCore.QRect(80, 270, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.tableLabel.setFont(font)
        self.tableLabel.setStyleSheet("background-color: rgb(255, 255, 255, 180);")
        self.tableLabel.setText("комплектующие")
        self.tableLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tableLabel.setObjectName("tableLabel")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(350, 270, 71, 41))
        self.nextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextButton.setWhatsThis("")
        self.nextButton.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.nextButton.setObjectName("nextButton")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(0, 270, 71, 41))
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setAutoFillBackground(False)
        self.backButton.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.backButton.setObjectName("backButton")
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(450, 0, 351, 261))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.infoLabel.setFont(font)
        self.infoLabel.setStyleSheet("background-color: rgb(255, 255, 255, 180);\n""\n""")
        self.infoLabel.setText("")
        self.infoLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.infoLabel.setObjectName("infoLabel")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(450, 270, 171, 41))
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.addButton.setObjectName("addButton")
        self.reloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.reloadButton.setGeometry(QtCore.QRect(630, 270, 171, 41))
        self.reloadButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reloadButton.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.reloadButton.setObjectName("reloadButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(630, 560, 171, 41))
        self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitButton.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.exitButton.setObjectName("exitButton")
        self.bgLabel = QtWidgets.QLabel(self.centralwidget)
        self.bgLabel.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.bgLabel.setMinimumSize(QtCore.QSize(800, 600))
        self.bgLabel.setMaximumSize(QtCore.QSize(800, 600))
        self.bgLabel.setStyleSheet("background-image: url(:/main/main_bg.jpg);")
        self.bgLabel.setText("")
        self.bgLabel.setObjectName("bgLabel")
        self.rikorLabel = QtWidgets.QLabel(self.centralwidget)
        self.rikorLabel.setGeometry(QtCore.QRect(20, 400, 540, 200))
        self.rikorLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.rikorLabel.setStyleSheet("background-image: url(:/logo/rikor_logo.png);")
        self.rikorLabel.setText("")
        self.rikorLabel.setObjectName("rikorLabel")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 421, 261))
        self.listWidget.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.listWidget.setObjectName("listWidget")
        self.bgLabel.raise_()
        self.tableLabel.raise_()
        self.nextButton.raise_()
        self.infoLabel.raise_()
        self.addButton.raise_()
        self.reloadButton.raise_()
        self.exitButton.raise_()
        self.backButton.raise_()
        self.rikorLabel.raise_()
        self.listWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.listFill()
        self.nextButton.clicked.connect(self.nextTable)
        self.backButton.clicked.connect(self.backTable)
        self.addButton.clicked.connect(self.add)
        self.listWidget.itemClicked.connect(self.onActiveItem)
        self.exitButton.clicked.connect(MainWindow.close)
        self.reloadButton.clicked.connect(self.reload)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", gui_utils.version))
        self.nextButton.setText(_translate("MainWindow", ">>"))
        self.backButton.setText(_translate("MainWindow", "<<"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.reloadButton.setText(_translate("MainWindow", "Обновить"))
        self.exitButton.setText(_translate("MainWindow", "Выход"))

    listFill = gui_utils.listFill
    onActiveItem = gui_utils.onActiveItem
    _switchContextMenu = gui_utils._switchContextMenu
    deleteContextMenu = gui_utils.deleteContextMenu
    deleteProduct = gui_utils.deleteProduct
    _changeTable = gui_utils._changeTable
    nextTable = gui_utils.nextTable
    backTable = gui_utils.backTable
    reload = gui_utils.reload

    def add(self):
        addClasses = {
            'комплектующие':            Ui_addComponentWindow,
            'выпускаемая продукция':    Ui_addProjectWindow,
            'готовые изделия':          Ui_addProductWindow}

        self.window = QtWidgets.QMainWindow()
        self.ui = addClasses[self.table](self.RIKOR)
        self.ui.setupUi(self.window)
        self.window.show()

import main_bg_rc
import rikor_ico_rc
import rikor_logo_rc

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())