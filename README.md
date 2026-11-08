# ISR401 -- Jeanpierre Robinson Espinoza

Repositorio personal de la asignatura **Ingeniería de Requerimientos (ISR-401)**, Facultad de Ciencias de la Computación, Carrera de Software, Universidad Técnica Estatal de Quevedo.

## Contenido

| Ruta | Descripción |
|---|---|
| `FORM-TL-01/main.tex` | Fuente LaTeX de la actividad formativa FORM-TL-01. |
| `FORM-TL-01/main.pdf` | PDF compilado de FORM-TL-01. |
| `FORM-TL-01/main.bib` | Entradas bibliográficas de referencia (espejo de la bibliografía del documento). |
| `SGA/datos_informativos.tex` | Fuente del PDF de una sola página para el SGA. |
| `SGA/datos_informativos.pdf` | PDF de una sola página con los datos informativos y la URL del repositorio. |

## Requisitos

- Una distribución LaTeX con `pdflatex` (TeX Live 2023 o superior, o MiKTeX 23 o superior).
- Paquetes: `inputenc`, `fontenc`, `babel-spanish`, `geometry`, `amsmath`, `amssymb`, `longtable`, `booktabs`, `array`, `xcolor`, `enumitem`, `hyperref`.

En una instalación mínima (TinyTeX) se pueden instalar con:

```bash
tlmgr install babel-spanish geometry amsmath longtable booktabs xcolor enumitem hyperref
```

## Compilación del documento principal

El archivo principal es `FORM-TL-01/main.tex`. La bibliografía está incluida con `thebibliography` para que el PDF se regenere sin depender de BibTeX.

```bash
cd FORM-TL-01
pdflatex main.tex
pdflatex main.tex
```

El resultado es `FORM-TL-01/main.pdf`. La segunda pasada actualiza referencias cruzadas y enlaces.

## Compilación del PDF del SGA

```bash
cd SGA
pdflatex datos_informativos.tex
pdflatex datos_informativos.tex
```

El resultado es `SGA/datos_informativos.pdf`, que debe tener **una sola página**.

## Repositorio

URL pública: <https://github.com/jean200525/ISR401-RobinsonJeanpierre>
