# Ejemplos de uso

## Funcionalidades

* la función `arbol` para mostrar los contenidos de la carpeta que le pases.
```python
import tacosdedatos_utils.file_management as tdd

tdd.arbol("./notebooks")
>>>> + notebooks
        + Cpp.ipynb
        + Data.ipynb
        + Fasta.ipynb
        + Lorenz.ipynb
        + R.ipynb
        + audio
            + audio.wav
        + bqplot.ipynb
        + images
            + marie.png
            + xeus-cling.png
            + xtensor.png
            + xwidgets.png
        + lorenz.py
        + pandas.ipynb
```

* la función `crear_proyecto`
```python
import tacosdedatos_utils as tdd

tdd.crear_proyecto(nombre = "proyecto-de-analisis-de-datos")

tdd.arbol("proyecto-de-analisis-de-datos/")
>>>> + proyecto-de-analisis-de-datos
        + AUTORES.md
        + README.md
        + datos
            + brutos
            + externos
            + finales
            + interinos
            + procesados
        + docs
        + notebooks
        + reportes
            + figuras
        + src
            + apps
            + datos
            + externos
            + herramientas
            + modelos
            + visualizaciones
```
que también funciona desde tu línea de comandos.

![GIF mostrando como usar la linea de comandos con tacosdedatos-utils](https://github.com/chekos/pics_for_github/blob/master/2020-06-17%2014.06.39.gif?raw=true)
