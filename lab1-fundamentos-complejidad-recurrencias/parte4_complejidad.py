"""Experimento de la Parte 4: insertion sort vs. merge sort.

Mide el tiempo de insertion_sort y merge_sort sobre el escenario A
(aleatorio) de Tamiza, para los mismos tamanos de entrada de la
Parte 3, y genera la grafica parte4_tiempo.png.
"""

import statistics
import time
from typing import Callable

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3

ALGORITMOS = {
    "Insertion sort": insertion_sort,
    "Merge sort": merge_sort,
}


def medir(
    algoritmo: Callable[[list[int]], tuple[list[int], int]], n: int
) -> float:
    """Mide el tiempo mediano de un algoritmo de ordenamiento.

    Args:
        algoritmo: funcion de ordenamiento instrumentada a medir.
        n: tamano del lote (escenario A) a ordenar.

    Returns:
        Tiempo mediano en segundos de REPETICIONES corridas.
    """
    tiempos = []
    for _ in range(REPETICIONES):
        datos = generar_aleatorio(n)
        inicio = time.perf_counter()
        algoritmo(datos)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.median(tiempos)


def ejecutar_experimento() -> dict[str, list[float]]:
    """Corre el experimento comparativo sobre el escenario A.

    Returns:
        Un diccionario por algoritmo con los tiempos medidos para
        cada tamano en TAMANOS.
    """
    resultados = {nombre: [] for nombre in ALGORITMOS}
    for nombre, algoritmo in ALGORITMOS.items():
        for n in TAMANOS:
            tiempo = medir(algoritmo, n)
            resultados[nombre].append(tiempo)
            print(f"{nombre:15s} n={n:5d}  t={tiempo:.4f}s")
    return resultados


def graficar(resultados: dict[str, list[float]]) -> None:
    """Genera la grafica de tiempo vs. tamano para ambos algoritmos."""
    plt.figure(figsize=(8, 5))
    for nombre, tiempos in resultados.items():
        plt.plot(TAMANOS, tiempos, marker="o", label=nombre)
    plt.title("Insertion sort vs. merge sort (escenario A, aleatorio)")
    plt.xlabel("Tamano de entrada (numero de registros)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/parte4_tiempo.png", dpi=150)
    plt.close()


def main() -> None:
    """Punto de entrada del script."""
    resultados = ejecutar_experimento()
    graficar(resultados)
    print("Grafica guardada en graficas/parte4_tiempo.png")


if __name__ == "__main__":
    main()
