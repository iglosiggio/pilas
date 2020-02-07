import sys
import unittest
import pilasengine


class TestFondos(unittest.TestCase):
    def setUp(self):
        self.pilas = pilasengine.iniciar()

    def testPuedeCrearUnFondo(self):
        fondo = self.pilas.fondos.Plano()
        self.assertTrue(fondo, "Puede hacer un fondo.")
