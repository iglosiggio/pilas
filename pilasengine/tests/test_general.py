# -*- encoding: utf-8 -*-
import sys
import unittest
from PyQt5 import QtWidgets
import pilasengine


class TestGeneral(unittest.TestCase):
    app = QtWidgets.QApplication(sys.argv)

    def setUp(self):
        import pilasengine
        self.pilas = pilasengine.iniciar()

    def testEscribirConAvisar(self):
        actor = self.pilas.avisar("Hola mundo !!")

if __name__ == '__main__':
    unittest.main()