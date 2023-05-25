from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFormLayout, QLineEdit, QHBoxLayout, QPushButton, \
    QDialog, QDialogButtonBox, QVBoxLayout

from cliente import Cliente


class Ventana4(QMainWindow):
    def __init__(self, anterior, cedula):
        super(Ventana4, self).__init__(None)

        self.ventanaAnterior = anterior
        self.cedulaUsuario = cedula

        self.setWindowTitle("Editar usuario")
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
        self.fondo.setStyleSheet("background-color:#FFDEAD")
        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()

        # _______LAYOUT IZQUIENDO______________

        self.ladoizquierdo = QFormLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Editar Cliente")
        self.letrero1.setFont(QFont("Andale Mono", 20))
        self.letrero1.setStyleSheet("color: #FFFFFF;background-color: #FF8C00")
        self.ladoizquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()
        self.letrero2.setFixedWidth(340)
        self.letrero2.setText("Por favor ingrese la información de cliente "
                              "\nen el formulario de abajo. los campos marcados"
                              "\ncon asterisco son obligatorios.")

        self.letrero2.setFont(QFont("Andale Mono", 10))
        self.letrero2.setStyleSheet("color: #FFFFFF;"
                                    "background-color: #FF8C00;"
                                    "margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #FFFFFF;"
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

        # Boton Editar
        self.botonEditar = QPushButton("Editar")
        self.botonEditar.setFixedWidth(90)
        self.botonEditar.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px; margin-top: 20px;")
        self.botonEditar.clicked.connect(self.accion_botonEditar)

        # Boton limpiar
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)
        self.botonLimpiar.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px; margin-top: 20px;")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoizquierdo.addRow(self.botonEditar, self.botonLimpiar)

        # Boton Eliminar
        self.botonEliminar = QPushButton("Eliminar")
        self.botonEliminar.setFixedWidth(90)
        self.botonEliminar.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px; margin-top: 20px;")
        self.botonEliminar.clicked.connect(self.accion_botonEliminar)

        self.ladoizquierdo.addRow(self.botonEliminar)

        # Boton volver
        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(90)
        self.botonVolver.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px; margin-top: 20px;")
        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        self.ladoizquierdo.addRow(self.botonVolver)

        # Ultimo
        self.horizontal.addLayout(self.ladoizquierdo)

        # Lado derecho
        self.ladoDerecho = QFormLayout()
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        self.letrero3 = QLabel()
        self.letrero3.setText("Editar recuperar contraseña")
        self.letrero3.setFont(QFont("Andale Mono", 20))
        self.letrero3.setStyleSheet("color: #FFFFFF; background-color: #FF8C00;")
        self.ladoDerecho.addRow(self.letrero3)

        self.letrero4 = QLabel()
        self.letrero4.setFixedWidth(400)
        self.letrero4.setText("Por favor ingrese la información para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco son obligatorios.")
        self.letrero4.setFont(QFont("Andela Mono", 10))
        self.letrero4.setStyleSheet("color: #000080;"
                                    "background-color: ·FF8C00"
                                    "margin-bottom: 40px;"
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

        self.horizontal.addLayout(self.ladoDerecho)

        # Mas ultimo
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

        self.cargar_datos()

    def accion_botonEditar(self):
        self.datosCorrecto = True
        self.ventanaDialogo.setWindowTitle("Formulario de edicion")

        if (self.password.text() != self.password2.text()):
            self.datosCorrecto = False
            self.mensaje.setText("Los password no son iguales")
            self.ventanaDialogo.exec_()

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
            self.datosCorrecto = False
            self.mensaje.setText("Debes seleccionar un usuario con documento valido!")
            self.ventanaDialogo.exec_()


        if self.datosCorrecto:

            self.file = open('datos/clientes.txt', 'rb')
            usuario = []  # Para guardar los usuarios

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

            existeDocumento = False
            for u in usuario:
                if int(u.documento) == self.cedulaUsuario:
                    u.usuario = self.usuario.text()
                    u.password = self.password.text()
                    u.correo = self.correo.text()
                    u.pregunta1 = self.pregunta1.text()
                    u.respuesta1 = self.respuesta1.text()
                    u.pregunta2 = self.pregunta2.text()
                    u.respuesta2 = self.respuesta2.text()
                    u.pregunta3 = self.pregunta3.text()
                    u.respuesta3 = self.respuesta3.text()

                    existeDocumento = True
                    break

            if (
                    not existeDocumento
            ):
                self.mensaje.setText("No existe un usuario con este documento: \n" + str(self.cedulaUsuario))
                self.ventanaDialogo.exec_()

            self.file = open('datos/clientes.txt', 'wb')

            for u in usuario:
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
                    + self.respuesta3.text(), encoding='UTF-8'))
            self.file.close()

            if (existeDocumento):
                self.mensaje.setText("Usuario actualizado corrrectamente!")
                self.ventanaDialogo.exec_()
                self.accion_botonLimpiar()
                self.metodo_botonVolver()

            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

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

    def accion_botonEliminar(self):
        self.datosCorrecto = True
        self.eliminar = False

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
            self.datosCorrecto = False
            self.mensaje.setText("Debes seleccionar un usuario con documento valido!")
            self.ventanaDialogo.exec_()
            self.metodo_botonVolver()

        if self.datosCorrecto:

            self.ventanaDialogoEliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
            self.ventanaDialogoEliminar.resize(300, 150)
            self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)
            self.verticalEliminar = QVBoxLayout()
            self.mensajeEliminar = QLabel("¿Estas seguro que deseas eliminar este registro de usuario?")
            self.mensajeEliminar.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")
            self.verticalEliminar.addWidget(self.mensajeEliminar)

            self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

            self.opcionesBox.accepted.connect(self.ok_opcion)
            self.opcionesBox.rejected.connect(self.cancel_opcion)
            self.verticalEliminar.addWidget(self.opcionesBox)
            self.ventanaDialogoEliminar.setLayout(self.verticalEliminar)
            self.ventanaDialogoEliminar.exec_()

        if self.eliminar:
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

            for u in usuario:
                if int(u.documento) == self.cedulaUsuario:
                    usuario.remove(u)
                    existeDocumento = True
                    break

        self.file = open('datos/clientes.txt', 'wb')

        for u in usuario:
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
                + self.respuesta3.text(), encoding='UTF-8'))

        # Cerramos el archivo.
        self.file.close()

        if (existeDocumento):
            self.mensaje.setText("Usuario eliminado exitosamente!")
            self.ventanaDialogo.exec_()
            self.accion_botonLimpiar()
            self.metodo_botonVolver()

    def ok_opcion(self):
        self.ventanaDialogoEliminar.close()
        self.eliminar = True

    def cancel_opcion(self):
        self.ventanaDialogoEliminar.close()

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def cargar_datos(self):

        self.file = open('datos/clientes.txt', 'rb')
        usuario = []

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

        existeDocumento = False

        for u in usuario:
            if int(u.documento) == self.cedulaUsuario:
                # Mostramos los datos en el formulario
                self.nombreCompleto.setText(u.nombreCompleto)
                # Hacemos que el nombre no se pueda editar
                self.nombreCompleto.setReadOnly(True)
                self.usuario.setText(u.usuario)
                self.password.setText(u.password)
                self.password2.setText(u.password)
                self.documento.setText(u.documento)
                # Hacemos que el documento no se pueda editar
                self.documento.setReadOnly(True)
                self.correo.setText(u.correo)
                self.pregunta1.setText(u.pregunta1)
                self.respuesta1.setText(u.respuesta1)
                self.pregunta2.setText(u.pregunta2)
                self.respuesta2.setText(u.respuesta2)
                self.pregunta3.setText(u.pregunta3)
                self.respuesta3.setText(u.respuesta3)

                existeDocumento = True

                break

        if (not existeDocumento):
            self.mensaje.setText("No existe un usuario con este documento: \n" + str(self.cedulaUsuario))
            self.ventanaDialogo.exec_()
            self.metodo_botonVolver()