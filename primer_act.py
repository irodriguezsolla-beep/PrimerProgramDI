import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QWidget,QLabel,QLineEdit)

class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera aplicación QL")
        self.setMinimumSize(300,200)
        self.setMaximumSize(500,400)
        self.show()

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()