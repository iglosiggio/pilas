import sys
import signal
from PyQt5 import QtWidgets

# Permitiendo cerrar pilas usando CTRL+C
signal.signal(signal.SIGINT, signal.SIG_DFL)

sys.path.append('./')
sys.path.append('../')

import pilasengine

app = QtWidgets.QApplication(sys.argv)
asistente = pilasengine.abrir_asistente()
sys.exit(app.exec_())