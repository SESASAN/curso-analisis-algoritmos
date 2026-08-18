# Semana 02 — Configuración del entorno de trabajo

## Entorno virtual

Desde la raíz del repositorio (no dentro de `ejercicios-clase/`):

```bash
python3 -m venv venv
source venv/bin/activate
```

El prefijo `(venv)` en la terminal confirma que el entorno está activo. La
carpeta `venv/` está listada en `.gitignore` y no se sube al repositorio.

> Si tu shell es `fish` en lugar de `bash`/`zsh`, activa con
> `source venv/bin/activate.fish` (el script `activate` normal falla en
> fish porque usa sintaxis de `sh`).

## Dependencias

Con el entorno activado se instaló `matplotlib` y se generó el archivo de
dependencias reproducible en la raíz del repositorio:

```bash
pip install matplotlib
pip freeze > requirements.txt
```

## Cómo reproducir el entorno

Otra persona (o yo mismo en otra máquina) puede recrear exactamente el mismo
entorno así:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Esto se verificó borrando `venv/` y reinstalando desde `requirements.txt`:
`pip list` mostró las mismas librerías que antes de borrar la carpeta.

## Contenido de esta carpeta

- `refactor_pep8_antes.py`: script original de la Parte 3, sin modificar.
- `refactor_pep8.py`: mismo script refactorizado con PEP 8 y type hints.
- `clasificador_anios.py`: ejercicio integrador (Parte 4), clasificador de
  años bisiestos.
