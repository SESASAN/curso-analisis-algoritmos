# Retroalimentación — Laboratorio 3: Estructuras de datos

**Estudiante:** Sebastián Jesús Pérez Araujo · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `0106811`

Excelente trabajo: un laboratorio completo, ordenado y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 24 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **98 / 100** |
| **Nota (0–5)** | **4.90** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explica bien la colisión y la ilustra con las guías 10, 24 y 17 con m = 7, tanto en encadenamiento (`17 → 24 → 10`) como en sondeo lineal (casillas 3, 4 y 5).
- Compara ventajas y costos de ambos métodos, incluyendo que con direccionamiento abierto α no puede pasar de 1 y que borrar es más difícil.
- Justifica por qué la tabla no sirve para rangos y estima bien la altura (399.999) y las comparaciones del árbol degenerado frente al equilibrado (unas 19).
- La recomendación (tabla hash más árbol balanceado) es acertada y la estimación a 5.000.000 está declarada como estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- La estimación de la tabla con 5.000.000 de envíos es corta: afirma que seguiría cerca de 0,16 µs, pero no discute si algo podría cambiar al crecer tanto la tabla.
  → *Cómo corregirlo:* piense qué otros factores, además de α, podrían afectar el tiempo con una tabla de millones de casillas, y diga si su medición alcanza para descartarlos.
- No dice cuánto costaría la consulta por rango en la tabla frente al árbol con un ejemplo de tamaño.
  → *Cómo corregirlo:* compare, con los 400.000 envíos, cuántas guías habría que revisar en cada estructura para un rango que devuelva pocas guías.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el `Θ(n)` de la lista y el `Θ(1 + α)` de la tabla paso a paso, nombra el supuesto de hash uniforme simple y explica que si todas las guías caen en una casilla el costo vuelve a `Θ(n)`.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` y `TablaHash` funcionan: búsquedas exitosas e infructuosas, colisión forzada con m = 7 (casilla 3 con tres guías), `factor_carga` igual a 3 / 7.
- La búsqueda es iterativa, la tabla reutiliza la lista y no usa `dict`, `set` ni `hash()`.
- Las pruebas cubren los casos pedidos y 30 colecciones aleatorias; todas pasan.
- Todas las funciones tienen *docstrings* con `Args` y `Returns`, *type hints* y las líneas en blanco entre funciones.

## 4. Calidad del análisis de las gráficas (24 / 25)
**Lo que hizo bien:**
- Ambas gráficas tienen título, ejes rotulados con unidades y leyenda; la primera cubre seis valores de n con ambas curvas en los mismos ejes y la segunda seis valores de α.
- Los factores de crecimiento (5,08 para la lista entre 1.000 y 5.000, 0,99 para la tabla) coinciden con sus tablas y sus gráficas.
- Incluyó tablas con los valores medidos, porque la curva de la tabla queda pegada al eje.
- Cronometra solo las búsquedas con `time.perf_counter()`, usa semilla fija y verifica que ambas estructuras coincidan.

**Lo que puede mejorar (y cómo corregirlo):**
- En la pregunta 2 calcula el factor de crecimiento con un solo par de valores de n.
  → *Cómo corregirlo:* repita el cálculo con otro par consecutivo (por ejemplo, los dos más grandes) y compruebe si el resultado es parecido.
- Para la segunda gráfica da la pendiente, pero no compara el valor a α = 10 con el de α = 1 frente a lo que predice `1 + α`.
  → *Cómo corregirlo:* calcule cuánto debería multiplicarse el tiempo según `1 + α` entre esos dos puntos y compárelo con lo medido.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada (`lab3-estructuras-datos/` con los cinco archivos pedidos) y entregó en `main`.
- El `README.md` tiene su nombre, instrucciones de reproducción, el orden pedido, enlaces al código en cada parte y gráficas que se ven con ruta relativa.
- Hay cuatro commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores y la medición corre en pocos segundos y genera las dos gráficas.
