# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Sebastián Jesús Pérez Araujo · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `c4be4a1`

Excelente trabajo: un laboratorio completo, ordenado y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **97 / 100** |
| **Nota (0–5)** | **4.85** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar entre 20 y 50 datos y lo apoya en su tabla.
- Compara con el máximo de un arreglo: el costo de combinar es constante y la recurrencia da Θ(n), igual que recorrerlo una vez.
- Recomienda divide y vencerás y estima 1.000.000 de registros (unas 6,45 horas contra unos 2 segundos), declarándolo como estimación y con un razonamiento que no es una regla de tres lineal.

**Lo que puede mejorar:**
- En la pregunta 4 podría decir con más claridad que dividir no gana porque combinar no ahorra nada, mientras que en el subarreglo el cruce se resuelve en tiempo lineal.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` y explica de dónde sale cada término.
- Resuelve con el método maestro (a = 2, b = 2) y comprueba la condición del caso 2.
- Justifica el Θ(n²) de la fuerza bruta contando los n(n+1)/2 tramos con suma acumulada.

**Lo que puede mejorar:**
- Explique también por qué el barrido del caso cruzado visita cada elemento una sola vez, para justificar el Θ(n).

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en 160 listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y ninguna función cambia la lista recibida.
- Hay tipos y *docstrings* en todas las funciones y el código cumple PEP 8.

**Lo que puede mejorar:**
- `suma_cruzada` usa `float("-inf")` como valor inicial; funciona, pero conviene explicarlo en un comentario.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con diez tamaños.
- Calcula el factor al pasar de 4000 a 8000 (4,06 para fuerza bruta y 2,22 para divide y vencerás) y lo compara con 4 y 2,17.
- Sus valores del informe (1,49 s y 0,011 s en n = 8000) coinciden con la gráfica.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta `lab2-divide-y-vencer/` tiene todos los archivos del entregable y el informe sigue el orden pedido.
- La gráfica está incrustada con ruta correcta, cada parte enlaza su código y hay instrucciones de reproducción.
- Hay cuatro commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, la medición corre sin errores y genera la gráfica en la ruta indicada.

## Para el próximo laboratorio
- Justifique en el informe por qué cada barrido lineal cuesta Θ(n).
- Explique con una frase el criterio general de cuándo dividir compensa.
- Mantenga el hábito de commits descriptivos y de usar `.gitignore`.
