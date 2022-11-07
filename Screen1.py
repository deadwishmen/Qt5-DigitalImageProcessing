# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Screen1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_adaptiveThreshold(object):
    def setupUi(self, adaptiveThreshold):
        adaptiveThreshold.setObjectName("adaptiveThreshold")
        adaptiveThreshold.resize(504, 393)
        self.ButtonOK = QtWidgets.QPushButton(adaptiveThreshold)
        self.ButtonOK.setGeometry(QtCore.QRect(180, 270, 93, 28))
        self.ButtonOK.setObjectName("ButtonOK")
        self.label_4 = QtWidgets.QLabel(adaptiveThreshold)
        self.label_4.setGeometry(QtCore.QRect(100, 50, 71, 41))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(adaptiveThreshold)
        self.comboBox.setGeometry(QtCore.QRect(180, 60, 181, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(adaptiveThreshold)
        QtCore.QMetaObject.connectSlotsByName(adaptiveThreshold)

    def retranslateUi(self, adaptiveThreshold):
        _translate = QtCore.QCoreApplication.translate
        adaptiveThreshold.setWindowTitle(_translate("adaptiveThreshold", "Form"))
        self.ButtonOK.setText(_translate("adaptiveThreshold", "OK"))
        self.label_4.setText(_translate("adaptiveThreshold", "types"))

class Ui_Threshold(object):
    def setupUi(self, Threshold):
        Threshold.setObjectName("Threshold")
        Threshold.resize(504, 393)
        self.label = QtWidgets.QLabel(Threshold)
        self.label.setGeometry(QtCore.QRect(70, 40, 91, 41))
        self.label.setObjectName("label")
        self.ButtonOK = QtWidgets.QPushButton(Threshold)
        self.ButtonOK.setGeometry(QtCore.QRect(180, 270, 93, 28))
        self.ButtonOK.setObjectName("ButtonOK")
        self.lineEdit = QtWidgets.QLineEdit(Threshold)
        self.lineEdit.setGeometry(QtCore.QRect(180, 50, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Threshold)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 91, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Threshold)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 90, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Threshold)
        self.label_4.setGeometry(QtCore.QRect(70, 120, 71, 41))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Threshold)
        self.comboBox.setGeometry(QtCore.QRect(180, 130, 181, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Threshold)
        QtCore.QMetaObject.connectSlotsByName(Threshold)

    def retranslateUi(self, Threshold):
        _translate = QtCore.QCoreApplication.translate
        Threshold.setWindowTitle(_translate("Threshold", "Form"))
        self.label.setText(_translate("Threshold", "thresh"))
        self.ButtonOK.setText(_translate("Threshold", "OK"))
        self.label_2.setText(_translate("Threshold", "maxval"))
        self.label_4.setText(_translate("Threshold", "types"))


class Ui_Canny(object):
    def setupUi(self, Canny):
        Canny.setObjectName("Canny")
        Canny.resize(504, 393)
        self.label = QtWidgets.QLabel(Canny)
        self.label.setGeometry(QtCore.QRect(70, 40, 91, 41))
        self.label.setObjectName("label")
        self.ButtonOK = QtWidgets.QPushButton(Canny)
        self.ButtonOK.setGeometry(QtCore.QRect(180, 270, 93, 28))
        self.ButtonOK.setObjectName("ButtonOK")
        self.lineEdit = QtWidgets.QLineEdit(Canny)
        self.lineEdit.setGeometry(QtCore.QRect(180, 50, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Canny)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 91, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Canny)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 90, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Canny)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 121, 41))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Canny)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 140, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Canny)
        self.label_4.setGeometry(QtCore.QRect(80, 180, 71, 41))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Canny)
        self.comboBox.setGeometry(QtCore.QRect(180, 190, 73, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Canny)
        QtCore.QMetaObject.connectSlotsByName(Canny)

    def retranslateUi(self, Canny):
        _translate = QtCore.QCoreApplication.translate
        Canny.setWindowTitle(_translate("Canny", "Form"))
        self.label.setText(_translate("Canny", "Nhập t_lower"))
        self.ButtonOK.setText(_translate("Canny", "OK"))
        self.label_2.setText(_translate("Canny", "Nhập t_upper"))
        self.label_3.setText(_translate("Canny", "Nhập aperture_size"))
        self.label_4.setText(_translate("Canny", "L2Gradient"))

class Ui_LoG(object):
    def setupUi(self, LoG):
        LoG.setObjectName("LoG")
        LoG.resize(504, 393)
        self.label = QtWidgets.QLabel(LoG)
        self.label.setGeometry(QtCore.QRect(70, 40, 91, 41))
        self.label.setObjectName("label")
        self.ButtonOK = QtWidgets.QPushButton(LoG)
        self.ButtonOK.setGeometry(QtCore.QRect(180, 270, 93, 28))
        self.ButtonOK.setObjectName("ButtonOK")
        self.comboBox = QtWidgets.QComboBox(LoG)
        self.comboBox.setGeometry(QtCore.QRect(190, 50, 151, 21))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(LoG)
        QtCore.QMetaObject.connectSlotsByName(LoG)

    def retranslateUi(self, LoG):
        _translate = QtCore.QCoreApplication.translate
        LoG.setWindowTitle(_translate("LoG", "Form"))
        self.label.setText(_translate("LoG", "Nhập ksize"))
        self.ButtonOK.setText(_translate("LoG", "OK"))

class Ui_Sobel(object):
    def setupUi(self, Sobel):
        Sobel.setObjectName("Sobel")
        Sobel.resize(504, 393)
        self.label = QtWidgets.QLabel(Sobel)
        self.label.setGeometry(QtCore.QRect(70, 40, 91, 41))
        self.label.setObjectName("label")
        self.ButtonOK = QtWidgets.QPushButton(Sobel)
        self.ButtonOK.setGeometry(QtCore.QRect(180, 270, 93, 28))
        self.ButtonOK.setObjectName("ButtonOK")
        self.comboBox = QtWidgets.QComboBox(Sobel)
        self.comboBox.setGeometry(QtCore.QRect(190, 50, 151, 21))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(Sobel)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 111, 41))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(Sobel)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 90, 151, 21))
        self.comboBox_2.setObjectName("comboBox_2")

        self.retranslateUi(Sobel)
        QtCore.QMetaObject.connectSlotsByName(Sobel)

    def retranslateUi(self, Sobel):
        _translate = QtCore.QCoreApplication.translate
        Sobel.setWindowTitle(_translate("Sobel", "Form"))
        self.label.setText(_translate("Sobel", "Nhập ksize"))
        self.ButtonOK.setText(_translate("Sobel", "OK"))
        self.label_2.setText(_translate("Sobel", "Nhập d"))

