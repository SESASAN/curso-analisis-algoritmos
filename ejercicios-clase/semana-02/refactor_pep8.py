"""Refactor PEP 8 del cálculo de promedio de una lista de números."""

from collections.abc import Sequence


def calcular_promedio(lista: Sequence[float]) -> float:
    """Calcula el promedio de una lista de números.

    Args:
        lista: secuencia de números (int o float) a promediar.

    Returns:
        El promedio de los elementos de la lista.
    """
    suma: float = 0.0
    for x in lista:
        suma = suma + x
    return suma / len(lista)


def main() -> None:
    """Punto de entrada del script."""
    numeros = [1, 2, 3, 4, 5]
    print(calcular_promedio(numeros))


if __name__ == "__main__":
    main()
