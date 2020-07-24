"""Utilidades para la visualización de datos"""
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Union


def tema_altair():
    """Un tema de Altair. Colores, dimensiones, tamaño de ticks, de etiquetas, de leyenda.

    Returns
    -------
    tema : Dict
        Un diccionario con las especificaciones del tema.
    """
    axisColor = "#282828"
    markColor = "#282828"
    backgroundColor = "#FFFAFA"
    font = "Helvetica"
    labelfont = "Helvetica"
    sourcefont = "Helvetica"
    gridColor = "#C9C9C9"
    axisLabelSize = 14
    return {
        "width": 600,
        "height": 400,
        "autosize": "pad",
        "config": {
            "padding": 10,
            "geoshape": {
                "fill": "#D9D9D6",
                "stroke": "#2B3E4B",
                "strokeWidth": 0.5,
            },
            "arc": {"fill": markColor,},
            "area": {"fill": markColor,},
            "axisBand": {"grid": False,},
            "axisBottom": {
                "domain": False,
                "domainColor": "black",
                "domainWidth": 3,
                "grid": True,
                "gridColor": gridColor,
                "gridWidth": 1,
                "labelFontSize": axisLabelSize,
                "labelFont": labelfont,
                "labelPadding": 8,
                "labelAngle": 0,
                "tickColor": axisColor,
                "tickSize": 10,
                "titleFontSize": 16,
                "titlePadding": 10,
                "titleFont": font,
                "title": "",
            },
            "axisLeft": {
                "domainColor": axisColor,
                "domainWidth": 1,
                "gridColor": gridColor,
                "gridWidth": 1,
                "labelFontSize": axisLabelSize,
                "labelFont": labelfont,
                "labelPadding": 8,
                "tickColor": axisColor,
                "tickSize": 10,
                "tickCount": 10,
                "ticks": True,
                "titleFontSize": 18,
                "titlePadding": 10,
                "titleFont": font,
                "titleAngle": 0,
                "titleX": -70,
                "titleY": -18,
                "titleAnchor": "start",
            },
            "axisRight": {
                "domainColor": axisColor,
                "domainWidth": 1,
                "gridColor": gridColor,
                "gridWidth": 1,
                "labelFontSize": axisLabelSize,
                "labelFont": labelfont,
                "labelPadding": 4,
                "tickColor": axisColor,
                "tickSize": 10,
                "ticks": True,
                "titleFontSize": 14,
                "titlePadding": 10,
                "titleFont": font,
            },
            "axisTop": {
                "domain": False,
                "domainColor": "black",
                "domainWidth": 3,
                "grid": True,
                "gridColor": gridColor,
                "gridWidth": 1,
                "labelFontSize": axisLabelSize,
                "labelFont": labelfont,
                "labelPadding": 4,
                "tickColor": axisColor,
                "tickSize": 10,
                "titleFontSize": 14,
                "titlePadding": 10,
                "titleFont": font,
            },
            "background": backgroundColor,
            "group": {"fill": backgroundColor,},
            "legend": {
                "labelFontSize": 18,
                "labelFont": labelfont,
                "labelLimit": 500,
                "padding": 5,
                "symbolSize": 200,
                "symbolType": "square",
                "titleFontSize": 20,
                "titlePadding": 5,
                "titleFont": font,
                "titleLimit": 400,
            },
            "line": {
                "color": markColor,
                "stroke": markColor,
                "strokeWidth": 3,
            },
            "rule": {
                "color": markColor,
                "stroke": markColor,
                "strokeWidth": 3,
            },
            "tick": {
                "color": markColor,
                "stroke": markColor,
                "strokeWidth": 1,
            },
            "trail": {
                "color": markColor,
                "stroke": markColor,
                "strokeWidth": 0,
                "size": 5,
            },
            "path": {"stroke": markColor, "strokeWidth": 0.5,},
            "point": {"filled": True,},
            "rect": {"fill": "#A20C4B", "opacity": 0.3,},
            "range": {
                "category": [
                    "#dc0d7a",
                    "#02a3cd",
                    "#e4a100",
                    "#dc0d12",
                    "#0DDC6F",
                    "#074a7e",
                    "#e46800",
                    "#aa3594",
                    "#a20c4b",
                ],
                "diverging": [
                    "#dc0d12",
                    "#e9686b",
                    "#fbe1e1",
                    "#dff4f9",
                    "#81d1e6",
                    "#03a3cd",
                ],
                "heatmap": [
                    "#fff7fd",
                    "#ffdbf7",
                    "#ffb9ec",
                    "#ff91dc",
                    "#ff67c7",
                    "#f83faf",
                    "#ef1d95",
                    "#e4007c",
                ],
            },
            "symbol": {
                "opacity": 1,
                "shape": "circle",
                "size": 40,
                "strokeWidth": 1,
            },
            "style": {
                "bar": {"binSpacing": 2, "fill": markColor, "stroke": False,},
                "text": {
                    "font": sourcefont,
                    "fontSize": 10,
                    "align": "right",
                    "fontWeight": 100,
                    "size": 10,
                },
            },
            "title": {
                "anchor": "start",
                "fontSize": 28,
                "fontWeight": 600,
                "font": font,
                "offset": 20,
            },
            "view": {"stroke": False, "padding": 15,},
            "header": {
                "fontWeight": 400,
                "labelFontSize": axisLabelSize,
                "labelFont": labelfont,
                "titleFontSize": 20,
                "titleFont": font,
                "title": " ",
                "titleBaseline": "bottom",
                "titleOffset": -30,
            },
        },
    }


