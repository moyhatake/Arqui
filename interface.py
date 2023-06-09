# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Project(object):
    def setupUi(self, Project):
        Project.setObjectName("Project")
        Project.resize(445, 580)
        Project.setMinimumSize(QtCore.QSize(445, 580))
        Project.setMaximumSize(QtCore.QSize(445, 580))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(64, 182, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 182, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 182, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 182, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 182, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 182, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 182, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 182, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 182, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Project.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("tec.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Project.setWindowIcon(icon)
        Project.setAutoFillBackground(False)
        Project.setStyleSheet("background-color: rgb(36, 36, 36);\n"
"color: rgb(64, 182, 255);")
        self.label = QtWidgets.QLabel(Project)
        self.label.setGeometry(QtCore.QRect(110, 20, 231, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 243, 243))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(36, 36, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(243, 243, 243);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Project)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.distance = QtWidgets.QRadioButton(Project)
        self.distance.setGeometry(QtCore.QRect(80, 120, 161, 17))
        self.distance.setChecked(True)
        self.distance.setObjectName("distance")
        self.sensorSelector = QtWidgets.QDial(Project)
        self.sensorSelector.setGeometry(QtCore.QRect(260, 110, 151, 151))
        self.sensorSelector.setMaximum(4)
        self.sensorSelector.setWrapping(False)
        self.sensorSelector.setNotchTarget(4.0)
        self.sensorSelector.setNotchesVisible(True)
        self.sensorSelector.setObjectName("sensorSelector")
        self.sliderVal = QtWidgets.QSlider(Project)
        self.sliderVal.setGeometry(QtCore.QRect(320, 380, 21, 171))
        self.sliderVal.setOrientation(QtCore.Qt.Vertical)
        self.sliderVal.setObjectName("sliderVal")
        self.lcdVal = QtWidgets.QLCDNumber(Project)
        self.lcdVal.setGeometry(QtCore.QRect(320, 300, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcdVal.setFont(font)
        self.lcdVal.setAutoFillBackground(False)
        self.lcdVal.setStyleSheet("color: rgb(255, 85, 0);")
        self.lcdVal.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdVal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdVal.setSmallDecimalPoint(True)
        self.lcdVal.setDigitCount(4)
        self.lcdVal.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdVal.setObjectName("lcdVal")
        self.pauseResume = QtWidgets.QPushButton(Project)
        self.pauseResume.setGeometry(QtCore.QRect(50, 530, 81, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pauseResume.setFont(font)
        self.pauseResume.setStyleSheet("")
        self.pauseResume.setAutoDefault(False)
        self.pauseResume.setDefault(False)
        self.pauseResume.setFlat(False)
        self.pauseResume.setObjectName("pauseResume")
        self.dataVals = QtWidgets.QColumnView(Project)
        self.dataVals.setGeometry(QtCore.QRect(50, 300, 256, 211))
        self.dataVals.setFrameShadow(QtWidgets.QFrame.Plain)
        self.dataVals.setObjectName("dataVals")
        self.temperature = QtWidgets.QRadioButton(Project)
        self.temperature.setGeometry(QtCore.QRect(80, 150, 175, 17))
        self.temperature.setObjectName("temperature")
        self.humidity = QtWidgets.QRadioButton(Project)
        self.humidity.setGeometry(QtCore.QRect(80, 180, 151, 17))
        self.humidity.setObjectName("humidity")
        self.light = QtWidgets.QRadioButton(Project)
        self.light.setGeometry(QtCore.QRect(80, 210, 171, 17))
        self.light.setObjectName("light")
        self.flame = QtWidgets.QRadioButton(Project)
        self.flame.setGeometry(QtCore.QRect(80, 240, 181, 17))
        self.flame.setObjectName("flame")
        self.min = QtWidgets.QLabel(Project)
        self.min.setGeometry(QtCore.QRect(360, 540, 55, 13))
        self.min.setObjectName("min")
        self.max = QtWidgets.QLabel(Project)
        self.max.setGeometry(QtCore.QRect(360, 380, 55, 13))
        self.max.setObjectName("max")
        self.label_5 = QtWidgets.QLabel(Project)
        self.label_5.setGeometry(QtCore.QRect(320, 350, 81, 19))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Project)
        self.label_6.setGeometry(QtCore.QRect(320, 270, 81, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Project)
        QtCore.QMetaObject.connectSlotsByName(Project)

    def retranslateUi(self, Project):
        _translate = QtCore.QCoreApplication.translate
        Project.setWindowTitle(_translate("Project", "Project"))
        self.label.setText(_translate("Project", "Sensor Reading"))
        self.label_2.setText(_translate("Project", "Select a sensor for measuring"))
        self.distance.setText(_translate("Project", "Distance - HC-SR04"))
        self.pauseResume.setText(_translate("Project", "Pause"))
        self.temperature.setText(_translate("Project", "Temperature - DHT-11"))
        self.humidity.setText(_translate("Project", "Humidity - DHT-11"))
        self.light.setText(_translate("Project", "Light Detection - MH-LM393"))
        self.flame.setText(_translate("Project", "Flame Detection - KY-026"))
        self.min.setText(_translate("Project", "2cm"))
        self.max.setText(_translate("Project", "4m"))
        self.label_5.setText(_translate("Project", "Range"))
        self.label_6.setText(_translate("Project", "Last value"))
