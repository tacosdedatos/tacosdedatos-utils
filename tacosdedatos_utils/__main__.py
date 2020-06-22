# type: ignore[attr-defined]

import random
from enum import Enum
from typing import Optional

import typer
from rich.console import Console

from tacosdedatos_utils import __version__
from tacosdedatos_utils.example import hello
from tacosdedatos_utils.manejo_de_archivos import arbol
from tacosdedatos_utils.manejo_de_proyectos import crear_proyecto


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="tacosdedatos-utils",
    help="Una coleccion de herramientas para facilitar el analisis y visualizacion de datos por @tacosdedatos.",
    add_completion=False,
)
console = Console()


def version_callback(value: bool):
    """Prints the version of the package."""
    if value:
        console.print(
            f"[yellow]tacosdedatos-utils[/] version: [bold blue]{__version__}[/]"
        )
        raise typer.Exit()


@app.command(name="")
def main(
    name: str = typer.Option(..., help="Name of person to greet."),
    color: Optional[Color] = typer.Option(
        None,
        "-c",
        "--color",
        "--colour",
        case_sensitive=False,
        help="Color for name. If not specified then choice will be random.",
    ),
    version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the tacosdedatos-utils package.",
    ),
):
    """Prints a greeting for a giving name."""
    if color is None:
        # If no color specified use random value from `Color` class
        color = random.choice(list(Color.__members__.values()))

    greeting: str = hello(name)
    console.print(f"[bold {color}]{greeting}[/]")


@app.command("crear")
def crear(
    nombre: str = typer.Option(
        ..., help="Nombre del proyecto que quieres crear"
    ),
    tipo: str = typer.Option(..., help="Tipo de proyecto: `analisis`"),
    dir: str = typer.Option(
        ..., help="Carpeta donde quieres crear tu proyecto"
    ),
):
    """Crea el esqueleto de un proyecto. Como cookiecutter pero más básico.

    Parameters
    ----------
    nombre : str, optional
        Nombre del proyecto que quieres crear
    tipo : str, optional
        Tipo de proyecto: `analisis`
    dir : str, optional
        Carpeta donde quieres crear tu proyecto
    """
    typer.echo(f"Creando tu proyecto {nombre} en {dir}")
    crear_proyecto(nombre, tipo, dir)
