# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ID-H Parameter Setting Software.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(949, 476)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 321, 421))
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 280, 301, 101))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.tolerancejudgmentframe = QtWidgets.QFrame(Dialog)
        self.tolerancejudgmentframe.setGeometry(QtCore.QRect(360, 20, 281, 161))
        self.tolerancejudgmentframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tolerancejudgmentframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tolerancejudgmentframe.setObjectName("tolerancejudgmentframe")
        self.toleranceonoffframe = QtWidgets.QFrame(self.tolerancejudgmentframe)
        self.toleranceonoffframe.setGeometry(QtCore.QRect(9, 10, 261, 41))
        self.toleranceonoffframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toleranceonoffframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toleranceonoffframe.setObjectName("toleranceonoffframe")
        self.toleranceonofflabel = QtWidgets.QLabel(self.toleranceonoffframe)
        self.toleranceonofflabel.setGeometry(QtCore.QRect(10, 10, 111, 20))
        self.toleranceonofflabel.setObjectName("toleranceonofflabel")
        self.toleranceonbutton = QtWidgets.QPushButton(self.toleranceonoffframe)
        self.toleranceonbutton.setGeometry(QtCore.QRect(140, 10, 41, 23))
        self.toleranceonbutton.setCheckable(True)
        self.toleranceonbutton.setObjectName("toleranceonbutton")
        self.toleranceoffbutton = QtWidgets.QPushButton(self.toleranceonoffframe)
        self.toleranceoffbutton.setGeometry(QtCore.QRect(200, 10, 41, 23))
        self.toleranceoffbutton.setCheckable(True)
        self.toleranceoffbutton.setObjectName("toleranceoffbutton")
        self.uppertoleranceframe = QtWidgets.QFrame(self.tolerancejudgmentframe)
        self.uppertoleranceframe.setGeometry(QtCore.QRect(9, 49, 261, 51))
        self.uppertoleranceframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uppertoleranceframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uppertoleranceframe.setObjectName("uppertoleranceframe")
        self.uppertolerancevalueentry = QtWidgets.QPlainTextEdit(self.uppertoleranceframe)
        self.uppertolerancevalueentry.setGeometry(QtCore.QRect(140, 10, 104, 31))
        self.uppertolerancevalueentry.setObjectName("uppertolerancevalueentry")
        self.uppertolerancelabel = QtWidgets.QLabel(self.uppertoleranceframe)
        self.uppertolerancelabel.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.uppertolerancelabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.uppertolerancelabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.uppertolerancelabel.setObjectName("uppertolerancelabel")
        self.lowertoleranceframe = QtWidgets.QFrame(self.tolerancejudgmentframe)
        self.lowertoleranceframe.setGeometry(QtCore.QRect(10, 100, 261, 51))
        self.lowertoleranceframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lowertoleranceframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lowertoleranceframe.setObjectName("lowertoleranceframe")
        self.lowertolerancevalueentry = QtWidgets.QPlainTextEdit(self.lowertoleranceframe)
        self.lowertolerancevalueentry.setGeometry(QtCore.QRect(140, 10, 104, 31))
        self.lowertolerancevalueentry.setObjectName("lowertolerancevalueentry")
        self.lowertolerancelabel = QtWidgets.QLabel(self.lowertoleranceframe)
        self.lowertolerancelabel.setGeometry(QtCore.QRect(10, 10, 91, 31))
        self.lowertolerancelabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lowertolerancelabel.setObjectName("lowertolerancelabel")
        self.unitsframe = QtWidgets.QFrame(Dialog)
        self.unitsframe.setGeometry(QtCore.QRect(650, 20, 281, 61))
        self.unitsframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.unitsframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.unitsframe.setObjectName("unitsframe")
        self.unitslabel = QtWidgets.QLabel(self.unitsframe)
        self.unitslabel.setGeometry(QtCore.QRect(10, 10, 47, 41))
        self.unitslabel.setObjectName("unitslabel")
        self.unitsinchbutton = QtWidgets.QPushButton(self.unitsframe)
        self.unitsinchbutton.setGeometry(QtCore.QRect(180, 20, 75, 23))
        self.unitsinchbutton.setCheckable(True)
        self.unitsinchbutton.setObjectName("unitsinchbutton")
        self.unitsmmbutton = QtWidgets.QPushButton(self.unitsframe)
        self.unitsmmbutton.setGeometry(QtCore.QRect(90, 20, 75, 23))
        self.unitsmmbutton.setCheckable(True)
        self.unitsmmbutton.setObjectName("unitsmmbutton")
        self.resolutionframe = QtWidgets.QFrame(Dialog)
        self.resolutionframe.setGeometry(QtCore.QRect(650, 90, 281, 61))
        self.resolutionframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resolutionframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resolutionframe.setObjectName("resolutionframe")
        self.resolutionlabel = QtWidgets.QLabel(self.resolutionframe)
        self.resolutionlabel.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.resolutionlabel.setObjectName("resolutionlabel")
        self.resolutionselect = QtWidgets.QComboBox(self.resolutionframe)
        self.resolutionselect.setGeometry(QtCore.QRect(150, 20, 101, 22))
        self.resolutionselect.setObjectName("resolutionselect")
        self.resolutionselect.addItem("")
        self.resolutionselect.addItem("")
        self.resolutionselect.addItem("")
        self.resolutionselect.addItem("")
        self.resolutionselect.addItem("")
        self.analograngeframe = QtWidgets.QFrame(Dialog)
        self.analograngeframe.setGeometry(QtCore.QRect(650, 160, 281, 61))
        self.analograngeframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.analograngeframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.analograngeframe.setObjectName("analograngeframe")
        self.analograngelabel = QtWidgets.QLabel(self.analograngeframe)
        self.analograngelabel.setGeometry(QtCore.QRect(10, 12, 81, 41))
        self.analograngelabel.setObjectName("analograngelabel")
        self.analograngeselect = QtWidgets.QComboBox(self.analograngeframe)
        self.analograngeselect.setGeometry(QtCore.QRect(150, 20, 101, 22))
        self.analograngeselect.setObjectName("analograngeselect")
        self.analograngeselect.addItem("")
        self.measurementmodeframe = QtWidgets.QFrame(Dialog)
        self.measurementmodeframe.setGeometry(QtCore.QRect(360, 190, 281, 61))
        self.measurementmodeframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.measurementmodeframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.measurementmodeframe.setObjectName("measurementmodeframe")
        self.measurementmodelabel = QtWidgets.QLabel(self.measurementmodeframe)
        self.measurementmodelabel.setGeometry(QtCore.QRect(10, 12, 101, 41))
        self.measurementmodelabel.setObjectName("measurementmodelabel")
        self.measurementmodeselect = QtWidgets.QComboBox(self.measurementmodeframe)
        self.measurementmodeselect.setGeometry(QtCore.QRect(150, 20, 101, 22))
        self.measurementmodeselect.setObjectName("measurementmodeselect")
        self.measurementmodeselect.addItem("")
        self.measurementmodeselect.addItem("")
        self.measurementmodeselect.addItem("")
        self.measurementmodeselect.addItem("")
        self.functionlockframe = QtWidgets.QFrame(Dialog)
        self.functionlockframe.setGeometry(QtCore.QRect(650, 230, 281, 61))
        self.functionlockframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.functionlockframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.functionlockframe.setObjectName("functionlockframe")
        self.functionlocklabel = QtWidgets.QLabel(self.functionlockframe)
        self.functionlocklabel.setGeometry(QtCore.QRect(10, 10, 81, 41))
        self.functionlocklabel.setObjectName("functionlocklabel")
        self.functionlockonbutton = QtWidgets.QPushButton(self.functionlockframe)
        self.functionlockonbutton.setGeometry(QtCore.QRect(90, 20, 75, 23))
        self.functionlockonbutton.setCheckable(True)
        self.functionlockonbutton.setObjectName("functionlockonbutton")
        self.functionlockoffbutton = QtWidgets.QPushButton(self.functionlockframe)
        self.functionlockoffbutton.setGeometry(QtCore.QRect(180, 20, 75, 23))
        self.functionlockoffbutton.setCheckable(True)
        self.functionlockoffbutton.setObjectName("functionlockoffbutton")
        self.directionframe = QtWidgets.QFrame(Dialog)
        self.directionframe.setGeometry(QtCore.QRect(360, 260, 281, 61))
        self.directionframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.directionframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.directionframe.setObjectName("directionframe")
        self.directionpositivebutton = QtWidgets.QPushButton(self.directionframe)
        self.directionpositivebutton.setGeometry(QtCore.QRect(90, 20, 75, 23))
        self.directionpositivebutton.setCheckable(True)
        self.directionpositivebutton.setObjectName("directionpositivebutton")
        self.directionnegativebutton = QtWidgets.QPushButton(self.directionframe)
        self.directionnegativebutton.setGeometry(QtCore.QRect(180, 20, 75, 23))
        self.directionnegativebutton.setCheckable(True)
        self.directionnegativebutton.setObjectName("directionnegativebutton")
        self.directionlabel = QtWidgets.QLabel(self.directionframe)
        self.directionlabel.setGeometry(QtCore.QRect(6, 12, 61, 41))
        self.directionlabel.setObjectName("directionlabel")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 360, 75, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 360, 111, 81))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.toleranceonofflabel.setText(_translate("Dialog", "Tolerance Judgment"))
        self.toleranceonbutton.setText(_translate("Dialog", "ON"))
        self.toleranceoffbutton.setText(_translate("Dialog", "OFF"))
        self.uppertolerancelabel.setText(_translate("Dialog", "Upper Tolerance"))
        self.lowertolerancelabel.setText(_translate("Dialog", "Lower Tolerance"))
        self.unitslabel.setText(_translate("Dialog", "Units"))
        self.unitsinchbutton.setText(_translate("Dialog", "INCH"))
        self.unitsmmbutton.setText(_translate("Dialog", "MM"))
        self.resolutionlabel.setText(_translate("Dialog", "Resolution"))
        self.resolutionselect.setItemText(0, _translate("Dialog", "0.001mm"))
        self.resolutionselect.setItemText(1, _translate("Dialog", "0.0005mm"))
        self.resolutionselect.setItemText(2, _translate("Dialog", ".0001in"))
        self.resolutionselect.setItemText(3, _translate("Dialog", ".00005in"))
        self.resolutionselect.setItemText(4, _translate("Dialog", ".00002in"))
        self.analograngelabel.setText(_translate("Dialog", "Analog Range"))
        self.analograngeselect.setItemText(0, _translate("Dialog", "TBD"))
        self.measurementmodelabel.setText(_translate("Dialog", "Measurement Mode"))
        self.measurementmodeselect.setItemText(0, _translate("Dialog", "Normal"))
        self.measurementmodeselect.setItemText(1, _translate("Dialog", "MAX"))
        self.measurementmodeselect.setItemText(2, _translate("Dialog", "MIN"))
        self.measurementmodeselect.setItemText(3, _translate("Dialog", "TIR"))
        self.functionlocklabel.setText(_translate("Dialog", "Function Lock"))
        self.functionlockonbutton.setText(_translate("Dialog", "ON"))
        self.functionlockoffbutton.setText(_translate("Dialog", "OFF"))
        self.directionpositivebutton.setText(_translate("Dialog", "^ = POSITIVE"))
        self.directionnegativebutton.setText(_translate("Dialog", "^ = NEGATIVE"))
        self.directionlabel.setText(_translate("Dialog", "Direction"))
        self.pushButton.setText(_translate("Dialog", "Zero"))
        self.pushButton_2.setText(_translate("Dialog", "Send All Parameters"))