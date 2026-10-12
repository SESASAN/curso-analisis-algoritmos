"""Medicion del tiempo: fuerza bruta vs. divide y venceras.

Mide ambas soluciones del subarreglo maximo sobre la misma lista para
cada tamano, comprueba que den la misma suma y genera la grafica
graficas/tiempo_vs_n.png.
"""

import random
import statistics
import time
from typing import Callable

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANOS = [10, 20, 50, 100, 200, 500, 1000, 2000, 4000, 8000]
REPETICIONES = 3
SEMILLA = 42


def generar_serie(n: int, semilla: int = SEMILLA) -> list[float]:
    """Genera una serie de n variaciones diarias de caja.

    Args:
        n: cantidad de dias de la serie.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n enteros entre -100 y 100.
    """
    rng = random.Random(semilla)
    return [rng.randint(-100, 100) for _ in range(n)]


def divide_y_venceras(valores: list[float]) -> tuple[int, int, float]:
    """Llama a subarreglo_maximo sobre toda la serie.

    Args:
        valores: variacion diaria de caja, con al menos un elemento.

    Returns:
        Una tupla (inicio, fin, suma) de la mejor racha de la serie.
    """
    return subarreglo_maximo(valores, 0, len(valores) - 1)


def medir(
    algoritmo: Callable[[list[float]], tuple[int, int, float]],
    valores: list[float],
) -> tuple[float, float]:
    """Mide el tiempo mediano de un algoritmo sobre una serie.

    Args:
        algoritmo: funcion que recibe la serie y devuelve la mejor racha.
        valores: serie ya generada; su creacion no se cronometra.

    Returns:
        Una tupla con el tiempo mediano en segundos (de REPETICIONES
        corridas) y la suma maxima encontrada.
    """
    tiempos = []
    suma = 0.0
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        suma = algoritmo(valores)[2]
        tiempos.append(time.perf_counter() - inicio)
    return statistics.median(tiempos), suma


def ejecutar_experimento() -> dict[str, list[float]]:
    """Corre el experimento completo para todos los tamanos.

    Returns:
        Un diccionario con los tiempos de cada algoritmo, en el mismo
        orden que TAMANOS.
    """
    tiempos = {"Fuerza bruta": [], "Divide y venceras": []}
    print(f"{'n':>6}  {'fuerza bruta (s)':>18}  {'divide y venceras (s)':>22}")
    for n in TAMANOS:
        valores = generar_serie(n)
        t_fb, suma_fb = medir(subarreglo_fuerza_bruta, valores)
        t_dc, suma_dc = medir(divide_y_venceras, valores)
        assert suma_fb == suma_dc, f"las sumas difieren para n = {n}"
        tiempos["Fuerza bruta"].append(t_fb)
        tiempos["Divide y venceras"].append(t_dc)
        print(f"{n:>6}  {t_fb:>18.6f}  {t_dc:>22.6f}")
    return tiempos


def graficar(tiempos: dict[str, list[float]]) -> None:
    """Genera la grafica de tiempo vs. tamano para ambos algoritmos.

    Args:
        tiempos: tiempos medidos de cada algoritmo, en el mismo orden
            que TAMANOS.
    """
    plt.figure(figsize=(8, 5))
    for nombre, valores in tiempos.items():
        plt.plot(TAMANOS, valores, marker="o", label=nombre)
    plt.title("Subarreglo maximo: tiempo de ejecucion vs. tamano de entrada")
    plt.xlabel("Tamano de entrada (numero de dias)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("graficas/tiempo_vs_n.png", dpi=150)
    plt.close()


def main() -> None:
    """Punto de entrada del script."""
    tiempos = ejecutar_experimento()
    graficar(tiempos)
    print("Grafica guardada en graficas/tiempo_vs_n.png")


if __name__ == "__main__":
    main()
