# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pilas/data/interprete.ui'
#
# Created: Fri Feb 21 18:52:30 2014
#      by: PyQt5 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_InterpreteWindow(object):
    def setupUi(self, InterpreteWindow):
        InterpreteWindow.setObjectName(_fromUtf8("InterpreteWindow"))
        InterpreteWindow.resize(719, 576)
        InterpreteWindow.setMinimumSize(QtCore.QSize(660, 530))
        self.centralwidget = QtWidgets.QWidget(InterpreteWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_vertical = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_vertical.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_vertical.setObjectName(_fromUtf8("splitter_vertical"))
        self.navegador = QtWebKit.QWebView(self.splitter_vertical)
        self.navegador.setMinimumSize(QtCore.QSize(250, 0))
        self.navegador.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.navegador.setObjectName(_fromUtf8("navegador"))
        self.splitter = QtWidgets.QSplitter(self.splitter_vertical)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.canvas = QtWidgets.QStackedWidget(self.layoutWidget)
        self.canvas.setMinimumSize(QtCore.QSize(320, 240))
        self.canvas.setObjectName(_fromUtf8("canvas"))
        self.page = QtWidgets.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.canvas.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.canvas.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.canvas)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.manual_button = QtWidgets.QPushButton(self.layoutWidget)
        self.manual_button.setMaximumSize(QtCore.QSize(20, 20))
        self.manual_button.setCursor(QtWidgets.QCursor(QtCore.Qt.PointingHandCursor))
        self.manual_button.setCheckable(True)
        self.manual_button.setFlat(True)
        self.manual_button.setObjectName(_fromUtf8("manual_button"))
        self.horizontalLayout_2.addWidget(self.manual_button)
        self.interprete_button = QtWidgets.QPushButton(self.layoutWidget)
        self.interprete_button.setMaximumSize(QtCore.QSize(20, 20))
        self.interprete_button.setCursor(QtWidgets.QCursor(QtCore.Qt.PointingHandCursor))
        self.interprete_button.setCheckable(True)
        self.interprete_button.setChecked(True)
        self.interprete_button.setFlat(True)
        self.interprete_button.setObjectName(_fromUtf8("interprete_button"))
        self.horizontalLayout_2.addWidget(self.interprete_button)
        self.guardar_button = QtWidgets.QPushButton(self.layoutWidget)
        self.guardar_button.setMaximumSize(QtCore.QSize(20, 20))
        self.guardar_button.setCursor(QtWidgets.QCursor(QtCore.Qt.PointingHandCursor))
        self.guardar_button.setFlat(True)
        self.guardar_button.setObjectName(_fromUtf8("guardar_button"))
        self.horizontalLayout_2.addWidget(self.guardar_button)
        spacerItem = QtWidgets.QSpacerItem(37, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_6.setCursor(QtWidgets.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_5.setCursor(QtWidgets.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_4.setCursor(QtWidgets.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_3.setCursor(QtWidgets.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_2.setCursor(QtWidgets.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton.setCursor(QtWidgets.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.console = QtWidgets.QStackedWidget(self.layoutWidget1)
        self.console.setObjectName(_fromUtf8("console"))
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.console.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.console.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.console)
        self.gridLayout.addWidget(self.splitter_vertical, 0, 0, 1, 1)
        InterpreteWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(InterpreteWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        InterpreteWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(InterpreteWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        InterpreteWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(InterpreteWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))

        self.retranslateUi(InterpreteWindow)
        self.console.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(InterpreteWindow)

    def retranslateUi(self, InterpreteWindow):
        InterpreteWindow.setWindowTitle(_translate("InterpreteWindow", "pilas-engine", None))
        self.manual_button.setToolTip(_translate("InterpreteWindow", "Mostrar el manual de pilas", None))
        self.manual_button.setText(_translate("InterpreteWindow", "M", None))
        self.interprete_button.setToolTip(_translate("InterpreteWindow", "Mostrar el intérprete", None))
        self.interprete_button.setText(_translate("InterpreteWindow", "I", None))
        self.guardar_button.setToolTip(_translate("InterpreteWindow", "Guardar el contenido del intérprete", None))
        self.guardar_button.setText(_translate("InterpreteWindow", "G", None))
        self.pushButton_6.setToolTip(_translate("InterpreteWindow", "Mostrar información del sistema", None))
        self.pushButton_6.setText(_translate("InterpreteWindow", "F7", None))
        self.pushButton_5.setToolTip(_translate("InterpreteWindow", "Mostrar puntos de control", None))
        self.pushButton_5.setText(_translate("InterpreteWindow", "F8", None))
        self.pushButton_4.setToolTip(_translate("InterpreteWindow", "Mostrar radios de colisión", None))
        self.pushButton_4.setText(_translate("InterpreteWindow", "F9", None))
        self.pushButton_3.setToolTip(_translate("InterpreteWindow", "Mostrar areas", None))
        self.pushButton_3.setText(_translate("InterpreteWindow", "F10", None))
        self.pushButton_2.setToolTip(_translate("InterpreteWindow", "Mostrar figuras físicas", None))
        self.pushButton_2.setText(_translate("InterpreteWindow", "F11", None))
        self.pushButton.setToolTip(_translate("InterpreteWindow", "Mostrar posiciones", None))
        self.pushButton.setText(_translate("InterpreteWindow", "F12", None))
        self.actionSalir.setText(_translate("InterpreteWindow", "Salir", None))

from PyQt5 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InterpreteWindow = QtWidgets.QMainWindow()
    ui = Ui_InterpreteWindow()
    ui.setupUi(InterpreteWindow)
    InterpreteWindow.show()
    sys.exit(app.exec_())

