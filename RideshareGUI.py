from PyQt5.QtCore import *
from PyQt5 import QtWidgets

from PyQt5.QtWebEngineWidgets import *
from geopy.geocoders import Nominatim
import sys, math


from main import Mapmain
Mapmain((0,0))

import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.initUI()

    def button_clicked(self):
        self.label.setText("Please select a location")
        self.label.setStyleSheet("border: 1px solid black")
        self.label.adjustSize()

    def initUI(self):
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("file:///aee.html"))

        self.setCentralWidget(self.browser)

        self.frame1 = QFrame(self)
        self.frame1.setStyleSheet("background-color: lightgray")
        self.frame1.setFrameShape(QFrame.Box | QFrame.Raised)
        self.frame1.setLineWidth(1)
        self.frame1.resize(size.width() + 10, 200)
        self.frame1.move(math.floor(0), math.floor(size.height() - 261))

        self.textbox = QLineEdit(self)
        self.textbox.move(50, size.height() - 200)
        self.textbox.resize(280, 40)

        self.button = QPushButton('Locate', self)
        self.button.setToolTip('sets your location')
        self.button.move(50, 940)
        self.button.clicked.connect(self.on_click)

        info = "Please select your role"

        self.label = QLabel(info, self)
        self.label.setStyleSheet("border: 1px solid black")
        self.label.setGeometry(875, 900, 120, 20)


        self.button1 = QtWidgets.QPushButton("Driver", self)
        self.button1.setStyleSheet("background-color: white")
        self.button1.move(1350, 940)
        self.button1.setGeometry(850, 940, 55, 55)
        self.button1.clicked.connect(self.button_clicked)

        self.button2 = QPushButton("Passenger", self)
        self.button2.setStyleSheet("background-color: white")
        self.button2.move(1450, 940)
        self.button2.setGeometry(950, 940, 55, 55)

    def update(self):
        self.label.adjustSize()


    def on_click(self):
        from Distchecker import distchecker
        geolocator = Nominatim(user_agent="RideShareApp")
        location = geolocator.geocode(self.textbox.text())
        cords = location.latitude, location.longitude
        Mapmain(cords)
        distchecker(cords)
        self.browser.reload()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    window = MyWindow()
    window.show()
    app.exec_()

