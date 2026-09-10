"""Generadores de lotes de registros para los escenarios de Tamiza.

En los tres generadores, el orden objetivo es el que Tamiza necesita
para su lista de llamadas: de mayor a menor indice de riesgo. El
indice de riesgo real de Tamiza esta acotado entre 0 y 1000, pero los
lotes de este laboratorio llegan a 6400 registros, asi que aqui se
generan indices distintos en un rango mas amplio para poder tener esa
cantidad de valores sin repetir.
"""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    rng = random.Random(semilla)
    return rng.sample(range(0, n * 10), n)


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    rng = random.Random(semilla)
    n_ordenado = round(n * 0.98)
    n_nuevo = n - n_ordenado

    ordenados = []
    valor = n * 10
    for _ in range(n_ordenado):
        valor -= rng.randint(1, 5)
        ordenados.append(valor)

    nuevos = rng.sample(range(0, valor), n_nuevo)
    return ordenados + nuevos


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    return list(range(n))
