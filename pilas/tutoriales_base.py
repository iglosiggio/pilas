# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pilas/data/tutoriales.ui'
#
# Created: Fri Feb 21 18:52:31 2014
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

class Ui_TutorialesWindow(object):
    def setupUi(self, TutorialesWindow):
        TutorialesWindow.setObjectName(_fromUtf8("TutorialesWindow"))
        TutorialesWindow.resize(844, 508)
        TutorialesWindow.setMinimumSize(QtCore.QSize(500, 400))
        self.centralwidget = QtWidgets.QWidget(TutorialesWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.webView.setStatusTip(_fromUtf8(""))
        self.webView.setAccessibleDescription(_fromUtf8(""))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)
        TutorialesWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TutorialesWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        TutorialesWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TutorialesWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        TutorialesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TutorialesWindow)
        QtCore.QMetaObject.connectSlotsByName(TutorialesWindow)

    def retranslateUi(self, TutorialesWindow):
        TutorialesWindow.setWindowTitle(_translate("TutorialesWindow", "Tutoriales de pilas-engine", None))

from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TutorialesWindow = QtWidgets.QMainWindow()
    ui = Ui_TutorialesWindow()
    ui.setupUi(TutorialesWindow)
    TutorialesWindow.show()
    sys.exit(app.exec_())

