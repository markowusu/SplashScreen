import platform
import sys
from PySide2.QtWidgets import QApplication,QMainWindow
from PySide2 import QtCore,QtGui
from ui_Splashp1 import Ui_SplashScreen
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import *

counter =0  # THIS IS TO SET AN INITVALUE FOR THE COUNTER

class SplashScreen(QMainWindow):
      def __init__(self):
            super().__init__()
            self.ui = Ui_SplashScreen()
            self.ui.setupUi(self)

            #  REMOVING THE TITLE BAR
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


            #  TMER -> SET
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.progress)
            #  SETTING THE TIME IN MILLISECONDS
            self.timer.start(35)
            

            #  CHANGING THE DESCRIPTION LABEL 
            QtCore.QTimer.singleShot(1500,lambda: self.ui.label_description.setText("Using MacosLabs Engines"))
            QtCore.QTimer.singleShot(4000,lambda :self.ui.label_loading.setText("Loading...User Interface"))
            QtCore.QTimer.singleShot(3600,lambda: self.ui.label_description.setText("We Build The Future"))
            QtCore.QTimer.singleShot(5300,lambda: self.ui.label_description.setText("Ready?"))
            


            # ==================================
            # SHOW -> MAIN WINDOW
            self.show()

            # ==================================

# ===============================================
# APPLICATION FUNCTIONS -> RECIEVERS
      def progress(self):
            global counter

            self.ui.progressBar.setValue(counter)

            #  LOGIC FOR THE SPLASHSCREEN

            if counter > 100:

                  self.timer.stop()


                  self.close()

            counter +=1
# ================================================

if __name__ == '__main__':
      myapp = QApplication([])
      window = SplashScreen()
      window.show()
      sys.exit(myapp.exec_())


