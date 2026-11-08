# TA-IND-01 — IEEE 29148 y tipos de requisitos de un sistema conocido

Actividad sumativa individual de **Ingeniería de Requerimientos (ISR-401)**,
Facultad de Ciencias de la Computación, Universidad Técnica Estatal de Quevedo.

- **Estudiante:** Jeanpierre Robinson Espinoza — código 1722574223
- **Sistema analizado:** aplicación de transporte (Uber / InDrive)
- **Fecha límite:** sábado 7 de noviembre de 2026, 23:59

## Contenido de esta carpeta

```
TA-IND-01/
├── main.tex              Archivo principal del informe
├── referencias.bib       Bibliografía IEEE (biber)
├── main.pdf              PDF compilado
├── entrega-sga.tex       Hoja de datos informativos para el SGA
├── entrega-sga.pdf       PDF de una sola página para el SGA
└── figuras/              Capturas propias del sistema (mínimo 3)
```

## Compilación

Compilador **pdfLaTeX** (MiKTeX 25.12) con **Biber**. Desde esta carpeta:

```
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Con `latexmk`:

```
latexmk -pdf main.tex
```

Para la hoja del SGA:

```
pdflatex entrega-sga.tex
```

En Overleaf: compilador *pdfLaTeX*, bibliografía *Biber*, archivo principal
`main.tex`.

## Dependencias

`babel-spanish`, `lmodern`, `geometry`, `microtype`, `graphicx`, `booktabs`,
`longtable`, `array`, `tabularx`, `enumitem`, `xcolor`, `csquotes`,
`caption`, `hyperref`, `biblatex` (estilo `ieee`). MiKTeX las instala
automáticamente.

## Figuras

Las capturas deben ser propias y guardarse en `figuras/` como
`captura-01.png`, `captura-02.png` y `captura-03.png`. El documento compila
aunque falten (muestra un recuadro rojo de advertencia que debe desaparecer
antes de la entrega).

## Declaración de uso de IA

La infraestructura LaTeX de esta carpeta (estructura del documento,
`README.md`, plantilla de referencias, compilación) se elaboró con apoyo de un
asistente de IA. El contenido evaluable es de autoría del estudiante y se
declara en la sección correspondiente de `main.tex`.