class Ui_Laplacian(object):
    def setupUi(self, Laplacian):
        Laplacian.setObjectName("Laplacian")
        Laplacian.resize(504, 393)
        self.label = QtWidgets.QLabel(Laplacian)
        self.label.setGeometry(QtCore.QRect(70, 40, 91, 41))
        self.label.setObjectName("label")
        self.ButtonOK = QtWidgets.QPushButton(Laplacian)
        self.ButtonOK.setGeometry(QtCore.QRect(180, 270, 93, 28))
        self.ButtonOK.setObjectName("ButtonOK")
        self.comboBox = QtWidgets.QComboBox(Laplacian)
        self.comboBox.setGeometry(QtCore.QRect(190, 50, 151, 21))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(Laplacian)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 111, 41))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Laplacian)
        QtCore.QMetaObject.connectSlotsByName(Laplacian)

    def retranslateUi(self, Laplacian):
        _translate = QtCore.QCoreApplication.translate
        Laplacian.setWindowTitle(_translate("Laplacian", "Form"))
        self.label.setText(_translate("Laplacian", "Nhập ksize"))
        self.ButtonOK.setText(_translate("Laplacian", "OK"))


class Ui_Median(object):
    def setupUi(self, Median):
        Median.setObjectName("Median")
        Median.resize(504, 393)
        self.label = QtWidgets.QLabel(Median)
        self.label.setGeometry(QtCore.QRect(70, 40, 91, 41))
        self.label.setObjectName("label")
        self.ButtonOK = QtWidgets.QPushButton(Median)
        self.ButtonOK.setGeometry(QtCore.QRect(180, 270, 93, 28))
        self.ButtonOK.setObjectName("ButtonOK")
        self.comboBox = QtWidgets.QComboBox(Median)
        self.comboBox.setGeometry(QtCore.QRect(190, 50, 151, 21))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(Median)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 111, 41))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(Median)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 90, 191, 21))
        self.comboBox_2.setObjectName("comboBox_2")

        self.retranslateUi(Median)
        QtCore.QMetaObject.connectSlotsByName(Median)

    def retranslateUi(self, Median):
        _translate = QtCore.QCoreApplication.translate
        Median.setWindowTitle(_translate("Median", "Form"))
        self.label.setText(_translate("Median", "Nhập ksize"))
        self.ButtonOK.setText(_translate("Median", "OK"))
        self.label_2.setText(_translate("Median", "Nhập borderType"))
