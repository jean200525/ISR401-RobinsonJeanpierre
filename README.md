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
| `TA-IND-01/main.tex` | Fuente LaTeX de la actividad TA-IND-01. |
| `TA-IND-01/main.pdf` | PDF compilado de TA-IND-01. |
| `TA-IND-02/main.tex` | Fuente LaTeX del informe de priorización de requisitos, con las siete secciones redactadas. |
| `TA-IND-02/main.pdf` | PDF compilado del informe de priorización de requisitos. |
| `TA-IND-02/entrega-sga.tex` | Fuente del PDF de una sola página para el SGA de TA-IND-02. |
| `TA-IND-02/entrega-sga.pdf` | PDF de una sola página con los datos informativos y la URL del repositorio. |
| `TA-IND-02/secciones/` | Tablas LaTeX generadas desde los CSV reales de requisitos y Kano. |
| `TA-IND-02/referencias.bib` | Entradas bibliográficas verificadas en formato BibTeX, estilo IEEE. |
| `TA-IND-02/formatos/boleta_votacion_R01-R20.pdf` | Boleta con los 20 enunciados finales y puntos en blanco para `V1`–`V3`. |
| `TA-IND-02/formatos/` | Instrumentos en blanco: entrevista, cuestionario Kano y boleta de votación. |
| `TA-IND-02/datos/LEEME.md` | Formato de los CSV, códigos de participantes y uso de los scripts. |
| `TA-IND-02/datos/clasificar_kano.py` | Clasificación de respuestas Kano con la tabla de evaluación. |
| `TA-IND-02/datos/calcular_spearman.py` | Cálculo de rho con rangos promediados y validación de boletas. |
| `TA-IND-02/evidencias/MANIFIESTO.md` | Metadatos de la evidencia custodiada, sin nombres ni datos personales. |

## Requisitos

- Una distribución LaTeX con `pdflatex` (TeX Live 2023 o superior, o MiKTeX 23 o superior).
- Paquetes LaTeX: `inputenc`, `fontenc`, `lmodern`, `babel-spanish`, `geometry`, `amsmath`, `amssymb`, `longtable`, `booktabs`, `array`, `xcolor`, `enumitem`, `graphicx`, `float`, `hyperref`, además de `IEEEtran.bst` (`ieeetran`) para TA-IND-02.

En una instalación mínima (TinyTeX) se pueden instalar con (en `tlmgr`, `longtable`/`array` vienen en `tools` y `graphicx` en `graphics`):

```bash
tlmgr install babel-spanish geometry amsmath tools booktabs xcolor enumitem graphics hyperref lmodern float ieeetran
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

El resultado es `SGA/datos_informativos.pdf`, que debe tener **una sola página**. Para TA-IND-02 se usa además `TA-IND-02/entrega-sga.tex`:

```bash
cd TA-IND-02
pdflatex entrega-sga.tex
pdflatex entrega-sga.tex
```

El resultado es `TA-IND-02/entrega-sga.pdf`, también de una sola página, con la URL del repositorio en una sola línea.

## Compilación de TA-IND-02

El archivo principal es `TA-IND-02/main.tex`. En esta actividad se usa **BibTeX** con el estilo `IEEEtran` y la base `TA-IND-02/referencias.bib` (no se usa `thebibliography`, método empleado solo en FORM-TL-01). Por eso el orden de compilación incluye una pasada de BibTeX:

```bash
cd TA-IND-02
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

El resultado es `TA-IND-02/main.pdf`. Las dos últimas pasadas actualizan las referencias cruzadas y los enlaces. Antes de la entrega final deben haberse agregado las citas `\cite{...}` correspondientes a las obras de `referencias.bib`, y cada entrada debe haberse verificado contra la fuente real.

## Repositorio

URL pública: <https://github.com/jean200525/ISR401-RobinsonJeanpierre>
