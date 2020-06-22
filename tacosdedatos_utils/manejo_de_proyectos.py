"""Utilidades para el manejo de proyectos."""

from pathlib import Path


def crear_proyecto(
    nombre: str = "nuevo-proyecto", tipo: str = "analisis", dir: str = "."
) -> None:
    """Crea una carpeta nueva para un poryecto con una estructura básica predeterminada. Como cookiecutter pero más básico.

    Parameters
    ----------
    nombre : str, optional
        Nombre de tu nuevo proyecto.
    tipo : str, optional
        Tipo de proyecto. Por el momento solo existe el proyecto de `analisis` de datos. Por default, "analisis".
    dir : str, optional
        Directorio donde crear el proyecto. Por default es en el que ejecutas el script `Path(.)`.
    """
    PROJECT_DIR = Path(dir).joinpath(nombre)

    DATA_DIR = PROJECT_DIR.joinpath("datos")
    DOCS_DIR = PROJECT_DIR.joinpath("docs")
    NOTEBOOKS_DIR = PROJECT_DIR.joinpath("notebooks")
    REPORTES_DIR = PROJECT_DIR.joinpath("reportes")
    SRC_DIR = PROJECT_DIR.joinpath("src")

    DATA_BRUTOS_DIR = DATA_DIR.joinpath("brutos")
    DATA_EXTERNOS_DIR = DATA_DIR.joinpath("externos")
    DATA_INTERINOS_DIR = DATA_DIR.joinpath("interinos")
    DATA_PROCESADOS_DIR = DATA_DIR.joinpath("procesados")
    DATA_FINALES_DIR = DATA_DIR.joinpath("finales")

    REPORTES_FIGURAS_DIR = REPORTES_DIR.joinpath("figuras")

    SRC_DATOS = SRC_DIR.joinpath("datos")
    SRC_EXTERNOS = SRC_DIR.joinpath("externos")
    SRC_HERRAMIENTAS = SRC_DIR.joinpath("herramientas")
    SRC_MODELOS = SRC_DIR.joinpath("modelos")
    SRC_VISUALIZACIONES = SRC_DIR.joinpath("visualizaciones")
    SRC_APPS = SRC_DIR.joinpath("apps")

    README = PROJECT_DIR.joinpath("README.md")
    AUTORES = PROJECT_DIR.joinpath("AUTORES.md")

    # Crea carpetas principales
    PROJECT_DIR.mkdir()
    DATA_DIR.mkdir()
    DOCS_DIR.mkdir()
    NOTEBOOKS_DIR.mkdir()
    REPORTES_DIR.mkdir()
    SRC_DIR.mkdir()

    # nivel 2
    DATA_BRUTOS_DIR.mkdir()
    DATA_EXTERNOS_DIR.mkdir()
    DATA_INTERINOS_DIR.mkdir()
    DATA_PROCESADOS_DIR.mkdir()
    DATA_FINALES_DIR.mkdir()

    REPORTES_FIGURAS_DIR.mkdir()

    SRC_DATOS.mkdir()
    SRC_EXTERNOS.mkdir()
    SRC_HERRAMIENTAS.mkdir()
    SRC_MODELOS.mkdir()
    SRC_VISUALIZACIONES.mkdir()
    SRC_APPS.mkdir()

    # archivos importantes
    README.touch()
    AUTORES.touch()

    DATA_BRUTOS_DIR.joinpath(".gitkeep").touch()
    DATA_EXTERNOS_DIR.joinpath(".gitkeep").touch()
    DATA_INTERINOS_DIR.joinpath(".gitkeep").touch()
    DATA_PROCESADOS_DIR.joinpath(".gitkeep").touch()
    DATA_FINALES_DIR.joinpath(".gitkeep").touch()

    REPORTES_FIGURAS_DIR.joinpath(".gitkeep").touch()

    SRC_DATOS.joinpath(".gitkeep").touch()
    SRC_EXTERNOS.joinpath(".gitkeep").touch()
    SRC_HERRAMIENTAS.joinpath(".gitkeep").touch()
    SRC_MODELOS.joinpath(".gitkeep").touch()
    SRC_VISUALIZACIONES.joinpath(".gitkeep").touch()
    SRC_APPS.joinpath(".gitkeep").touch()

    NOTEBOOKS_DIR.joinpath(".gitkeep").touch()
    DOCS_DIR.joinpath(".gitkeep").touch()
