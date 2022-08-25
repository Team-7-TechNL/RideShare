from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from geopy.geocoders import Nominatim
import sys, math


from main import Mapmain
Mapmain((0,0))



class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

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
        self.show()

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
    window = MainWindow()
    app.exec_()
