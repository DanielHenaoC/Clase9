from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
import sys
from cliente import Cliente
from ventana2 import  Ventana2

class Ventana1(QMainWindow):

    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        self.setWindowTitle("Formulario de registro")

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


        # Layout derecho

        self.ladoDerecho = QFormLayout()

        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        self.letrero3 = QLabel()

        self.letrero3.setText("Recuperar contraseña")

        self.letrero3.setFont(QFont("Andale Mono", 20))

        self.letrero3.setStyleSheet("color: #000080;")

        self.ladoDerecho.addRow(self.letrero3)

        self.letrero4 = QLabel()

        self.letrero4.setFixedWidth(400)

        self.letrero4.setText("Por favor ingrese la información para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        self.letrero4.setFont(QFont("Andela Mono", 10))

        self.letrero4.setStyleSheet("color: #000080; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        self.ladoDerecho.addRow(self.letrero4)

        # ---1

        self.labelPregunta1 = QLabel("Pregunta de verificación 1*")

        self.ladoDerecho.addRow(self.labelPregunta1)

        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta1)

        self.labelRespuesta1 = QLabel("Respuesta de verificación 1*")

        self.ladoDerecho.addRow(self.labelRespuesta1)

        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta1)

        # ---2

        self.labelPregunta2 = QLabel("Pregunta de verificación 2*")

        self.ladoDerecho.addRow(self.labelPregunta2)

        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta2)

        self.labelRespuesta2 = QLabel("Respuesta de verificación 2*")

        self.ladoDerecho.addRow(self.labelRespuesta2)

        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta2)

        # ---3

        self.labelPregunta3 = QLabel("Pregunta de verificación 3*")

        self.ladoDerecho.addRow(self.labelPregunta3)

        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta3)

        self.labelRespuesta3 = QLabel("Respuesta de verificación 3*")

        self.ladoDerecho.addRow(self.labelRespuesta3)

        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta3)

        self.botonbuscar = QPushButton("Buscar")
        self.botonbuscar.setFixedWidth(90)
        self.botonbuscar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonbuscar.clicked.connect(self.accion_botonBuscar)

        self.botonRecuperar = QPushButton("Recuperar")
        self.botonRecuperar.setFixedWidth(90)
        self.botonRecuperar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonRecuperar.clicked.connect(self.accion_botonRecuperar)
        self.ladoDerecho.addRow(self.botonbuscar, self.botonRecuperar)

        self.botonContinuar = QPushButton("Continuar")
        self.botonContinuar.setFixedWidth(90)
        self.botonContinuar.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px; margin-top: 10px;")
        self.botonContinuar.clicked.connect(self.accion_botonContinuar)
        self.ladoDerecho.addRow(self.botonContinuar)


        self.horizontal.addLayout(self.ladoDerecho)



        # ------------- SIEMPRE PONER DE ULTIMO ---------------------
        self.fondo.setLayout(self.horizontal)




        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        self.ventanaDialogo.resize(300, 150)

        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.vertical = QVBoxLayout()

        self.mensaje = QLabel("")

        self.mensaje.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")

        self.vertical.addWidget(self.mensaje)

        self.vertical.addWidget(self.opciones)

        self.ventanaDialogo.setLayout(self.vertical)

    # Metodo del botonLimpiar:
    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    # Metodo del botonRegistrar
    def accion_botonRegistrar(self):

        self.datosCorrectos = True

        # Validación de la contraseñas
        if (
                self.password.text() != self.password2.text()
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Los passwords no son iguales")

            self.ventanaDialogo.exec_()

            # Validación de que hayan ingresado algo en los campos
        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debes ingresar todos los campos")

            self.ventanaDialogo.exec_()


        if self.datosCorrectos:
            # Traer el texto de los QLineEdit() y los agrega concatenandolos.
            # Para escribirlos en el archivo en forma binario utf-8.
            self.file = open('datos/clientes.txt', 'ab')
            self.file.write(bytes(
                self.nombreCompleto.text() + ";"
                + self.usuario.text() + ";"
                + self.password.text() + ";"
                + self.documento.text() + ";"
                + self.correo.text() + ";"
                + self.pregunta1.text() + ";"
                + self.respuesta1.text() + ";"
                + self.pregunta2.text() + ";"
                + self.respuesta2.text() + ";"
                + self.pregunta3.text() + ";"
                + self.respuesta3.text() + '\n'
                , encoding='UTF-8'))

            # Cerramos el archivo.
            self.file.close()

            # Abrimos el modo lectra
            self.file = open('datos/clientes.txt', 'rb')
            # Recorrer el archivo linea por linea.
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '': # Para cuando encuentre una linea vacida
                    break
            self.file.close()

    # Metodo boton buscar

    def accion_botonBuscar(self):

        self.datosCorrectos = True

        self.ventanaDialogo.setWindowTitle("Buscar Pregunta de validación")
        if (self.documento.text() == ''):

            self.datosCorrectos = False

            self.mensaje.setText("Si va a buscar la pregunta para recuperar la contraseña."
                                 "\ndebe primero ingresar el documento.")

            self.ventanaDialogo.exec_()

        if (not self.documento.text().isnumeric()):
            self.datosCorrectos = False

            self.mensaje.setText("El documento debe ser numerico\nno ingrese letras ni caracteres especiales")

            self.ventanaDialogo.exec_()

            self.documento.setText('') # Limpiar el campo del documento

        # Proceso para mostrar los archivos planos
        if (self.datosCorrectos):

            self.file = open('datos/clientes.txt', 'rb')

            usuario = [] # Para guardar los usuarios

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                lista = linea.split(";")

                if linea == '':
                    break

                # Creamos un objeto tipo cliente
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

                # Metemos el objeto en la lista usuario
                usuario.append(u)

            # Cerramos el archivo
            self.file.close()

            # En este punto ya tenemos la lista usuarios con todos los usuarios:

            existeDocumento = False

            for u in usuario:

                if u.documento == self.documento.text():
                    # Mostramos las preguntas en el formulario
                    self.pregunta1.setText(u.pregunta1)
                    self.pregunta2.setText(u.pregunta2)
                    self.pregunta3.setText(u.pregunta3)

                    existeDocumento = True

                    break

            if (not existeDocumento):
                self.mensaje.setText("No existe un usuario con este documento:\n" + self.documento.text())

                self.ventanaDialogo.exec_()

    def accion_botonRecuperar(self):

        self.datosCorrectos = True

        self.ventanaDialogo.setWindowTitle("Recuperar contraseña")

        if (self.pregunta1.text() == '' or self.pregunta2.text() == '' or self.pregunta3.text() == ''):

            self.datosCorrectos = False

            self.mensaje.setText("Para recuperar la contraseña debe\nbuscar las preguntas de verificación."
                                 "\nPrimero ingrese su documento y luego\npresione el boton 'buscar'")

            self.ventanaDialogo.exec_()

        if (self.pregunta1.text() != '' and self.respuesta1.text() == '' and self.pregunta2.text() != '' and
            self.respuesta2.text() == '' and self.pregunta3.text() != '' and self.respuesta3.text() == ''):

            self.datosCorrectos = False

            self.mensaje.setText("Para recuperar la contraseña bede\ningresar la respuesta de cada pregunta.")

            self.ventanaDialogo.exec_()

        if (self.datosCorrectos):
            self.file = open('datos/clientes.txt', 'rb')

            usuario = []

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
                usuario.append(u)

            self.file.close()

            existeDocumento = False

            resp1 = ''
            resp2 = ''
            resp3 = ''
            passw = ''

            for u in usuario:

                if u.documento == self.documento.text():
                    resp1 = u.respuesta1
                    resp2 = u.respuesta2
                    resp3 = u.respuesta3
                    passw = u.password
                    break

            if (
                    self.respuesta1.text().lower().strip() == resp1.lower().strip() and
                    self.respuesta2.text().lower().strip() == resp2.lower().strip() and
                    self.respuesta1.text().lower().strip() == resp1.lower().strip()
            ):
                self.accion_botonLimpiar()

                self.mensaje.setText("Contraseña: " + passw)

                self.ventanaDialogo.exec_()

            else:
                self.mensaje.setText("Las respuestas son incorrecta para estas"
                                     "\npreguntas de recuperación de contraseña")

                self.ventanaDialogo.exec_()

    def accion_botonContinuar(self):
        self.hide()
        self.ventana2 = Ventana2(self)
        self.ventana2.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec_())