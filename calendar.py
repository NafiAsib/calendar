import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QDialog, QVBoxLayout, QCalendarWidget, QLayout, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "Calendar"
        self.top = 100
        self.left = 100
        self.width = 400
        self. height = 400
        self.InitWindow()
        self.calendar()
        self.show()
    
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon("images/calendar.png"))
    
    def calendar(self):
        vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        
        self.button = QPushButton(self)
        self.button.setIcon(QtGui.QIcon("images/about.png"))
        self.button.setToolTip("<h2><code>About developer</code></h2>")
        self.button.clicked.connect(self.clickMethod)

        self.exit = QPushButton(self)
        self.exit.setIcon(QtGui.QIcon("images/exit.png"))
        self.exit.setToolTip("Exit Calendar")
        self.exit.clicked.connect(self.b_exit)
        
        vbox.addWidget(self.calendar)
        vbox.addWidget(self.button)
        vbox.addWidget(self.exit)
        self.setLayout(vbox)

    def clickMethod(self):
        QMessageBox.about(self,"About","Developed by K.M. Nafi Asib with Python3 and PyQt5<br>Academic project for <code>CSE-242</code>")

    def b_exit(self):
        sys.exit()

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())