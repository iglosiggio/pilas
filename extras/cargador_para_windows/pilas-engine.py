# -*- encoding: utf-8 -*-
import sys
import signal

import importlib
from PyQt5 import *
from PyQt5 import Qt
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtOpenGL
import Box2D
import pygame
import tkMessageBox
import Tkinter
import imp
import sys
import os
import json
import new
import uuid
import code

from xml.dom import minidom

def ejecutar_archivo(nombre):
    try:
        imp.load_source("__main__", nombre)
    except Exception, e:
        terminar_con_error("Error al ejecutar " + nombre + ":\n" + str(e))

def terminar_con_error(mensaje):
    app = QtWidgets.QApplication(sys.argv)
    error = QtWidgets.QMessageBox()
    error.critical(None, "Uh, algo anda mal...", mensaje)
    sys.exit(1)


pilasengine = __import__('pilasengine')

if os.path.exists('ejecutar.py'):
    #window = Tkinter.Tk()
    #window.wm_withdraw()
    ejecutar_archivo('ejecutar.py') 
    sys.exit(0)

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[-1]):
        ejecutar_archivo(sys.argv[-1])
        sys.exit(0)
    else:
        if sys.argv[1] == '-u':
            sys.exit(0)
	terminar_con_error("No se puede abrir el archivo " + sys.argv[-1] + "\n" + "los argumentos son:" + str(sys.argv))

#window = Tkinter.Tk()
#window.wm_withdraw()


app = QtWidgets.QApplication(sys.argv)

pilasengine.configuracion.Configuracion()

if '-i' in sys.argv:
    from pilasengine import interprete
    _ = interprete.abrir()
elif '-t' in sys.argv:
    from pilasengine import utils
    utils.realizar_pruebas()
    sys.exit(1)
else:
    _ = pilasengine.abrir_asistente()

icono = pilasengine.utils.obtener_ruta_al_recurso('icono.ico')
app.setWindowIcon(QtGui.QIcon(icono))
#mainwindow.setWindowIcon(QtWidgets.QIcon(icono))

sys.exit(app.exec_())