class Ui_Gamma(object):
    def setupUi(self, Gamma):
        Gamma.setObjectName("Gamma")
        Gamma.resize(504, 393)
        self.label = QtWidgets.QLabel(Gamma)
        self.label.setGeometry(QtCore.QRect(70, 40, 91, 41))
        self.label.setObjectName("label")
        self.lineValueGamma = QtWidgets.QLineEdit(Gamma)
        self.lineValueGamma.setGeometry(QtCore.QRect(170, 50, 113, 22))
        self.lineValueGamma.setObjectName("lineValueGamma")
        self.ButtonOK = QtWidgets.QPushButton(Gamma)
        self.ButtonOK.setGeometry(QtCore.QRect(180, 270, 93, 28))
        self.ButtonOK.setObjectName("ButtonOK")

        self.retranslateUi(Gamma)
        QtCore.QMetaObject.connectSlotsByName(Gamma)

    def retranslateUi(self, Gamma):
        _translate = QtCore.QCoreApplication.translate
        Gamma.setWindowTitle(_translate("Gamma", "Form"))
        self.label.setText(_translate("Gamma", "Nhập Gamma"))
        self.ButtonOK.setText(_translate("Gamma", "OK"))

################Affine#######################
class Ui_Translation(object):
    def setupUi(self, Translation):
        Translation.setObjectName("Translation")
        Translation.resize(472, 374)
        self.label = QtWidgets.QLabel(Translation)
        self.label.setGeometry(QtCore.QRect(60, 90, 55, 16))
        self.label.setObjectName("label")
        self.lineValueTx = QtWidgets.QLineEdit(Translation)
        self.lineValueTx.setGeometry(QtCore.QRect(120, 90, 113, 22))
        self.lineValueTx.setText("")
        self.lineValueTx.setObjectName("lineValueTx")
        self.ButtonOK = QtWidgets.QPushButton(Translation)
        self.ButtonOK.setGeometry(QtCore.QRect(180, 290, 93, 28))
        self.ButtonOK.setObjectName("ButtonOK")
        self.label_2 = QtWidgets.QLabel(Translation)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lineValueTy = QtWidgets.QLineEdit(Translation)
        self.lineValueTy.setGeometry(QtCore.QRect(120, 140, 113, 22))
        self.lineValueTy.setText("")
        self.lineValueTy.setObjectName("lineValueTy")

        self.retranslateUi(Translation)
        QtCore.QMetaObject.connectSlotsByName(Translation)

    def retranslateUi(self, Translation):
        _translate = QtCore.QCoreApplication.translate
        Translation.setWindowTitle(_translate("Translation", "Form"))
        self.label.setText(_translate("Translation", "Nhập Tx"))
        self.ButtonOK.setText(_translate("Translation", "OK"))
        self.label_2.setText(_translate("Translation", "Nhập Ty"))
