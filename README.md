pilas-doblea
============

Pilas es un motor para realizar videojuegos de manera rápida y sencilla. `pilas-doblea` es un port de este motor a Python3 y QT5 para poder preservar trabajos ya realizados con el framework.

Es una herramienta orientada a programadores casuales o principiantes, es ideal para quienes quieran aprender a realizar sus primeros videojuegos.

![](extras/preview.png)

## Estado actual del port

El menú principal `pilasengine` funciona en su totalidad (se exponen varias cosas desde python por medio de QWebChannel). Todos los ejemplos se ejecutan sin lanzar excepciones y la suite de tests pasa sin problemas. La aplicación [TierraLuna](https://github.com/HuayraLinux/TierraLuna) funciona con el nuevo framework una vez actualizados los prints en su codebase.

El directorio `pilas` que contenía la versión más vieja del framework fué eliminado.

Debido a que el port fué hecho en gran parte corriendo `sed` sobre todos los ficheros es posible que haya múltiples typos. Imports fuera de lugar o similares. Todo reporte de error es bienvenido!

## ¿Cómo empezar?

Una buena forma de comenzar con pilas es instalar todo el kit de desarrollo siguiendo las intrucciones de nuestra web:

- http://www.pilas-engine.com.ar

Y una vez instalada la biblioteca, se puede invocar al comando ``pilas -e`` para ver una lista completa de ejemplos y minijuegos.

## Instalación

TBD - Una vez estemos seguros que todo el código fué migrado correctamente (WebKit por WebEgine y demases) habrá binarios disponibles para descargar

## Tests

Los tests se pueden ejecutar manualmente en tu equipo con el siguiente comando:

    make utest

En caso de encontrar algún problema al migrar tus aplicaciones de pilas-engine a pilas-doblea reportá el issue si es posible con un fragmento de código reproducible (así podemos armar una suite de tests de regresión).

## Licencia

Pilas es software libre, y se distribuye bajo la licencia LGPLv3.

Visita nuestro sitio web para obtener mas detalles:

- http://www.pilas-engine.com.ar

