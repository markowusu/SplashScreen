# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Splashp1yVdIhW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(583, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 10)
        self.splashframe = QFrame(self.centralwidget)
        self.splashframe.setObjectName(u"splashframe")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(11)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.splashframe.setFont(font)
        self.splashframe.setStyleSheet(u"QFrame{\n"
"	\n"
"	color: rgb(102, 108, 149);\n"
"	background-color: rgb(43, 44, 116);\n"
"	border-radius:12px;\n"
"}")
        self.splashframe.setFrameShape(QFrame.StyledPanel)
        self.splashframe.setFrameShadow(QFrame.Raised)
        self.labelAppname = QLabel(self.splashframe)
        self.labelAppname.setObjectName(u"labelAppname")
        self.labelAppname.setGeometry(QRect(10, 100, 591, 71))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semilight")
        font1.setPointSize(38)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.labelAppname.setFont(font1)
        self.labelAppname.setStyleSheet(u"QLabel{\n"
"color: rgb(255, 176, 193);\n"
"}")
        self.labelAppname.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.splashframe)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(180, 160, 261, 21))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Emoji")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(True)
        font2.setUnderline(False)
        font2.setWeight(50)
        font2.setStrikeOut(False)
        self.label_description.setFont(font2)
        self.label_description.setStyleSheet(u"QLabel#label_description{\n"
"	\n"
"	color: #fff;\n"
"}")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.splashframe)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 270, 481, 23))
        font3 = QFont()
        font3.setFamily(u"Verdana")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setWeight(75)
        self.progressBar.setFont(font3)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(200, 200, 200);\n"
"	color:rgb(56, 56, 230);\n"
"	border-style:none;\n"
"	border-radius:10px;\n"
"	text-align:center;\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.011, y1:0.517091, x2:0.960227, y2:0.488, stop:0.0909091 rgba(255, 181, 244, 255), stop:0.892045 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.progressBar.setValue(21)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.BottomToTop)
        self.label_loading = QLabel(self.splashframe)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(190, 300, 211, 21))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Emoji")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setWeight(50)
        font4.setStrikeOut(False)
        self.label_loading.setFont(font4)
        self.label_loading.setStyleSheet(u"QLabel#label_loading{\n"
"	\n"
"	color: #fff\n"
"}")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.splashframe)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(460, 340, 121, 21))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Emoji")
        font5.setPointSize(7)
        font5.setBold(False)
        font5.setItalic(True)
        font5.setUnderline(False)
        font5.setWeight(50)
        font5.setStrikeOut(False)
        self.label_credits.setFont(font5)
        self.label_credits.setStyleSheet(u"QLabel#label_credits{\n"
"	\n"
"	color: rgb(248, 248, 248);\n"
"}")
        self.label_credits.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.splashframe)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.labelAppname.setText(QCoreApplication.translate("SplashScreen", u"<strong>MacosLabs</strong> ", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"The software engine", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"Loading...", None))
        self.label_credits.setText(QCoreApplication.translate("SplashScreen", u"<strong>Designed By:</strong> Mark Owusu", None))
    # retranslateUi

