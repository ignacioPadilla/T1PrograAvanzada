# -*- coding: utf-8 -*-
"""Tarea1PrograAvanzada.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TTYamiPrMxCtDmxDt7x3f53daijbcEoq
"""

import math
import numpy as np
import time
import matplotlib.pyplot as plt

# Decorador para medir el tiempo de ejecución
def calcularTiempo(funcion):
    def funcionModificada(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        final = time.time()
        return final - inicio, resultado  # Retorna el tiempo y el resultado
    return funcionModificada

class Caminos:
    def __init__(self, N, M):
        self.N = N  # número de filas de la grilla PCB
        self.M = M  # número de columnas de la grilla PCB

    # Primer Método combinatoria
    @calcularTiempo
    def TotalCaminosCombinatoria(self):
        return math.comb(self.N + self.M - 2, self.M - 1)

    # Segundo Método recurrencia
    @calcularTiempo
    def TotalCaminosRecurrencia(self):
        grilla = np.zeros((self.N, self.M), int)  # Crea la grilla

        # Inicializa la primera fila y columna
        grilla[:, 0] = 1  # Primera columna
        grilla[0, :] = 1  # Primera fila

        # Llena la tabla usando la recurrencia
        for i in range(1, self.N):
            for j in range(1, self.M):
                grilla[i][j] = grilla[i-1][j] + grilla[i][j-1]

        return grilla[self.N - 1][self.M - 1]

    #Para hacer más dinamico la llamada a los distintos métodos
    def Metodo(self, metodo):
        if metodo == "combinatoria":
            tiempo, _ = self.TotalCaminosCombinatoria()
        elif metodo == "recurrencia":
            tiempo, _ = self.TotalCaminosRecurrencia()
        return tiempo

### Generar los gráficos ###
def generar_grafico_tiempos():
    tamanos_grilla = [(5, 5), (10, 10), (15, 15), (20, 20), (25, 25)]
    tiempos_combinatoria = []
    tiempos_recurrencia = []

    for N, M in tamanos_grilla:
        ClaseCaminos = Caminos(N, M)
        tiempo_combinatoria = ClaseCaminos.Metodo("combinatoria")
        tiempo_recurrencia = ClaseCaminos.Metodo("recurrencia")
        tiempos_combinatoria.append(tiempo_combinatoria)
        tiempos_recurrencia.append(tiempo_recurrencia)

    # Crear el gráfico
    tamanos = [N for N, M in tamanos_grilla]
    plt.plot(tamanos, tiempos_combinatoria, label="Combinatoria", marker="o")
    plt.plot(tamanos, tiempos_recurrencia, label="Recurrencia", marker="x")

    # Título y etiquetas
    plt.title("Comparación de Tiempos de Ejecución")
    plt.xlabel("Tamaño de la Grilla (NxM)")
    plt.ylabel("Tiempo de Ejecución (segundos)")
    plt.legend()

    # Guardar el gráfico en formato SVG
    plt.savefig("grafico_tiempos.svg")
    print("Gráfico guardado como 'grafico_tiempos.svg'")

    # Mostrar el gráfico
    plt.show()

### Ejecutar la generación del gráfico ###
generar_grafico_tiempos()

"""Preguntas

• ¿Qué es un paradigma de programación?

Un paradigma de programación es una manera o estilo de programación de software. Existen diferentes formas de diseñar un lenguaje de programación y varios modos de trabajar para obtener los resultados que necesitan los programadores.  Se trata de un conjunto de métodos sistemáticos aplicables en todos los niveles del diseño de programas para resolver problemas computacionales.

Los lenguajes de programación adoptan uno o varios paradigmas en función del tipo de órdenes que permiten implementar como, por ejemplo, Python o JavaScript, que son multiparadigmas.

¿En qué se basa la programación orientada a objetos?

La programación orientada a objetos se basa en el concepto de crear un modelo del problema de destino en sus programas. La programación orientada a objetos disminuye los errores y promociona la reutilización del código. Python es un lenguaje orientado a objetos. Los objetos definidos en Python tienen las características siguientes:

Identidad. Cada objeto debe ser distinguido y ello debe poder demostrarse mediante pruebas. Las pruebas is e is not existen para este fin.
Estado Cada objeto debe ser capaz de almacenar el estado. Para este fin, existen atributos, tales como variables de instancias y campos.
Comportamiento. Cada objeto debe ser capaz de manipular su estado. Para este fin existen métodos.

explicar la diferencia de rendimiento entre 𝑂(1) y 𝑂(𝑛)

O(1) u orden 1 se refiere al tiempo de ejecución del programa que es constante, es decir no depende del tamaño de la entrada. O(n) u orden n se refiere a que el tiempo de ejecución del programa aumenta linealmente con el tamaño de la entrada. Por tanto la principal diferencia radica en que los algoritmos O(1) son más rapidos y eficientes que los O(n)

¿Cómo se calcula el orden en un programa que funciona por etapas?

Es importante dividir el programa en etapas individuales ya que cada etapa puede tener un orden distinto. Una vez identificados los distintos ordenes de cada etapa del programa tambien es importante considerar  si las etapas se ejecutan secuancialmente una después de otra donde el orden va a ser el orden predomiante o si hay paralelismo de ejecución. La complejidad de esos casos a menudo va a estar dominada por la más costoda, es decir la de mayor orden

¿Cómo se puede determinar la complejidad temporal de un algoritmo recursivo?

Es importante identificar la fórmula de la recurrencia que expresa el tiempo de ejecución. Usar teormea del maestro, en donde se compara con la forma general del teorema del maestro y luego se aplica el teorema del maestro con lo que finalmente se puede obtener la complejidad del problema.
"""