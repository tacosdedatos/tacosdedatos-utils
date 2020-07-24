## 1.3.0 (2020-07-23)
* Agrega función `.crear_paleta_tableau()` que tranforma una lista de colores en formato hex a XML para poder agregar al archivo `~/Documents/My Tableau Repository/Preferences.tps` para agregar tu paleta de colores personalizada a Tableau.

## 1.2.0 (2020-07-18)
* Agrega el submódulo `viz` con la función `tema_altair` la cual es un _theme_ de Altair. Para más información sobre temas en Altair visita [la documentación](https://altair-viz.github.io/user_guide/configuration.html?highlight=theme#altair-themes) o este artículo para crear tu propio _theme_: [Consistently Beautiful Visualizations with Altair Themes](https://towardsdatascience.com/consistently-beautiful-visualizations-with-altair-themes-c7f9f889602) por su servilleta Sergio Sánchez 🤓

## 1.1.0 (2020-07-08)
* Agrega el submódulo `manejo_de_datos` con la función `mostrar_dfs` para mostrar más de un DataFrame o Serie de pandas como _output_ de una celda de jupyter notebook.
* También cambia la estructura del proyecto, ahora las funciones son incluides al nivel mas alto de `tacosdedatos_utils`. Ya no es necesario importar `tacosdedatos_utils.manejo_de_proyectos` para usar `crear_proyecto()`, por ejemplo. Ahora solo es

```python
import tacosdedatos_utils as tdd
tdd.crear_proyecto()
```

## 1.0.0 (2020-06-22)
* ¡Versiôn 1.0!
  - Esta versión rompe las versiones anteriores ya que cambia el nombre de los módulos `project_management` y `file_management` a sus equivalentes en español.

## 0.2.2 (2020-06-17)
* Actualiza la documentación en el README para reflejar los cambios recientes y agregar ejemplos de las funciones.

## 0.2.1 (2020-06-17)
* Agrega la función `tacosdedatos_utils.project_management.crear_proyect()`
* Agrega el comando `crear` a la herramienta de línea de comandos. Ahora puedes usar `tacosdedatos-utils crear --nombre "proyecto-chido" --tipo "analisis" --dir "."`

## 0.2.0 (2020-06-17)
* Agrega la primera función `tacosdedatos_utls.file_management.arbol()` 

## 0.1.0 (2020-06-17)
* Creación del proyecto
