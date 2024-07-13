# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_add_product.ui'
#
# Created by: PyQt5 UI code generator 5.15.10

from PyQt5 import QtCore, QtGui, QtWidgets
import gui_utils

class Ui_addProductWindow(object):
    def setupUi(self, addProductWindow):
        addProductWindow.setObjectName("addProductWindow")
        addProductWindow.resize(390, 200)
        addProductWindow.setMinimumSize(QtCore.QSize(390, 200))
        addProductWindow.setMaximumSize(QtCore.QSize(390, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/rikor_ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        addProductWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(addProductWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.projectBox = QtWidgets.QComboBox(self.centralwidget)
        self.projectBox.setGeometry(QtCore.QRect(10, 30, 180, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.projectBox.setFont(font)
        self.projectBox.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.projectBox.setEditable(False)
        self.projectBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.projectBox.setObjectName("projectBox")
        self.countLine = QtWidgets.QLineEdit(self.centralwidget)
        self.countLine.setGeometry(QtCore.QRect(340, 30, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.countLine.setFont(font)
        self.countLine.setObjectName("countLine")
        self.countSlider = QtWidgets.QSlider(self.centralwidget)
        self.countSlider.setGeometry(QtCore.QRect(201, 35, 121, 22))
        self.countSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.countSlider.setOrientation(QtCore.Qt.Horizontal)
        self.countSlider.setObjectName("countSlider")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(10, 5, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.countLabel = QtWidgets.QLabel(self.centralwidget)
        self.countLabel.setGeometry(QtCore.QRect(201, 5, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.countLabel.setFont(font)
        self.countLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.countLabel.setObjectName("countLabel")
        self.bgImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.bgImageLabel.setGeometry(QtCore.QRect(0, 0, 390, 200))
        self.bgImageLabel.setStyleSheet("background-image: url(:/image 600x200/main_bg_600x200.jpg);")
        self.bgImageLabel.setText("")
        self.bgImageLabel.setObjectName("bgImageLabel")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(240, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.addButton.setFont(font)
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.addButton.setObjectName("addButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(240, 150, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.cancelButton.setFont(font)
        self.cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.cancelButton.setObjectName("cancelButton")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(5, 115, 225, 80))
        self.logoLabel.setStyleSheet("background-image: url(:/logo/rikor_logo_225x80.png);")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.bgImageLabel.raise_()
        self.projectBox.raise_()
        self.countLine.raise_()
        self.countSlider.raise_()
        self.nameLabel.raise_()
        self.countLabel.raise_()
        self.addButton.raise_()
        self.cancelButton.raise_()
        self.logoLabel.raise_()
        addProductWindow.setCentralWidget(self.centralwidget)

        self.fillProjectBox()
        self.addButton.clicked.connect(self.addProduct)
        self.countSlider.valueChanged.connect(self.changeSliderValue)
        self.countLine.textChanged.connect(self.changeLineValueBlock)
        self.cancelButton.clicked.connect(addProductWindow.close)
        self.projectBox.currentTextChanged.connect(self.changeProjectBoxValue)

        self.retranslateUi(addProductWindow)
        QtCore.QMetaObject.connectSlotsByName(addProductWindow)

    def retranslateUi(self, addProductWindow):
        _translate = QtCore.QCoreApplication.translate
        addProductWindow.setWindowTitle(_translate("addProductWindow", "Добавить готовое изделие"))
        self.countLine.setText(_translate("addProductWindow", "1"))
        self.nameLabel.setText(_translate("addProductWindow", "продукт"))
        self.countLabel.setText(_translate("addProductWindow", "количество"))
        self.addButton.setText(_translate("addProductWindow", "Добавить"))
        self.cancelButton.setText(_translate("addProductWindow", "Отмена"))

    def clearFields(self):
        self.countSlider.setValue(0)

    addProduct = gui_utils.addProduct
    fillProjectBox = gui_utils.fillProjectBox #
    changeSliderValue = gui_utils.changeSliderValue #
    changeLineValueBlock = gui_utils.changeLineValueBlock #
    changeProjectBoxValue = gui_utils.changeProjectBoxValue #
    message = gui_utils.message #

    def __init__(self, data):
        self.data = data

import main_bg_600x200_rc
import rikor_logo_225x80_rc
import rikor_logo_280x100_rc