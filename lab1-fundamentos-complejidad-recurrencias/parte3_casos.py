"""Experimento de la Parte 3: peor caso, mejor caso y caso promedio.

Ejecuta insertion_sort sobre los tres escenarios de Tamiza (A, B y C)
para distintos tamanos de entrada, mide tiempo y comparaciones, y
genera las graficas parte3_comparaciones.png y parte3_tiempo.png.
"""

import statistics
import time
from typing import Callable

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3

ESCENARIOS = {
    "A - Aleatorio": generar_aleatorio,
    "B - Casi ordenado": generar_casi_ordenado,
    "C - Orden inverso": lambda n, semilla=42: generar_inverso(n),
}


def medir(generador: Callable[[int], list[int]], n: int) -> tuple[float, int]:
    """Mide el tiempo mediano y las comparaciones de insertion_sort.

    Args:
        generador: funcion que produce el lote de datos de entrada.
        n: tamano del lote a generar y ordenar.

    Returns:
        Una tupla con el tiempo mediano en segundos (de REPETICIONES
        corridas) y el numero de comparaciones de la ultima corrida.
    """
    tiempos = []
    comparaciones = 0
    for _ in range(REPETICIONES):
        datos = generador(n)
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(datos)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.median(tiempos), comparaciones


def ejecutar_experimento() -> dict[str, dict[str, list[float]]]:
    """Corre el experimento completo sobre los tres escenarios.

    Returns:
        Un diccionario por escenario con las listas de tiempos y
        comparaciones medidas para cada tamano en TAMANOS.
    """
    resultados = {
        nombre: {"tiempos": [], "comparaciones": []} for nombre in ESCENARIOS
    }
    for nombre, generador in ESCENARIOS.items():
        for n in TAMANOS:
            tiempo, comparaciones = medir(generador, n)
            resultados[nombre]["tiempos"].append(tiempo)
            resultados[nombre]["comparaciones"].append(comparaciones)
            print(
                f"{nombre:20s} n={n:5d}  t={tiempo:.4f}s  comp={comparaciones}"
            )
    return resultados


def graficar(resultados: dict[str, dict[str, list[float]]]) -> None:
    """Genera las graficas de comparaciones y de tiempo por escenario."""
    plt.figure(figsize=(8, 5))
    for nombre, datos in resultados.items():
        plt.plot(TAMANOS, datos["comparaciones"], marker="o", label=nombre)
    plt.title("Insertion sort: comparaciones vs. tamano de entrada")
    plt.xlabel("Tamano de entrada (numero de registros)")
    plt.ylabel("Numero de comparaciones")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte3_comparaciones.png", dpi=150)
    plt.close()

    plt.figure(figsize=(8, 5))
    for nombre, datos in resultados.items():
        plt.plot(TAMANOS, datos["tiempos"], marker="o", label=nombre)
    plt.title("Insertion sort: tiempo de ejecucion vs. tamano de entrada")
    plt.xlabel("Tamano de entrada (numero de registros)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte3_tiempo.png", dpi=150)
    plt.close()


def main() -> None:
    """Punto de entrada del script."""
    resultados = ejecutar_experimento()
    graficar(resultados)
    print("Graficas guardadas en graficas/parte3_comparaciones.png y "
          "graficas/parte3_tiempo.png")


if __name__ == "__main__":
    main()
