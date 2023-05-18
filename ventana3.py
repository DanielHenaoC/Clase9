from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton
from PyQt5 import QtGui

from cliente import Cliente


class Ventana3(QMainWindow):
    def __init__(self, anterior):
        super(Ventana3, self).__init__(anterior)

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
        self.vertical = QVBoxLayout()

        self.letre1 = QLabel()
        self.letre1.setText("Usuarios registrado")
        self.letre1.setFont(QFont("Andale mono", 20))
        self.letre1.setStyleSheet("color: #FFFFFF;")
        self.vertical.addWidget(self.letre1)

        self.vertical.addStretch()

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(11)

        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)
        self.tabla.setColumnWidth(7, 150)
        self.tabla.setColumnWidth(8, 150)
        self.tabla.setColumnWidth(9, 150)
        self.tabla.setColumnWidth(10, 150)

        self.tabla.setHorizontalHeaderLabels(['Nombre','Usuario','Password','Documento','Correo','Pregunta1','Respuesta1','Pregunta2','Respuesta2','Pregunta3','Respuesta3'])

        self.tabla.setRowCount(self.numeroUsuario)

        for u in self.usuario:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombreCompleto))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.password))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.pregunta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.pregunta2))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.pregunta3))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
            self.contador += 1

        self.scrollArea.setWidget(self.tabla)
        self.vertical.addWidget(self.scrollArea)

        self.vertical.addStretch()

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(90)
        self.botonVolver.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px; margin-top: 10px;")
        self.botonVolver.clicked.connect(self.metodo_volver)
        self.vertical.addWidget(self.botonVolver)


        # OJO PONER DE ULTIMO
        self.fondo.setLayout(self.vertical)

    def metodo_volver(self):
            self.hide()
            self.ventanaAnterior.show()
















