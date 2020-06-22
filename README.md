# tacosdedatos-utils

<div align="center">

[![PyPI version](https://badge.fury.io/py/tacosdedatos-utils.svg)](https://badge.fury.io/py/tacosdedatos-utils)
[![Documentation Status](https://readthedocs.org/projects/tacosdedatos-utils/badge/?version=latest)](https://tacosdedatos-utils.readthedocs.io/es/latest/?badge=latest)
[![Build status](https://github.com/tacosdedatos/tacosdedatos-utils/workflows/build/badge.svg?branch=master&event=push)](https://github.com/tacosdedatos/tacosdedatos-utils/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/tacosdedatos-utils.svg)](https://pypi.org/project/tacosdedatos-utils/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/tacosdedatos/tacosdedatos-utils/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/tacosdedatos/tacosdedatos-utils/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/tacosdedatos/tacosdedatos-utils/releases)
[![License](https://img.shields.io/github/license/tacosdedatos/tacosdedatos-utils)](https://github.com/tacosdedatos/tacosdedatos-utils/blob/master/LICENSE)

Una coleccion de herramientas para facilitar el analisis y visualizacion de datos por @tacosdedatos.
</div>

Que trae
--------
* la función `arbol` para mostrar los contenidos de la carpeta que le pases.
```python
from tacosdedatos_utils.file_management import arbol

arbol("./notebooks")
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
from tacosdedatos_utils.project_management import crear_proyecto
from tacosdedatos_utils.file_management import arbol

crear_proyecto(nombre = "proyecto-de-analisis-de-datos")

arbol("proyecto-de-analisis-de-datos/")
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


## 📃 Citeishon

```
@misc{tacosdedatos-utils,
  author = {tacosdedatos},
  title = {Una coleccion de herramientas para facilitar el analisis y visualizacion de datos por @tacosdedatos.},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/tacosdedatos/tacosdedatos-utils}}
}
```

## Créditos

Este proyecto fue generado con [`python-package-template`](https://github.com/TezRomacH/python-package-template).
