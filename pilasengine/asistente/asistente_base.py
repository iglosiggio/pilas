# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pilasengine/asistente/asistente.ui'
#
# Created by: PyQt5 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtGui

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

class Ui_AsistenteWindow(object):
    def setupUi(self, AsistenteWindow):
        AsistenteWindow.setObjectName(_fromUtf8("AsistenteWindow"))
        AsistenteWindow.resize(615, 480)
        AsistenteWindow.setMinimumSize(QtCore.QSize(615, 480))
        AsistenteWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../pilas/pilas/data/pilas.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AsistenteWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AsistenteWindow)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)
        AsistenteWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AsistenteWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        AsistenteWindow.setStatusBar(self.statusbar)
        self.salir_action = QtWidgets.QAction(AsistenteWindow)
        self.salir_action.setObjectName(_fromUtf8("salir_action"))

        self.retranslateUi(AsistenteWindow)
        QtCore.QMetaObject.connectSlotsByName(AsistenteWindow)

    def retranslateUi(self, AsistenteWindow):
        AsistenteWindow.setWindowTitle(_translate("AsistenteWindow", "pilas-engine", None))
        self.salir_action.setText(_translate("AsistenteWindow", "Salir", None))

from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AsistenteWindow = QtWidgets.QMainWindow()
    ui = Ui_AsistenteWindow()
    ui.setupUi(AsistenteWindow)
    AsistenteWindow.show()
    sys.exit(app.exec_())

