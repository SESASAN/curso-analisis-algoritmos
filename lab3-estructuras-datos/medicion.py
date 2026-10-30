"""Medicion del tiempo de busqueda: lista enlazada vs. tabla hash.

Experimento A: tiempo medio de busqueda de guias inexistentes frente al
numero de guias n, con alfa cercano a 2 en la tabla.
Experimento B: con n fijo, tiempo medio de busqueda frente al factor de
carga alfa.

Genera graficas/lista_vs_tabla.png y graficas/tiempo_vs_alfa.png.
"""

import random
import statistics
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

TAMANOS = [100, 500, 1000, 5000, 20000, 50000]
N_FIJO = 20000
ALFAS = [0.25, 0.5, 1, 2, 4, 10]
BUSQUEDAS = 200
MUESTRA_VERIFICACION = 200
REPETICIONES = 7
SEMILLA = 42
ESTADOS = ["en bodega", "en reparto", "entregado", "devuelto"]
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_guias(n: int, semilla: int = SEMILLA) -> list[tuple[int, str]]:
    """Genera n guias distintas de diez digitos con un estado al azar.

    Args:
        n: cantidad de guias.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista de n parejas (guia, estado) sin guias repetidas.
    """
    azar = random.Random(semilla)
    guias = azar.sample(range(10**9, 10**10), n)
    return [(guia, azar.choice(ESTADOS)) for guia in guias]


def es_primo(numero: int) -> bool:
    """Indica si un numero es primo, probando divisores hasta su raiz.

    Args:
        numero: entero a revisar.

    Returns:
        True si el numero es primo, False en otro caso.
    """
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True


def primo_cercano(objetivo: float) -> int:
    """Busca el primo mas cercano a un valor, empezando por los menores.

    Args:
        objetivo: valor alrededor del cual se busca el primo.

    Returns:
        El primo mas cercano a `objetivo` (al menos 2).
    """
    centro = max(2, round(objetivo))
    distancia = 0
    while True:
        if es_primo(centro - distancia):
            return centro - distancia
        if es_primo(centro + distancia):
            return centro + distancia
        distancia += 1


