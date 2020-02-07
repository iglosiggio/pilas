# -*- coding: utf-8 -*-
# pilas engine: un motor para hacer videojuegos
#
# Copyright 2010-2014 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar
import codecs
import os
import sys
import time

from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QMainWindow
from PyQt5.QtGui import (QKeySequence, QIcon)

from pilasengine import utils
from pilasengine.interprete import editor, lanas

from pilasengine.interprete.ventana_interprete import VentanaInterprete


def abrir():
    MainWindow = QMainWindow()

    ui = VentanaInterprete()
    ui.setupUi(MainWindow)

    utils.centrar_ventana(MainWindow)
    MainWindow.show()
    MainWindow.raise_()
    utils.destacar_ventanas()
    return MainWindow

def abrir_editor():
    MainWindow = QMainWindow()

    ui = VentanaInterprete()
    ui.setupUi(MainWindow)

    utils.centrar_ventana(MainWindow)
    MainWindow.show()
    MainWindow.raise_()

    ui.ocultar_el_interprete()
    ui.mostrar_editor()

    utils.destacar_ventanas()
    return MainWindow


def abrir_script_con_livereload(archivo):
    MainWindow = QMainWindow()

    ui = VentanaInterprete()
    ui.setupUi(MainWindow)

    utils.centrar_ventana(MainWindow)
    MainWindow.show()
    ui.colapsar_interprete()
    MainWindow.raise_()
    ui.editor.abrir_archivo_del_proyecto(archivo)
    ui.editor.ejecutar()

    return MainWindow
