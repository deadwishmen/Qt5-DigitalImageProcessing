import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt,QObject
from Display import Ui_MainWindow
from Screen1 import Ui_Translation, Ui_Scaling, Ui_Rotation, Ui_Shearing, Ui_Gamma, Ui_Median, Ui_Laplacian, Ui_Sobel, Ui_LoG, Ui_Canny, Ui_Threshold, Ui_adaptiveThreshold
# from Screen2 import Ui_Median
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog
import cv2
from utill import *
import numpy as np
class MainWindown(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image = QWidget()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.path = ''
        # self.uic.bnt1.clicked.connect(lambda: self.OpenSubmitWin1())
        self.uic.action_Scaling.triggered.connect(lambda: self.OpenSubmitWin2())
        self.uic.action_Translation.triggered.connect(lambda: self.OpenSubmitWin1())
        self.uic.action_Rotation.triggered.connect(lambda: self.OpenSubmitWin3())
        self.uic.action_Shearing.triggered.connect(lambda: self.OpenSubmitWin4())
        self.uic.action_Gamma.triggered.connect(lambda: self.OpenSubmitWin5())
        self.uic.action_Median.triggered.connect(lambda: self.OpenSubmitWin6(1))
        self.uic.action_Gaussian.triggered.connect(lambda: self.OpenSubmitWin6(2))
        self.uic.action_Laplacian.triggered.connect(lambda: self.OpenSubmitWin8())
        self.uic.action_Sobel.triggered.connect(lambda : self.OpenSubmitWin9())
        self.uic.actionLoG.triggered.connect(lambda : self.OpenSubmitWin10())
        self.uic.actionCanny.triggered.connect(lambda : self.OpenSubmitWin11())
        self.uic.actionHistogram.triggered.connect(lambda: self.RunHistogram())
        self.uic.action_Threshold.triggered.connect(lambda : self.OpenSubmitWin12())
        self.uic.action_Adaptive_2.triggered.connect(lambda : self.OpenSubmitWin13())
        self.uic.action_Open_3.triggered.connect(lambda: self.openFileNameDialog())
    def OpenSubmitWin13(self):
        self.Second_Win = QtWidgets.QMainWindow()
        self.uic13 = Ui_adaptiveThreshold()
        self.uic13.setupUi(self.Second_Win)
        self.uic13.comboBox.addItems(['cv2.THRESH_BINARY', 'cv2.ADAPTIVE_THRESH_MEAN_C,\cv2.THRESH_BINARY', 'cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\cv.THRESH_BINARY', 'cv2.THRESH_TOZERO', 'cv2.THRESH_TOZERO_INV'])
        self.uic13.ButtonOK.clicked.connect(lambda: self.runDig(13))
        self.Second_Win.show()
    def OpenSubmitWin12(self):
        self.Second_Win = QtWidgets.QMainWindow()
        self.uic12 = Ui_Threshold()
        self.uic12.setupUi(self.Second_Win)
        self.uic12.comboBox.addItems(['cv2.THRESH_BINARY', 'cv2.THRESH_BINARY_INV', 'cv2.THRESH_TRUNC', 'cv2.THRESH_TOZERO', 'cv2.THRESH_TOZERO_INV'])
        self.uic12.ButtonOK.clicked.connect(lambda: self.runDig(12))
        self.Second_Win.show()
    def OpenSubmitWin11(self):
        self.Second_Win = QtWidgets.QMainWindow()
        self.uic11 = Ui_Canny()
        self.uic11.setupUi(self.Second_Win)
        self.uic11.comboBox.addItems(['True', 'False'])
        self.uic11.ButtonOK.clicked.connect(lambda: self.runDig(11))
        self.Second_Win.show()

    def OpenSubmitWin10(self):
        self.Second_Win = QtWidgets.QMainWindow()
        self.uic10 = Ui_LoG()
        self.uic10.setupUi(self.Second_Win)
        self.uic10.comboBox.addItems(['3','5','7','9'])
        self.uic10.ButtonOK.clicked.connect(lambda: self.runDig(10))
        self.Second_Win.show()

    def OpenSubmitWin9(self):
        self.Second_Win = QtWidgets.QMainWindow()
        self.uic9 = Ui_Sobel()
        self.uic9.setupUi(self.Second_Win)
        self.uic9.comboBox.addItems(['3','5','7','9'])
        self.uic9.comboBox_2.addItems(['dx', 'dy', 'dxy'])
        self.uic9.ButtonOK.clicked.connect(lambda: self.runDig(9))
        self.Second_Win.show()
    def OpenSubmitWin8(self):
        self.Second_Win = QtWidgets.QMainWindow()
        self.uic8 = Ui_Laplacian()
        self.uic8.setupUi(self.Second_Win)
        self.uic8.comboBox.addItems(['3'])
        self.uic8.ButtonOK.clicked.connect(lambda: self.runDig(8))
        self.Second_Win.show()
    def OpenSubmitWin6(self, id):
        self.Second_Win = QtWidgets.QMainWindow()
        self.uic6 = Ui_Median()
        self.uic6.setupUi(self.Second_Win)
        self.uic6.comboBox.addItems(['3','5','7','9'])
        self.uic6.comboBox_2.addItems(['cv2.BORDER_CONSTANT', 'cv2.BORDER_REFLECT', 'cv2.BORDER_REFLECT_101', 'cv2.BORDER_REPLICATE', 'cv2.BORDER_WRAP'])
        if id == 1:
            self.uic6.ButtonOK.clicked.connect(lambda: self.runDig(6))
        if id ==2:
            self.uic6.ButtonOK.clicked.connect(lambda: self.runDig(7))
        self.Second_Win.show()
    def OpenSubmitWin5(self):
        self.Second_Win = QtWidgets.QMainWindow()
        self.uic5 = Ui_Gamma()
        self.uic5.setupUi(self.Second_Win)
        self.uic5.ButtonOK.clicked.connect(lambda: self.runDig(5))
        self.Second_Win.show()
    ###############Rotation###########################
    def OpenSubmitWin3(self):
        self.Second_Win = QtWidgets.QMainWindow()
        self.uic3 = Ui_Rotation()
        self.uic3.setupUi(self.Second_Win)
        self.uic3.ButtonOK.clicked.connect(lambda: self.runDig(3))
        self.Second_Win.show()
    ###############Shearing###########################
    def OpenSubmitWin4(self):
        self.Second_Win = QtWidgets.QMainWindow()
        self.uic4 = Ui_Shearing()
        self.uic4.setupUi(self.Second_Win)
        self.uic4.ButtonOK.clicked.connect(lambda: self.runDig(4))
        self.Second_Win.show()
    ###############Scaling###########################
    def OpenSubmitWin2(self):
        self.Second_Win = QtWidgets.QMainWindow()
        self.uic2 = Ui_Scaling()
        self.uic2.setupUi(self.Second_Win)
        self.uic2.ButtonOK.clicked.connect(lambda: self.runDig(2))
        self.Second_Win.show()
    ###############Translation###########################
    def OpenSubmitWin1(self):
        self.Second_Win = QtWidgets.QMainWindow()
        self.uic1 = Ui_Translation()
        self.uic1.setupUi(self.Second_Win)
        self.uic1.ButtonOK.clicked.connect(lambda: self.runDig(1))
        self.Second_Win.show()
    ###############RUN###########################
    def run(self):
        print(self.path)
        self.cv_img = cv2.imread(self.path)
        qt_img = self.convert_cv_qt(self.cv_img)
        self.uic.label.setPixmap(qt_img)
    def runDig(self, i):
        if (i==1):
            Tx = int(self.uic1.lineValueTx.text())
            Ty = int(self.uic1.lineValueTy.text())
            self.cv_img = Translation(self.cv_img,Tx, Ty )
        if(i==2):
            Sx = float(self.uic2.lineValueSx.text())
            Sy = float(self.uic2.lineValueSy.text())
            self.cv_img = Scaling(self.cv_img, Sx, Sy)
        if(i==3):
            angle = float(self.uic3.lineValueAngle.text())
            self.cv_img = Rotation(self.cv_img, angle)
        if(i==4):
            lambda1 = float(self.uic4.lineValueLambda.text())
            self.cv_img = Shearing(self.cv_img,lambda1)
        if(i==5):
            gamma = float(self.uic5.lineValueGamma.text())
            self.cv_img = adjust_gamma(self.cv_img, gamma)
        if(i==6):
            ksize = int(self.uic6.comboBox.currentText())
            borderType = self.uic6.comboBox_2.currentText()
            self.cv_img = Median(self.cv_img, ksize, borderType)
        if(i==7):
            ksize = int(self.uic6.comboBox.currentText())
            borderType = self.uic6.comboBox_2.currentText()
            self.cv_img = Gaussian(self.cv_img, ksize, borderType)
        if(i==8):
            ksize = int(self.uic8.comboBox.currentText())
            self.cv_img = Laplacina(self.cv_img, ksize)
        if(i==9):
            ksize = int(self.uic9.comboBox.currentText())
            d = self.uic9.comboBox_2.currentText()
            self.cv_img = Sobel(self.cv_img, ksize, d)
        if(i==10):
            ksize = int(self.uic10.comboBox.currentText())
            self.cv_img = LoG(self.cv_img, ksize)
        if (i == 11):
            t_lower = int(self.uic11.lineEdit.text())
            t_upper = int(self.uic11.lineEdit_2.text())
            aperture_size = int(self.uic11.lineEdit_3.text())
            L2Gradient = self.uic11.comboBox.currentText()
            self.cv_img = Canny(self.cv_img, t_lower, t_upper, aperture_size, L2Gradient)
        if (i == 12):
            thresh = int(self.uic12.lineEdit.text())
            maxval = int(self.uic12.lineEdit_2.text())
            types = self.uic12.comboBox.currentText()
            self.cv_img = Threshold(self.cv_img, thresh, maxval, types)
        if (i == 13):
            types = self.uic13.comboBox.currentText()
            self.cv_img = adaptiveThreshold(self.cv_img, types)
        qt_img = self.convert_cv_qt(self.cv_img)
        self.uic.label_2.setPixmap(qt_img)
        self.Second_Win.close()
    def RunHistogram(self):
        self.cv_img = equalizeHist(self.cv_img)
        qt_img = self.convert_cv_qt(self.cv_img)
        self.uic.label_2.setPixmap(qt_img)
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            # print(fileName)
            self.path = fileName
            self.run()
        else:
            print("ko xuat duoc")
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        # rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        #rgb_image = cv_img
        id = 0
        # if len(cv_img.shape) == 3:
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        # else:
        #     id = 1
        #     rgb_image = cv_img
        #     h, w = rgb_image.shape
        #     ch = 1
        bytes_per_line = ch * w

        if ch == 3:
            convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        # if id == 1:
        #     convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h,rgb_image.strides[0], QtGui.QImage.Format_Indexed8)
        p = convert_to_Qt_format.scaled(800, 600, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindown()
    main_win.show()
    sys.exit(app.exec())