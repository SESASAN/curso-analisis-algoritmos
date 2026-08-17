"""Refactor PEP 8 del cálculo de promedio de una lista de números."""


def calcular_promedio(lista: list[float]) -> float:
    """Calcula el promedio de una lista de números.

    Args:
        lista: lista de números (int o float) a promediar.

    Returns:
        El promedio de los elementos de la lista.
    """
    suma = 0
    for x in lista:
        suma = suma + x
    return suma / len(lista)


def main() -> None:
    """Punto de entrada del script."""
    numeros = [1, 2, 3, 4, 5]
    print(calcular_promedio(numeros))


if __name__ == "__main__":
    main()
