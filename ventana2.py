import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QVBoxLayout, QApplication
from PyQt5 import QtGui


class Ventana2(QMainWindow):

    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)

        self.ventanaAnterior = anterior
        self.setWindowTitle("Usuario registrado")
        self.setWindowIcon(QtGui.QIcon("imagen/sherry-christian-8Myh76_3M2U-unsplash.jpg"))
        self.ancho = 1000
        self.alto = 700
        self.resize(self.ancho, self.alto)
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)
        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap("imagen/daniel.png")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        self.setCentralWidget(self.fondo)
        self.vertical = QVBoxLayout()






        # OJO PONER AL FINAL
        self.fondo.setLayout(self.vertical)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana2 = Ventana2()
    ventana2.show()
    sys.exit(app.exec_())