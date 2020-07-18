"""Utilidades para la visualización de datos"""

from typing import Dict


def tema_altair() -> Dict:
    """Un tema de Altair. Colores, dimensiones, tamaño de ticks, de etiquetas, de leyenda.

    Returns
    -------
    tema : Dict
        Un diccionario con las especificaciones del tema.
    """
    markColor = "#282828"
    axisColor = "#282828"
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
