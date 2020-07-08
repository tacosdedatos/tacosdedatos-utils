"""Utilidades para el manejo de datos."""

from typing import Union

import pandas as pd
from IPython.display import display_html


def mostrar_dfs(
    *dfs: Union[pd.DataFrame, pd.Series], espacio: int = 20
) -> None:
    """Muestra más de un DataFrame o Serie de pandas en una celda de jupyter notebooks.

    Parameters
    ----------
    espacio : int, optional
        El espacio entre cada DataFrame en pixeles, por default 20 
    """
    html = f"""<div style="display:flex;">"""
    for df in dfs:
        try:
            html_del_df = df._repr_html_()
        except AttributeError:
            html_del_df = f"<pre>{repr(df)}</pre>"

        html += f"<div style='margin-right:{espacio}px;'>{html_del_df}</div>"

    html += "</div>"
    display_html(html, raw=True)
