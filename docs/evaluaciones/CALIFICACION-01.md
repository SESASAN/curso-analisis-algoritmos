# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Sebastián Jesús Pérez Araujo · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `b9a24d8`

Muy buen trabajo: el código es limpio y el informe cubre todas las partes.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 25 |
| Calidad de la explicación teórica | 23 / 25 |
| Corrección de la implementación | 19 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **88 / 100** |
| **Nota (0–5)** | **4.40** |

## 1. Corrección conceptual (19 / 25)
**Lo que hizo bien:**
- Separa bien "da el resultado correcto" de "lo da a tiempo" y nombra la ventana de cuatro horas como lo que no se cumple.
- Explica que duplicar el servidor mejora 2 veces, frente a un crecimiento de unas 3.600 veces.
- En la Parte 2 identifica al paciente y al operador como afectados y dice quién asume el costo. También explica que la lista debe quedar completa y correcta, no solo rápida.

**Lo que puede mejorar:**
- El ejemplo propio (Fast 6.2) es válido, pero le faltan datos concretos: cuántos registros, cuánto tardaba y qué límite se incumplía.
- La parte ambiental es general. Falta relacionar las horas de ejecución con el consumo de energía acumulado durante años, aunque sea con una estimación sencilla.
- Los dos perjuicios a personas podrían describirse con más detalle (por ejemplo, qué le pasa a un paciente concreto que se llama tarde).

## 2. Calidad de la explicación teórica (23 / 25)
**Lo que hizo bien:**
- Define peor, mejor y promedio indicando sobre qué se toma cada uno, elige el peor caso para decidir y deja escrita la predicción antes de medir.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con el método maestro, verificando que se cumple el caso 2.
- Hace el análisis línea a línea de insertion sort y presenta la tabla de complejidades.

**Lo que puede mejorar:**
- En la tabla de líneas, el costo de la línea del desplazamiento quedó como "depende del caso"; debía quedar expresado con la suma de los t_i.

## 3. Corrección de la implementación (19 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no modifican la lista recibida y cuentan solo comparaciones entre elementos (n-1 en el mejor caso, n(n-1)/2 en el inverso).
- `merge_sort` tiene su propia mezcla recursiva, sin `sorted()` ni `list.sort()`.
- Los generadores dan listas del tamaño pedido, sin repetidos y con semilla. El código cumple PEP 8 y tiene type hints y docstrings.

**Lo que puede mejorar:**
- Las funciones auxiliares de merge sort tienen docstring de una sola línea; conviene usar el formato completo con Args y Returns.

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes rotulados, leyenda y las curvas pedidas en los mismos ejes.
- Identifica con datos el peor (C), el mejor (B) y el promedio (A), y lo contrasta con su predicción.
- Describe lo que hace cada curva en la Parte 4 y lo compara con lo calculado. Estima las 16 horas de insertion sort y los pocos segundos de merge sort, y lo declara como estimación.

**Lo que puede mejorar:**
- Dice que insertion sort no cabría "incluso en el escenario más favorable", pero la cifra usada es la del escenario C, que es el peor. Faltó estimar también el escenario B, que es el actual.
- En el concepto técnico falta una consideración distinta del tiempo propia de merge sort, como la memoria extra que necesita.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Estructura de carpetas y nombres de archivos tal como se pidió, con las gráficas visibles en el informe.
- Instrucciones claras de reproducción, enlaces al código en cada parte práctica y cinco commits descriptivos.

## ¿El código funciona?
Sí. Los scripts de las Partes 3 y 4 corren sin errores en unos 10 segundos, ordenan correctamente y generan las gráficas.

## Para el próximo laboratorio
- Respalde los ejemplos propios con datos concretos (cantidad, tiempo y límite incumplido).
- Cuando hable de consumo de energía, haga una estimación sencilla de horas acumuladas.
- Complete las funciones auxiliares con docstrings de formato completo.
- En el concepto técnico, estime el tiempo para el escenario real de uso, no solo para el peor.