def construir(
    guias: list[tuple[int, str]], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye una lista y una tabla con las mismas guias.

    Args:
        guias: parejas (guia, estado) a insertar.
        m: numero de casillas de la tabla.

    Returns:
        Una tupla (lista, tabla) con las guias ya insertadas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia, estado in guias:
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def verificar(
    lista: ListaEnlazada, tabla: TablaHash, guias: list[tuple[int, str]]
) -> None:
    """Comprueba que lista y tabla devuelven el estado correcto.

    Usa una muestra de guias existentes elegida con semilla fija.

    Args:
        lista: lista enlazada con las guias.
        tabla: tabla hash con las mismas guias.
        guias: parejas (guia, estado) insertadas en ambas.

    Raises:
        AssertionError: si alguna estructura devuelve un estado distinto.
    """
    azar = random.Random(SEMILLA)
    cantidad = min(MUESTRA_VERIFICACION, len(guias))
    for guia, estado in azar.sample(guias, cantidad):
        assert lista.buscar(guia) == estado
        assert tabla.buscar(guia) == estado


def medir(
    estructura: ListaEnlazada | TablaHash, consultas: list[int]
) -> float:
    """Mide el tiempo medio por busqueda, en segundos.

    Repite la tanda de busquedas REPETICIONES veces y toma la mediana,
    para reducir el ruido del sistema operativo. Solo se cronometran
    las busquedas.

    Args:
        estructura: lista o tabla donde se busca.
        consultas: guias a buscar.

    Returns:
        La mediana del tiempo medio por busqueda, en segundos.
    """
    tiempos: list[float] = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        for guia in consultas:
            estructura.buscar(guia)
        tiempos.append((time.perf_counter() - inicio) / len(consultas))
    return statistics.median(tiempos)


def experimento_a() -> list[tuple[int, int, float, float, float]]:
    """Mide lista y tabla para cada n, con alfa cercano a 2.

    Returns:
        Una lista de filas (n, m, alfa, tiempo_lista, tiempo_tabla), con
        los tiempos en segundos por busqueda.
    """
    filas = []
    for n in TAMANOS:
        guias = generar_guias(n)
        m = primo_cercano(n / 2)
        lista, tabla = construir(guias, m)
        verificar(lista, tabla, guias)
        consultas = generar_guias_inexistentes(
            {guia for guia, _ in guias}, BUSQUEDAS
        )
        filas.append(
            (n, m, tabla.factor_carga(), medir(lista, consultas),
             medir(tabla, consultas))
        )
    return filas


def experimento_b() -> list[tuple[int, float, float]]:
    """Mide la tabla con n fijo y distintos factores de carga.

    Returns:
        Una lista de filas (m, alfa, tiempo_tabla), con el tiempo en
        segundos por busqueda.
    """
    guias = generar_guias(N_FIJO)
    consultas = generar_guias_inexistentes(
        {guia for guia, _ in guias}, BUSQUEDAS
    )
    filas = []
    for alfa in ALFAS:
        m = primo_cercano(N_FIJO / alfa)
        lista, tabla = construir(guias, m)
        verificar(lista, tabla, guias)
        filas.append((m, tabla.factor_carga(), medir(tabla, consultas)))
    return filas


def graficar_a(filas: list[tuple[int, int, float, float, float]]) -> None:
    """Dibuja el tiempo medio por busqueda frente a n.

    Args:
        filas: resultados del experimento A.
    """
    tamanos = [fila[0] for fila in filas]
    # Se pasa a microsegundos para que los valores sean legibles.
    lista_us = [fila[3] * 1e6 for fila in filas]
    tabla_us = [fila[4] * 1e6 for fila in filas]
    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, lista_us, "o-", label="Lista enlazada")
    plt.plot(tamanos, tabla_us, "s-", label="Tabla hash (α ≈ 2)")
    plt.title("Búsqueda de guías inexistentes: lista vs. tabla hash")
    plt.xlabel("Número de guías n")
    plt.ylabel("Tiempo medio por búsqueda (µs)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "lista_vs_tabla.png", dpi=120)
    plt.close()


def graficar_b(filas: list[tuple[int, float, float]]) -> None:
    """Dibuja el tiempo medio por busqueda frente al factor de carga.

    Args:
        filas: resultados del experimento B.
    """
    alfas = [fila[1] for fila in filas]
    tabla_us = [fila[2] * 1e6 for fila in filas]
    plt.figure(figsize=(8, 5))
    plt.plot(alfas, tabla_us, "s-", color="tab:orange",
             label=f"Tabla hash (n = {N_FIJO})")
    plt.title("Efecto del factor de carga en la búsqueda infructuosa")
    plt.xlabel("Factor de carga α = n / m (guías por casilla)")
    plt.ylabel("Tiempo medio por búsqueda (µs)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_alfa.png", dpi=120)
    plt.close()


def main() -> None:
    """Corre ambos experimentos, imprime las tablas y guarda graficas."""
    CARPETA_GRAFICAS.mkdir(exist_ok=True)

    filas_a = experimento_a()
    print("Experimento A (tiempos en microsegundos por busqueda)")
    print(f"{'n':>7} {'m':>7} {'alfa':>6} {'lista':>10} {'tabla':>8}")
    for n, m, alfa, t_lista, t_tabla in filas_a:
        print(f"{n:>7} {m:>7} {alfa:>6.2f} {t_lista * 1e6:>10.2f} "
              f"{t_tabla * 1e6:>8.3f}")
    graficar_a(filas_a)

    filas_b = experimento_b()
    print(f"\nExperimento B (n = {N_FIJO}, microsegundos por busqueda)")
    print(f"{'m':>7} {'alfa':>6} {'tabla':>8}")
    for m, alfa, t_tabla in filas_b:
        print(f"{m:>7} {alfa:>6.2f} {t_tabla * 1e6:>8.3f}")
    graficar_b(filas_b)


if __name__ == "__main__":
    main()
