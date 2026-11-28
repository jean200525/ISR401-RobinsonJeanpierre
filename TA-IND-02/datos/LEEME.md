# Formato de los datos de TA-IND-02

`kano_respuestas.csv` ya contiene las 40 filas transcritas de los cinco cuestionarios corregidos `P1`–`P5`; sus huellas están en `../evidencias/MANIFIESTO.md`. `moscow.csv` contiene los 20 requisitos entregados por el autor (12 funcionales y 8 de calidad) con MoSCoW en `M`/`S`/`C`/`W`; los enunciados de `R12`, `R13`, `R14` y `R19` se restauraron al texto votado de `formatos/boleta_votacion_R01-R20.tex` para conservar la trazabilidad con las boletas y el cuestionario Kano; solo cambiaron la clase MoSCoW, la justificación y el criterio verificable, sin modificar IDs, tipos ni horas. `votacion.csv` contiene 60 filas (3 votantes x 20 requisitos), transcritas de las boletas conservadas como imagen `V1.jpeg` a `V3.jpeg`. Inicialmente se bajó `R20` de 3 a 2 en `V1` y `R16` de 4 a 3 en `V3` por confirmación de chat; después `V1` y `V3` declararon por separado cada corrección con fecha `27/11/2026` y se recibieron boletas corregidas con esa fecha. El archivo quedó **validado** con esos valores; la secuencia se documenta en `../evidencias/MANIFIESTO.md`. El autor preparó y verificó las plantillas, los esquemas, los CSV y los scripts; la IA solo apoyó en la revisión ortográfica y en errores de compilación, sin generar participantes, respuestas, requisitos ni votos.

## Códigos

- Cuestionario Kano y entrevista: `P1`–`P5`, según el consentimiento `TA-IND-02-CONS`.
- Votación ponderada: `V1`–`V3`, según el mismo consentimiento.
- Los ocho consentimientos manuscritos se custodian en la carpeta institucional privada `@uteq.edu.ec`, compartida con el docente; en el manifiesto solo se publican código, perfil genérico, fecha y SHA-256, sin nombres ni cédulas.

## Archivos

- `kano_caracteristicas.csv`: 8 características Kano con pregunta funcional y disfuncional, enlazadas a `R01`–`R20` por correspondencia literal de sus enunciados.
- `kano_respuestas.csv`: una fila por participante y característica (`5 × 8 = 40` pares, 80 respuestas), transcrita de los PDF corregidos. Columnas: `participante,caracteristica,respuesta_funcional,respuesta_disfuncional`. Las etiquetas son las literales de las opciones: `me gusta`, `espero que sea así`, `me resulta indiferente`, `puedo aceptarlo`, `no me gusta`.
- `moscow.csv`: 20 filas, una por requisito. Columnas: `requisito,tipo,enunciado,criterio_verificacion,horas,moscow,justificacion`. MoSCoW usa `M`, `S`, `C` o `W` (11 `M`/66 h, 7 `S`/40 h, 1 `C`/4 h, 1 `W`/4 h). `R09` bajó a `S` y `R12` pasó a `W` para que los Must no superen el 60 % del esfuerzo y para dejar constancia de lo que queda fuera de la versión 1.
- `votacion.csv`: 20 filas por votante, con enteros no negativos. Cada votante suma exactamente 100 con las correcciones declaradas por `V1` y `V3` y las boletas fechadas `27/11/2026`.
- `.gitattributes` conserva los CSV con saltos LF para que las huellas SHA-256 sean reproducibles.

## Scripts

- `clasificar_kano.py`: aplica la tabla de evaluación a `kano_respuestas.csv`, escribe `kano_clasificado.csv` e imprime el conteo por característica. No decide desempates.
- `calcular_spearman.py`: convierte MoSCoW en 4/3/2/1, promedia rangos empatados y calcula Pearson sobre esos rangos. Valida que cada boleta sume 100.
- `calcular_tres_rhos.py`: calcula los cuatro rho del trabajo (20 y 8 requisitos) con rangos promediados y escribe `tres_rhos.csv`. Valida que cada boleta sume 100. Es el equivalente de `calcular_tres_rhos.ps1` y usa solo biblioteca estándar.
- `calcular_tres_rhos.ps1`: versión en PowerShell 5 del script anterior. Se ejecutó en el equipo de trabajo porque Python 3 no estaba instalado; produce el mismo `tres_rhos.csv`.
- `generar_tabla_requisitos.ps1`: regenera `../secciones/tabla_requisitos.tex` desde `moscow.csv`, con ID, tipo, enunciado, clase MoSCoW, horas, justificación y criterio de verificación.

Ejecución con Python 3 (biblioteca estándar):

```bash
python datos/clasificar_kano.py
python datos/calcular_spearman.py
python datos/calcular_tres_rhos.py
```

Ejecución alternativa usada en el equipo (PowerShell 5):

```powershell
powershell -ExecutionPolicy Bypass -File datos/calcular_tres_rhos.ps1
powershell -ExecutionPolicy Bypass -File datos/generar_tabla_requisitos.ps1
```
