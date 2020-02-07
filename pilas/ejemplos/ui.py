# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Fri Aug 22 14:23:59 2014
#      by: PyQt5 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Ejemplos(object):
    def setupUi(self, Ejemplos):
        Ejemplos.setObjectName(_fromUtf8("Ejemplos"))
        Ejemplos.resize(787, 493)
        self.gridLayout = QtWidgets.QGridLayout(Ejemplos)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_2 = QtWidgets.QSplitter(Ejemplos)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.vbox_left = QtWidgets.QWidget(self.splitter_2)
        self.vbox_left.setObjectName(_fromUtf8("vbox_left"))
        self.vlayout_left = QtWidgets.QVBoxLayout(self.vbox_left)
        self.vlayout_left.setMargin(0)
        self.vlayout_left.setObjectName(_fromUtf8("vlayout_left"))
        self.arbol = QtWidgets.QTreeWidget(self.vbox_left)
        self.arbol.setObjectName(_fromUtf8("arbol"))
        self.arbol.headerItem().setText(0, _fromUtf8("1"))
        self.vlayout_left.addWidget(self.arbol)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.imagen = QtWidgets.QGraphicsView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagen.sizePolicy().hasHeightForWidth())
        self.imagen.setSizePolicy(sizePolicy)
        self.imagen.setMinimumSize(QtCore.QSize(400, 300))
        self.imagen.setAutoFillBackground(True)
        self.imagen.setRenderHints(QtWidgets.QPainter.SmoothPixmapTransform)
        self.imagen.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.imagen.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.imagen.setViewportUpdateMode(QtWidgets.QGraphicsView.SmartViewportUpdate)
        self.imagen.setObjectName(_fromUtf8("imagen"))
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.progreso = QtWidgets.QFrame(self.layoutWidget)
        self.progreso.setMinimumSize(QtCore.QSize(0, 22))
        self.progreso.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.progreso.setFrameShadow(QtWidgets.QFrame.Plain)
        self.progreso.setLineWidth(0)
        self.progreso.setObjectName(_fromUtf8("progreso"))
        self.label = QtWidgets.QLabel(self.progreso)
        self.label.setGeometry(QtCore.QRect(6, 0, 170, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.progreso)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ejecutar = QtWidgets.QPushButton(self.layoutWidget)
        self.ejecutar.setObjectName(_fromUtf8("ejecutar"))
        self.horizontalLayout.addWidget(self.ejecutar)
        self.fuente = QtWidgets.QPushButton(self.layoutWidget)
        self.fuente.setObjectName(_fromUtf8("fuente"))
        self.horizontalLayout.addWidget(self.fuente)
        self.guardar = QtWidgets.QPushButton(self.layoutWidget)
        self.guardar.setObjectName(_fromUtf8("guardar"))
        self.horizontalLayout.addWidget(self.guardar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.codigo = QtWidgets.QTextEdit(self.layoutWidget)
        self.codigo.setReadOnly(True)
        self.codigo.setObjectName(_fromUtf8("codigo"))
        self.verticalLayout.addWidget(self.codigo)
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.retranslateUi(Ejemplos)
        QtCore.QMetaObject.connectSlotsByName(Ejemplos)

    def retranslateUi(self, Ejemplos):
        Ejemplos.setWindowTitle(QtWidgets.QApplication.translate("Ejemplos", "Explorador de ejemplos", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label.setText(QtWidgets.QApplication.translate("Ejemplos", "Aguarde por favor ...", None, QtWidgets.QApplication.UnicodeUTF8))
        self.ejecutar.setText(QtWidgets.QApplication.translate("Ejemplos", "Ejecutar", None, QtWidgets.QApplication.UnicodeUTF8))
        self.fuente.setText(QtWidgets.QApplication.translate("Ejemplos", "Cambiar tipografia", None, QtWidgets.QApplication.UnicodeUTF8))
        self.guardar.setText(QtWidgets.QApplication.translate("Ejemplos", "Guardar Codigo", None, QtWidgets.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ejemplos = QtWidgets.QDialog()
    ui = Ui_Ejemplos()
    ui.setupUi(Ejemplos)
    Ejemplos.show()
    sys.exit(app.exec_())

