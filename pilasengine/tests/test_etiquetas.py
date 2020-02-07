# -*- encoding: utf-8 -*-
import sys
import time
import unittest
import pilasengine


class TestEtiquetas(unittest.TestCase):
    def setUp(self):
        self.pilas = pilasengine.iniciar(modo_test=True)

    def testEtiquetasEnActores(self):
        # Se asegura que todos los actores nacen con
        # una etiqueta que identifica la clase.

        m = self.pilas.actores.Mono()
        self.assertEqual(str(m.etiquetas), "['mono']")

        a = self.pilas.actores.Aceituna()
        self.assertEqual(str(a.etiquetas), "['aceituna']")

        # Se asegura que se pueden agregar y eliminar
        # etiquetas.

        a.etiquetas.agregar('enemigo')
        self.assertEqual(str(a.etiquetas), "['aceituna', 'enemigo']")

        a.etiquetas.eliminar('enemigo')
        self.assertEqual(str(a.etiquetas), "['aceituna']")

    def testEtiquetasEnFiguras(self):
        # Se asegura que todos los actores nacen con
        # una etiqueta que identifica la clase.

        m = self.pilas.fisica.Circulo()
        self.assertEqual(str(m.etiquetas), "['circulo']")

        rectangulo = self.pilas.fisica.Rectangulo(0, 0, 100, 100)
        self.assertEqual(str(rectangulo.etiquetas), "['rectangulo']")

        # Se asegura que se pueden agregar y eliminar
        # etiquetas.

        rectangulo.etiquetas.agregar('enemigo')
        self.assertEqual(str(rectangulo.etiquetas), "['rectangulo', 'enemigo']")

        rectangulo.etiquetas.eliminar('enemigo')
        self.assertEqual(str(rectangulo.etiquetas), "['rectangulo']")


if __name__ == '__main__':
    unittest.main()