class Ui_Scaling(object):
    def setupUi(self, Scaling):
        Scaling.setObjectName("Scaling")
        Scaling.resize(504, 393)
        self.label = QtWidgets.QLabel(Scaling)
        self.label.setGeometry(QtCore.QRect(100, 50, 55, 16))
        self.label.setObjectName("label")
        self.lineValueSx = QtWidgets.QLineEdit(Scaling)
        self.lineValueSx.setGeometry(QtCore.QRect(170, 50, 113, 22))
        self.lineValueSx.setObjectName("lineValueSx")
        self.label_2 = QtWidgets.QLabel(Scaling)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lineValueSy = QtWidgets.QLineEdit(Scaling)
        self.lineValueSy.setGeometry(QtCore.QRect(170, 100, 113, 22))
        self.lineValueSy.setObjectName("lineValueSy")
        self.ButtonOK = QtWidgets.QPushButton(Scaling)
        self.ButtonOK.setGeometry(QtCore.QRect(180, 270, 93, 28))
        self.ButtonOK.setObjectName("ButtonOK")

        self.retranslateUi(Scaling)
        QtCore.QMetaObject.connectSlotsByName(Scaling)

    def retranslateUi(self, Scaling):
        _translate = QtCore.QCoreApplication.translate
        Scaling.setWindowTitle(_translate("Scaling", "Form"))
        self.label.setText(_translate("Scaling", "Nhập Sx"))
        self.label_2.setText(_translate("Scaling", "Nhập Sy"))
        self.ButtonOK.setText(_translate("Scaling", "OK"))
class Ui_Rotation(object):
    def setupUi(self, Rotation):
        Rotation.setObjectName("Rotation")
        Rotation.resize(514, 394)
        self.label = QtWidgets.QLabel(Rotation)
        self.label.setGeometry(QtCore.QRect(80, 70, 55, 16))
        self.label.setObjectName("label")
        self.lineValueAngle = QtWidgets.QLineEdit(Rotation)
        self.lineValueAngle.setGeometry(QtCore.QRect(160, 70, 113, 22))
        self.lineValueAngle.setObjectName("lineValueAngle")
        self.ButtonOK = QtWidgets.QPushButton(Rotation)
        self.ButtonOK.setGeometry(QtCore.QRect(170, 280, 93, 28))
        self.ButtonOK.setObjectName("ButtonOK")

        self.retranslateUi(Rotation)
        QtCore.QMetaObject.connectSlotsByName(Rotation)

    def retranslateUi(self, Rotation):
        _translate = QtCore.QCoreApplication.translate
        Rotation.setWindowTitle(_translate("Rotation", "Form"))
        self.label.setText(_translate("Rotation", "Angle"))
        self.ButtonOK.setText(_translate("Rotation", "Ok"))
class Ui_Shearing(object):
    def setupUi(self, Shearing):
        Shearing.setObjectName("Shearing")
        Shearing.resize(514, 394)
        self.label = QtWidgets.QLabel(Shearing)
        self.label.setGeometry(QtCore.QRect(80, 70, 55, 16))
        self.label.setObjectName("label")
        self.lineValueLambda = QtWidgets.QLineEdit(Shearing)
        self.lineValueLambda.setGeometry(QtCore.QRect(160, 70, 113, 22))
        self.lineValueLambda.setObjectName("lineValueLambda")
        self.ButtonOK = QtWidgets.QPushButton(Shearing)
        self.ButtonOK.setGeometry(QtCore.QRect(170, 280, 93, 28))
        self.ButtonOK.setObjectName("ButtonOK")

        self.retranslateUi(Shearing)
        QtCore.QMetaObject.connectSlotsByName(Shearing)

    def retranslateUi(self, Shearing):
        _translate = QtCore.QCoreApplication.translate
        Shearing.setWindowTitle(_translate("Shearing", "Form"))
        self.label.setText(_translate("Shearing", "Lambda"))
        self.ButtonOK.setText(_translate("Shearing", "Ok"))