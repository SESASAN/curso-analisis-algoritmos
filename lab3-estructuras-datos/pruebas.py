"""Pruebas con assert de la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash

ESTADOS = ["en bodega", "en reparto", "entregado", "devuelto"]

# Busqueda exitosa e infructuosa con la serie de ejemplo del enunciado.
ejemplo = [
    (1000000010, "en bodega"),
    (1000000024, "en reparto"),
    (1000000017, "en bodega"),
    (1000000005, "entregado"),
]
lista = ListaEnlazada()
tabla = TablaHash(7)
for guia, estado in ejemplo:
    lista.insertar(guia, estado)
    tabla.insertar(guia, estado)

for guia, estado in ejemplo:
    assert lista.buscar(guia) == estado
    assert tabla.buscar(guia) == estado
assert lista.buscar(1000000099) is None
assert tabla.buscar(1000000099) is None
assert lista.tamano == 4
assert tabla.tamano == 4

# Estructuras vacias: toda busqueda es infructuosa.
assert ListaEnlazada().buscar(10) is None
assert TablaHash(7).buscar(10) is None
assert TablaHash(7).factor_carga() == 0

# Colision forzada: con m = 7, las guias 10, 24 y 17 caen en la casilla 3.
tabla = TablaHash(7)
for guia in (10, 24, 17):
    assert tabla.hash(guia) == 3
    tabla.insertar(guia, "en bodega")

assert tabla.buscar(10) == "en bodega"
assert tabla.buscar(24) == "en bodega"
assert tabla.buscar(17) == "en bodega"
assert tabla.buscar(99) is None
# 31 tambien cae en la casilla 3, pero no esta: recorre la cadena completa.
assert tabla.buscar(31) is None
assert tabla.casillas[3].tamano == 3
for casilla in range(7):
    if casilla != 3:
        assert tabla.casillas[casilla].tamano == 0
assert tabla.factor_carga() == 3 / 7

# Insercion al inicio: la ultima guia insertada queda en la cabeza.
assert tabla.casillas[3].cabeza is not None
assert tabla.casillas[3].cabeza.guia == 17

# Con m = 1 todas las guias caen en la misma casilla y siguen apareciendo.
tabla = TablaHash(1)
for guia in range(50):
    tabla.insertar(guia, "en bodega")
assert tabla.casillas[0].tamano == 50
assert tabla.buscar(0) == "en bodega"
assert tabla.buscar(50) is None
assert tabla.factor_carga() == 50

# 30 colecciones aleatorias: lista y tabla responden lo mismo.
azar = random.Random(2026)
for _ in range(30):
    n = azar.randint(1, 300)
    m = azar.choice([1, 7, 13, 97, 101])
    guias = azar.sample(range(10**9, 10**10), n)
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia in guias:
        estado = azar.choice(ESTADOS)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    for guia in guias:
        assert lista.buscar(guia) == tabla.buscar(guia)
        assert lista.buscar(guia) is not None

    existentes = set(guias)
    inexistentes = 0
    while inexistentes < 30:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None
            inexistentes += 1

    assert tabla.factor_carga() == n / m

print("Todas las pruebas pasaron.")
