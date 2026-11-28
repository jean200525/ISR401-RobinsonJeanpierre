# TA-IND-02 — Instrucciones de compilación

Archivo principal: `main.tex`. Compilador probado en esta máquina: MiKTeX-pdfTeX 4.23 (MiKTeX 25.12).

## Secuencia completa

Desde la carpeta `TA-IND-02/`:

```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

El resultado es `main.pdf`. La secuencia debe ejecutarse completa porque las referencias cruzadas de las tablas y la bibliografía se resuelven en la última pasada.

## Dependencias

Paquetes LaTeX usados: `inputenc`, `fontenc`, `lmodern`, `babel` con la opción `spanish`, `geometry`, `booktabs`, `graphicx`, `longtable`, `float` y `hyperref`. La bibliografía usa el estilo `IEEEtran` y el archivo `referencias.bib`.

Si tu sistema no trae el idioma español de `babel`, ese es un problema de la instalación local, no del repositorio: instala el paquete `babel-spañol` o compila en una distribución que lo incluya. No se ha eliminado `babel` del repositorio para ocultar ese fallo.

## Datos y scripts

- `datos/moscow.csv`: fuente de la tabla de requisitos.
- `datos/generar_tabla_requisitos.ps1`: regenera `secciones/tabla_requisitos.tex` desde `moscow.csv`.
- `datos/calcular_tres_rhos.ps1`: versión ejecutada en PowerShell 5; produce `datos/tres_rhos.csv`.
- `datos/calcular_tres_rhos.py`, `datos/calcular_spearman.py` y `datos/clasificar_kano.py`: equivalentes en Python 3 con biblioteca estándar.

Para regenerar la tabla en Windows:

```powershell
powershell -ExecutionPolicy Bypass -File datos/generar_tabla_requisitos.ps1
```

Python 3 no estaba instalado en el equipo de trabajo; por eso los rho publicados se generaron con el script de PowerShell y luego se comprobó que el script de Python produce el mismo esquema de salida.

## Evidencia

Los originales firmados y los instrumentos se custodian en la carpeta institucional privada `@uteq.edu.ec`, compartida con el docente responsable. En el repositorio público solo se publican códigos, fechas y huellas SHA-256 en `evidencias/MANIFIESTO.md`; no se publican nombres, cédulas, firmas, rostros ni teléfonos.

## Comprobación mínima

Tras compilar, verificar en `main.log`:

- 0 errores (`!`).
- 0 advertencias `Overfull` y 0 referencias `Undefined`.
- La bibliografía contiene cuatro entradas citadas.
- `main.pdf` tiene al menos 6 páginas.

El PDF de una página para el SGA se mantiene en `entrega-sga.pdf` y se compila por separado con `entrega-sga.tex`.
