# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'miduCal.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(400, 300)
        self.density = QtWidgets.QLineEdit(Widget)
        self.density.setGeometry(QtCore.QRect(100, 40, 113, 21))
        self.density.setObjectName("density")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(10, 40, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(0, 80, 72, 15))
        self.label_2.setObjectName("label_2")
        self.volume = QtWidgets.QLineEdit(Widget)
        self.volume.setGeometry(QtCore.QRect(100, 80, 113, 21))
        self.volume.setObjectName("volume")
        self.label_3 = QtWidgets.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(0, 120, 72, 15))
        self.label_3.setObjectName("label_3")
        self.weight = QtWidgets.QLineEdit(Widget)
        self.weight.setGeometry(QtCore.QRect(100, 120, 113, 21))
        self.weight.setObjectName("weight")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(100, 180, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label.setBuddy(self.density)
        self.label_2.setBuddy(self.volume)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Form"))
        self.density.setText(_translate("Widget", "12"))
        self.label.setText(_translate("Widget", "密度"))
        self.label_2.setText(_translate("Widget", "体积"))
        self.volume.setText(_translate("Widget", "2"))
        self.label_3.setText(_translate("Widget", "重量"))
        self.pushButton.setText(_translate("Widget", "计算"))
