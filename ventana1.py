import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton
from PyQt5 import QtGui

class Ventana1(QMainWindow):

    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        self.setWindowTitle("Formulario de registro")

        self.setWindowIcon(QtGui.QIcon("imagen/pngwing.com (1).png"))

        self.ancho = 900
        self.alto = 600

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)

        self.imagenFondo = QPixmap("imagen/sherry-christian-8Myh76_3M2U-unsplash.jpg")

        self.fondo.setPixmap(self.imagenFondo)

        self.fondo.setScaledContents(True)

        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()

        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # Layout izquierdo

        # Creamos el layout izquierdo
        self.ladoizquierdo = QFormLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("Información del cliente")

        self.letrero1.setFont(QFont("Andale Mono", 20))

        self.letrero1.setStyleSheet("color: #000080")

        self.ladoizquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()

        self.letrero2.setFixedWidth(340)

        self.letrero2.setText("Por favor ingrese la información de cliente "
                              "\nen el formulario de abajo. los campos marcados"
                              "\ncon asterisco son obligatorios.")

        self.letrero2.setFont(QFont("Andale Mono", 10))

        self.letrero2.setStyleSheet("color: #000080; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        self.ladoizquierdo.addRow(self.letrero2)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(220)

        self.ladoizquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(220)

        self.ladoizquierdo.addRow("Usuario*", self.usuario)

        self.password = QLineEdit()
        self.password.setFixedWidth(220)
        self.password.setEchoMode(QLineEdit.Password)

        self.ladoizquierdo.addRow("Password*", self.password)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(220)
        self.password2.setEchoMode(QLineEdit.Password)

        self.ladoizquierdo.addRow("Password*", self.password2)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(220)

        self.ladoizquierdo.addRow("Documento*", self.documento)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(220)

        self.ladoizquierdo.addRow("Correo*", self.correo)

        self.botonRegistrar = QPushButton("Registrar")

        self.botonRegistrar.setFixedWidth(90)

        self.botonRegistrar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonLimpiar = QPushButton("Limpiar")

        self.botonLimpiar.setFixedWidth(90)

        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoizquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        self.horizontal.addLayout(self.ladoizquierdo)



        # ------------- SIEMPRE PONER DE ULTIMO ---------------------
        self.fondo.setLayout(self.horizontal)




    # Metodo del botonLimpiar:
    def accion_botonLimpiar(self):
        pass

    # Metodo del botonRegistrar
    def accion_botonRegistrar(self):
        pass






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec_())