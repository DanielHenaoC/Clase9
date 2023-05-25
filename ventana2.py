import math
import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QVBoxLayout, QApplication, QScrollArea, \
    QWidget, QGridLayout, QButtonGroup, QPushButton
from PyQt5 import QtGui

from cliente import Cliente
from ventana3 import Ventana3
from ventana4 import Ventana4


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

        self.letrero1 = QLabel()
        self.letrero1.setText("Información del cliente")
        self.letrero1.setFont(QFont("Andale Mono", 20))
        self.letrero1.setStyleSheet("color: #000080")
        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        # Creamos un scroll
        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet("background-color: transparent;")
        self.scrollArea.setWidgetResizable(True)

        self.contenedor = QWidget()
        self.cuadricula = QGridLayout(self.contenedor)
        self.scrollArea.setWidget(self.contenedor)
        self.vertical.addWidget(self.scrollArea)

        self.file = open('datos/clientes.txt', 'rb')
        self.usuario = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")
            if linea == '':
                break

            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
            )

            self.usuario.append(u)
        self.file.close()

        self.numeroUsuario = len(self.usuario)
        self.contador = 0
        self.elementosPorColumna = 3
        self.filas = math.ceil(self.numeroUsuario/self.elementosPorColumna) + 1

        # El boton para todos los botones
        self.botones = QButtonGroup()
        self.botones.setExclusive(False)

        for fila in range(1, self.numeroUsuario):
            for columna in range(1, self.elementosPorColumna+1):
                if self.contador < self.numeroUsuario:
                    self.ventanaAuxiliar = QWidget()
                    self.ventanaAuxiliar.setFixedHeight(100)
                    self.ventanaAuxiliar.setFixedWidth(200)

                    self.verticalCuadricula = QVBoxLayout()
                    self.botonAccion = QPushButton(self.usuario[self.contador].documento)
                    self.botonAccion.setFixedWidth(150)
                    self.botonAccion.setStyleSheet("background-color: #008B45; color: black; padding: 10px;")
                    self.verticalCuadricula.addWidget(self.botonAccion)
                    self.botones.addButton(self.botonAccion, int(self.usuario[self.contador].documento))
                    self.verticalCuadricula.addStretch()
                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)
                    self.contador += 1

        self.botones.idClicked.connect(self.metodo_accionBotones)

        self.botoTabular = QPushButton("Forma Tabular")
        self.botoTabular.setFixedWidth(100)
        self.botoTabular.setStyleSheet("background-color: #008b45; color: #FFFFFF; padding: 10px; margin-top: 10px")
        self.botoTabular.clicked.connect(self.metodo_formulario)
        self.vertical.addWidget(self.botoTabular)


        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(90)
        self.botonVolver.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px; margin-top: 10px;")
        self.botonVolver.clicked.connect(self.metodo_volver)
        self.vertical.addWidget(self.botonVolver)


        # OJO PONER AL FINAL
        self.fondo.setLayout(self.vertical)

    def metodo_accionBotones(self,cedulaUsuario):
        self.hide()
        self.ventana = Ventana4(self, cedulaUsuario)
        self.ventana.show()

    def metodo_volver(self):
        self.hide()
        self.ventanaAnterior.show()

    def metodo_formulario(self):
        self.hide()
        self.ventana3 = Ventana3(self)
        self.ventana3.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana2 = Ventana2()
    ventana2.show()
    sys.exit(app.exec_())