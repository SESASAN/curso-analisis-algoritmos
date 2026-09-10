"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    Ordena de mayor a menor, que es el orden que necesita Tamiza para
    generar la lista de llamadas. No modifica la lista recibida:
    trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    resultado = list(datos)
    comparaciones = 0
    for i in range(1, len(resultado)):
        clave = resultado[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if resultado[j] < clave:
                resultado[j + 1] = resultado[j]
                j -= 1
            else:
                break
        resultado[j + 1] = clave
    return resultado, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    Ordena de mayor a menor, que es el orden que necesita Tamiza para
    generar la lista de llamadas. No modifica la lista recibida:
    trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    return _dividir(list(datos))


def _dividir(lista: list[int]) -> tuple[list[int], int]:
    """Divide la lista a la mitad y combina las dos mitades ordenadas."""
    if len(lista) <= 1:
        return lista, 0

    medio = len(lista) // 2
    izquierda, comparaciones_izquierda = _dividir(lista[:medio])
    derecha, comparaciones_derecha = _dividir(lista[medio:])
    combinado, comparaciones_mezcla = _combinar(izquierda, derecha)

    total = (
        comparaciones_izquierda + comparaciones_derecha + comparaciones_mezcla
    )
    return combinado, total


def _combinar(
    izquierda: list[int], derecha: list[int]
) -> tuple[list[int], int]:
    """Mezcla dos listas ya ordenadas de mayor a menor en una sola."""
    resultado = []
    comparaciones = 0
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado, comparaciones
