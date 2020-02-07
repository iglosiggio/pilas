# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pilasengine/interprete/lanas.ui'
#
# Created by: PyQt5 UI code generator 4.11.4
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

class Ui_Lanas(object):
    def setupUi(self, Lanas):
        Lanas.setObjectName(_fromUtf8("Lanas"))
        Lanas.resize(656, 349)
        self.verticalLayout = QtWidgets.QVBoxLayout(Lanas)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_interprete = QtWidgets.QStackedWidget(Lanas)
        self.widget_interprete.setObjectName(_fromUtf8("widget_interprete"))
        self.verticalLayout.addWidget(self.widget_interprete)
        self.consejo = QtWidgets.QLabel(Lanas)
        self.consejo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.consejo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.consejo.setLineWidth(0)
        self.consejo.setMidLineWidth(0)
        self.consejo.setText(_fromUtf8(""))
        self.consejo.setObjectName(_fromUtf8("consejo"))
        self.verticalLayout.addWidget(self.consejo)

        self.retranslateUi(Lanas)
        QtCore.QMetaObject.connectSlotsByName(Lanas)

    def retranslateUi(self, Lanas):
        Lanas.setWindowTitle(_translate("Lanas", "Lanas - Interprete de Python", None))
        Lanas.setToolTip(_translate("Lanas", "Guardar contenido del interprete", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Lanas = QtWidgets.QWidget()
    ui = Ui_Lanas()
    ui.setupUi(Lanas)
    Lanas.show()
    sys.exit(app.exec_())

