# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pilas/data/manual.ui'
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

class Ui_ManualWindow(object):
    def setupUi(self, ManualWindow):
        ManualWindow.setObjectName(_fromUtf8("ManualWindow"))
        ManualWindow.resize(844, 508)
        ManualWindow.setMinimumSize(QtCore.QSize(500, 400))
        self.centralwidget = QtWidgets.QWidget(ManualWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.webView.setStatusTip(_fromUtf8(""))
        self.webView.setAccessibleDescription(_fromUtf8(""))
        self.webView.setProperty("url", QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayout.addWidget(self.webView, 0, 0, 1, 1)
        ManualWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ManualWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ManualWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ManualWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ManualWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ManualWindow)
        QtCore.QMetaObject.connectSlotsByName(ManualWindow)

    def retranslateUi(self, ManualWindow):
        ManualWindow.setWindowTitle(_translate("ManualWindow", "manual de pilas-engine", None))

from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManualWindow = QtWidgets.QMainWindow()
    ui = Ui_ManualWindow()
    ui.setupUi(ManualWindow)
    ManualWindow.show()
    sys.exit(app.exec_())

