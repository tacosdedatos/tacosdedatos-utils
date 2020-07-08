# Cómo usar `tacosdedatos_utils`

## `arbol()`

la función `arbol` sirve para mostrar los contenidos de la carpeta que le pases.
```python
import tacosdedatos_utils as tdd

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

## `crear_proyecto()`
la función `crear_proyecto()` sirve para crear el esqueleto de un proyecto de análisis de datos desde tu notebook
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

`crear_proyecto()` también funciona desde la línea de comandos
```shell
tacosdeatos crear --nombre "proyecto-nuevo" --tipo "analisis" --dir "."
```

![GIF mostrando como usar la linea de comandos con tacosdedatos-utils](https://github.com/chekos/pics_for_github/blob/master/2020-06-17%2014.06.39.gif?raw=true)
