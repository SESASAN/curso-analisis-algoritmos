import random

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
    suma_cruzada,
)


def verificar(serie, suma_esperada=None):
    """Corre ambas funciones y comprueba que sean consistentes."""
    copia = list(serie)

    fb_inicio, fb_fin, fb_suma = subarreglo_fuerza_bruta(serie)
    dc_inicio, dc_fin, dc_suma = subarreglo_maximo(serie, 0, len(serie) - 1)

    assert serie == copia, "una funcion modifico la lista recibida"
    assert fb_suma == dc_suma, f"las sumas difieren en {serie}"
    assert sum(serie[fb_inicio:fb_fin + 1]) == fb_suma
    assert sum(serie[dc_inicio:dc_fin + 1]) == dc_suma
    if suma_esperada is not None:
        assert fb_suma == suma_esperada
        assert dc_suma == suma_esperada
    return dc_inicio, dc_fin, dc_suma


# Serie de ocho dias de la situacion problema.
serie = [-3, 5, -2, 8, -6, 3, 9, -4]
assert subarreglo_fuerza_bruta(serie)[2] == 17
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17
assert verificar(serie, 17)[:2] == (1, 6)

# Un solo elemento (positivo, negativo y cero).
verificar([7], 7)
verificar([-7], -7)
verificar([0], 0)

# Dos elementos.
verificar([-1, 2], 2)
verificar([2, -1], 2)

# Todos negativos: la mejor racha es el elemento menos negativo.
verificar([-8, -3, -5, -1, -9], -1)

# Todos positivos: la mejor racha es la serie completa.
inicio, fin, suma = verificar([4, 1, 7, 2, 9], 23)
assert (inicio, fin) == (0, 4)

# El mejor tramo cruza el punto medio (indices 3 y 4 en esta serie).
cruce = [-2, -3, 4, 5, 6, -1, -4, -2]
inicio, fin, suma = verificar(cruce, 15)
assert (inicio, fin) == (2, 4)
assert suma_cruzada(cruce, 0, 3, 7) == (2, 4, 15)

# Cruce con numero impar de elementos.
verificar([1, -1, 5, 6, -2, 3, -9], 12)

# Listas aleatorias: ambas funciones deben dar la misma suma.
rng = random.Random(2024)
for _ in range(100):
    n = rng.randint(1, 60)
    lista = [rng.randint(-100, 100) for _ in range(n)]
    verificar(lista)

# Listas aleatorias con muchos negativos y con muchos positivos.
for _ in range(30):
    n = rng.randint(1, 60)
    verificar([rng.randint(-100, 20) for _ in range(n)])
    verificar([rng.randint(-20, 100) for _ in range(n)])

print("Todas las pruebas pasaron.")
