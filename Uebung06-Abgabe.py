from PyQt5.QtWidgets import *
from PyQt5.uic import *
import urllib.parse
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("showmap.ui",self)

        self.KarteButton.clicked.connect(self.Karte)

    def Karte(self):
        addresse = f"{self.breite.text()},{self.laenge.text()}"
        query = urllib.parse.quote(addresse)
        link = f"https://www.google.ch/maps/place/{addresse}"
        QDesktopServices.openUrl(QUrl(link))

app=QApplication([])

window=Fenster()
window.show()

app.exec()