def crear_paleta_tableau(
    colores: List[str], tipo: str, nombre: str, agregar_a_tableau: bool = False
) -> Union[str, None]:
    r"""Tranforma una lista de colores (en formato hex) en una paleta en formato XML para copiar y pegar en Preferences.tps para su uso en tableau. Si el argumento `agregar_a_tableau` es True puedes agregarla directamente con esta función.

    Parameters
    ----------
    colores : List[str]
        Una lista de colores en formato hex.
    tipo : str
        Tipo de paleta de colores: "divergente", "regular", o "secuencial".
    nombre : str
        Nombre de tu paleta de colores. Por ejemplo, "likert - rojo a azul"
    agregar_a_tableau : bool, optional
        Si es True, esta función busca tu `Preferences.tps` en `~/Documents/My Tableau Repository/` y agrega la paleta para que no tengas que hacerlo manualmente. Por default es False.

    Returns
    -------
    Union[str, None]
        La paleta lista en el formato correcto para `Preferences.tps`. Si `agregar_a_tableau` es True, no se regresa la paleta. Se agrega directo a Preferences.tps

    
    Examples
    --------
    `crear_paleta_tableau()` te da una cadena de caracteres con caracteres especiales (como el \ n para saltar líneas o \ t para tabs). Asegurate de hacer `print()` el resultado de la función para copiar y pegar en `Preferences.tps`.
    Por ejemplo:
    >>>> colores_tdd = [
                    "#dc0d7a",
                    "#02a3cd",
                    "#e4a100",
                    "#dc0d12",
                    "#0DDC6F",
                    "#074a7e",
                    "#e46800",
                    "#aa3594",
                    "#a20c4b",
                ]
    >>>> paleta_nueva = tdd.crear_paleta_tableau(colores = colores_tdd, tipo = "regular", nombre = "tacosdedatos - colores principales")
    >>>> print(paleta_nueva)
    >>>> <color-palette name="tacosdedatos - colores principales" type="regular">
            <color>#dc0d7a</color>
            <color>#02a3cd</color>
            <color>#e4a100</color>
            <color>#dc0d12</color>
            <color>#0DDC6F</color>
            <color>#074a7e</color>
            <color>#e46800</color>
            <color>#aa3594</color>
            <color>#a20c4b</color>
        </color-palette>
    """
    tipos_de_paletas = ["regular", "secuencial", "divergente"]
    if tipo not in tipos_de_paletas:
        raise TypeError(
            f"Las paletas pueden ser solo `regular`, `secuencial`, or `divergente`, tu escogiste: {tipo}"
        )

    if tipo == "secuencial":
        tipo = "ordered-sequential"
    if tipo == "divergente":
        tipo = "ordered-divergent"

    lista_de_colores = [f"\t<color>{color}</color>\n" for color in colores]
    colores_de_la_paleta = "".join(lista_de_colores)

    paleta = f'<color-palette name="{nombre}" type="{tipo}">\n{colores_de_la_paleta}</color-palette>\n'

    if agregar_a_tableau:
        repo_tableau = Path.home() / "Documents/My Tableau Repository/"
        if repo_tableau.exists():
            arbol = ET.parse(repo_tableau / "Preferences.tps")
            raiz = arbol.getroot()
            preferences = raiz[0]
            nueva_paleta = ET.fromstring(paleta)
            preferences.append(nueva_paleta)
            arbol.write(repo_tableau / "Preferences.tps")
        else:
            raise OSError(
                f"No encontramos la carpeta {str(repo_tableau)} asegurate que exista y tengas acceso a ella."
            )
        return None
    else:
        return paleta
