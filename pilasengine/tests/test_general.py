# -*- encoding: utf-8 -*-
import sys
import unittest
import pilasengine


class TestGeneral(unittest.TestCase):
    def setUp(self):
        self.pilas = pilasengine.iniciar()

    def testEscribirConAvisar(self):
        actor = self.pilas.avisar("Hola mundo !!")


if __name__ == '__main__':
    unittest.main()
