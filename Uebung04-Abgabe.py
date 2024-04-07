#Aufgabe 1

import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI-Programmierung")
        self.show()

        layout=QVBoxLayout()

        button=QPushButton("Save")

        label1=QLabel("Vorname:")
        label2=QLabel("Name")
        label3=QLabel("Adresse:")
        label4=QLabel("Postleitzahl:")
        label5=QLabel("Ort:")
        geburtstag=QSpinBox()
        land=QComboBox()
        land.addItems(["Schweiz", "Deutschland", "Österreich"])

        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(geburtstag)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)
        layout.addWidget(land)
        layout.addWidget(button)

        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)

        menu=self.menuBar()
        filemenu=menu.addMenu("File")

        save=QAction("Save", self)
        quit=QAction("Quit", self)

        filemenu.addAction(save)
        self.triggered.connect(self.menu_save)
        filemenu.addAction(quit)
        quit.triggered.connect(self.menu_quit)

        button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print("Daten gespeichert")

    def menu_save(self):
        print("Daten gespiechert")

    def menu_quit(self):
        self.close()


def main():
    app = QApplication(sys.argv) 
    mainwindow = MainWindow()      
    mainwindow.raise_()           
    app.exec_()                 

if __name__ == '__main__':
    main()