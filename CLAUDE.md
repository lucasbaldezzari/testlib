# CLAUDE.md — testlib

Contexto del proyecto para Claude Code. Este archivo viaja con el repositorio.

---

## Descripción del proyecto

**testlib** es una librería Python de uso **educativo**, diseñada para enseñar a estudiantes de ingeniería biomédica cómo crear, empaquetar e instalar una librería Python propia de manera local.

- **Audiencia:** Estudiantes y docentes de ingeniería biomédica / procesamiento de señales.
- **Estado:** Alpha (v2.0.0) — en desarrollo activo con fines pedagógicos.
- **Licencia:** MIT
- **Python mínimo:** 3.11

---

## Instalación local (modo desarrollo)

```bash
pip install -e .
# Con dependencias de desarrollo:
pip install -e ".[dev]"
# Con dependencias de documentación:
pip install -e ".[docs]"
```

---

## Comandos frecuentes

```bash
# Ejecutar todos los tests
pytest

# Tests con reporte de cobertura
pytest --cov=testlib

# Formatear código
black src/ tests/

# Linting
ruff check src/ tests/

# Corregir automáticamente con ruff
ruff check --fix src/ tests/

# Construir el paquete para distribución
python -m build
```

---

## Estructura de módulos

```
src/testlib/
├── __init__.py           # Expone __version__. Punto de entrada público.
├── version.py            # __version__ = "2.0.0" (fuente única de verdad)
├── logging_config.py     # configure_logging() — configura logging para toda la lib
├── signals/
│   ├── __init__.py       # Exporta: Filter
│   └── filter.py         # Clase Filter: pasabanda(), pasabajos()
└── images/
    ├── __init__.py       # Exporta: conv2D, modifyContrast, show
    ├── visualization.py  # show() — visualización de imágenes (esqueleto)
    └── transform/
        ├── __init__.py   # Exporta: conv2D, modifyContrast
        └── filters.py    # conv2D(), modifyContrast() — SIN IMPLEMENTAR (pass)
```

### Estado por módulo

| Módulo | Estado | Notas |
|--------|--------|-------|
| `signals.Filter` | 🟡 Esqueleto | `pasabanda()` y `pasabajos()` validan `None` pero no filtran aún |
| `images.visualization.show` | 🟡 Esqueleto | Solo logging, sin lógica real |
| `images.transform.conv2D` | 🔴 Vacío | `pass` — pendiente de implementar |
| `images.transform.modifyContrast` | 🔴 Vacío | `pass` — pendiente de implementar |
| `logging_config.configure_logging` | ✅ Completo | Funcional, bien documentado |

---

## Decisiones de diseño

### Logging con NullHandler
`__init__.py` registra un `NullHandler` para que la librería no emita logs por defecto. Los consumidores (apps o tests) deben llamar a `configure_logging()` explícitamente para activar la salida.

```python
# Patrón correcto al usar la librería:
from testlib.logging_config import configure_logging
configure_logging(level="DEBUG")
```

### Versión como única fuente de verdad
La versión se define en `src/testlib/version.py` y `pyproject.toml` la lee dinámicamente:
```toml
[tool.setuptools.dynamic]
version = {attr = "testlib.version.__version__"}
```
**Nunca editar la versión en dos lugares.** Solo modificar `version.py`.

### Layout `src/`
Se usa el layout `src/testlib/` (en lugar de `testlib/` en la raíz) para evitar importaciones accidentales del código fuente sin instalar. Esto es una buena práctica de empaquetado Python.

### Tests como scripts de demostración
Los archivos en `tests/` actualmente funcionan como scripts de demostración más que como tests unitarios con `assert`. El objetivo pedagógico es mostrar cómo se importa y usa la librería.

---

## Dependencias principales

| Paquete | Uso previsto |
|---------|-------------|
| `numpy` | Arrays y operaciones numéricas sobre señales/imágenes |
| `scipy` | Filtros digitales (pasabanda, pasabajos, etc.) |
| `pandas` | Manejo de datos tabulares |
| `matplotlib` | Visualización estática |
| `plotly` | Visualización interactiva |
| `pyqtgraph` + `PyQt5` | Visualización en tiempo real |

---

## Roadmap pedagógico (orientativo)

1. Implementar `Filter.pasabanda()` y `Filter.pasabajos()` usando `scipy.signal`
2. Implementar `conv2D()` con `numpy` o `scipy.ndimage`
3. Implementar `modifyContrast()` con operaciones de histograma
4. Agregar tests unitarios reales con `pytest` y `assert`
5. Agregar documentación con Sphinx
