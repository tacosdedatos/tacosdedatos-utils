# type: ignore[attr-defined]
"""Una coleccion de herramientas para facilitar el analisis y visualizacion de datos por @tacosdedatos."""

try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:  # pragma: no cover
    from importlib_metadata import version, PackageNotFoundError


try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

from .manejo_de_archivos import *
from .manejo_de_datos import *
from .manejo_de_proyectos import *
from .viz import *
