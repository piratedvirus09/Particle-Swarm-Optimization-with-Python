# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maingui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 488)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 581, 21))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 581, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 581, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 110, 581, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 581, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 180, 581, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 581, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 250, 581, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 420, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 420, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 290, 581, 121))
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 20, 421, 20))
        self.lineEdit_5.setInputMask("")
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 50, 421, 20))
        self.lineEdit_6.setInputMask("")
        self.lineEdit_6.setReadOnly(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(150, 80, 421, 20))
        self.lineEdit_7.setInputMask("")
        self.lineEdit_7.setReadOnly(False)
        self.lineEdit_7.setObjectName("lineEdit_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGroup_members = QtWidgets.QAction(MainWindow)
        self.actionGroup_members.setObjectName("actionGroup_members")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionPreset_Inputs = QtWidgets.QAction(MainWindow)
        self.actionPreset_Inputs.setObjectName("actionPreset_Inputs")
        self.actionMatplotlib = QtWidgets.QAction(MainWindow)
        self.actionMatplotlib.setObjectName("actionMatplotlib")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.actionExit.setObjectName("actionExit")
        self.menuOptions.addAction(self.actionPreset_Inputs)
        self.menuOptions.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionGroup_members)
        self.menuAbout.addAction(self.actionHelp)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Particle Swarm Optimization"))
        self.lineEdit.setToolTip(_translate("MainWindow", "Enter initial starting location as a list (enclosed within square brackets)"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "  x1, x2, ..."))
        self.label.setText(_translate("MainWindow", "Enter the initial starting location:"))
        self.label_2.setText(_translate("MainWindow", "Enter the input bounds:"))
        self.lineEdit_2.setToolTip(_translate("MainWindow", "Enter the input bounds as a list of tuples"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "  x1_min, x1_max, x2_min, x2_max, ..."))
        self.label_3.setText(_translate("MainWindow", "Enter the number of particles:"))
        self.lineEdit_3.setToolTip(_translate("MainWindow", "Enter the number of particles"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "  number of particles"))
        self.label_4.setText(_translate("MainWindow", "Enter the maximum number of iterations:"))
        self.lineEdit_4.setToolTip(_translate("MainWindow", "Enter the maximum number of iterations"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "  maximum iterations"))
        self.pushButton.setToolTip(_translate("MainWindow", "CLick to execute"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.groupBox.setToolTip(_translate("MainWindow", "For best results, do not change the default values!"))
        self.groupBox.setTitle(_translate("MainWindow", "PSO Parameters:"))
        self.label_5.setText(_translate("MainWindow", "Inertial weight:"))
        self.lineEdit_5.setToolTip(_translate("MainWindow", "Enter the weight (w)"))
        self.lineEdit_5.setText(_translate("MainWindow", "0.5"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "  constant inertia weight"))
        self.label_6.setText(_translate("MainWindow", "Cognitive Constant:"))
        self.lineEdit_6.setToolTip(_translate("MainWindow", "Enter the cognitive constant (c1)"))
        self.lineEdit_6.setText(_translate("MainWindow", "1"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "  cognitive constant"))
        self.label_7.setText(_translate("MainWindow", "Social Constant:"))
        self.lineEdit_7.setToolTip(_translate("MainWindow", "Enter the social constant (c2)"))
        self.lineEdit_7.setText(_translate("MainWindow", "2"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "  social constant"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionGroup_members.setText(_translate("MainWindow", "Group members"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionPreset_Inputs.setText(_translate("MainWindow", "Preset Inputs"))
        self.actionMatplotlib.setText(_translate("MainWindow", "Matplotlib"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

