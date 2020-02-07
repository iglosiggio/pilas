import sys
import unittest
from PyQt5 import QtWidgets

import pilasengine


class TestFondos(unittest.TestCase):
    app = QtWidgets.QApplication(sys.argv)

    def setUp(self):
        self.pilas = pilasengine.iniciar()

    def testPuedeCrearUnFondo(self):
        fondo = self.pilas.fondos.Plano()
        self.assertTrue(fondo, "Puede hacer un fondo.")
