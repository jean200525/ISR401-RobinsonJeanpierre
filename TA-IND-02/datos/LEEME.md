# Formato de los datos de TA-IND-02

`kano_respuestas.csv` ya contiene las 40 filas transcritas de los cinco cuestionarios corregidos `P1`–`P5`; sus huellas están en `../evidencias/MANIFIESTO.md`. `moscow.csv` contiene los 20 requisitos entregados por el autor (12 funcionales y 8 de calidad) con MoSCoW en `M`/`S`/`C`/`W`. Solo `votacion.csv` sigue vacío a la espera de las boletas `V1`–`V3`. La IA solo preparó las plantillas, transcribió los datos y escribió los scripts; no generó participantes, respuestas, requisitos ni votos.

## Códigos

- Cuestionario Kano y entrevista: `P1`–`P5`, según el consentimiento `TA-IND-02-CONS`.
- Votación ponderada: `V1`–`V3`, según el mismo consentimiento.
- La correspondencia entre Participantes y votantes se documentará en el manifiesto cuando se reciban los originales.

## Archivos

- `kano_caracteristicas.csv`: 8 características Kano con pregunta funcional y disfuncional, enlazadas a `R01`–`R20` por correspondencia literal de sus enunciados.
- `kano_respuestas.csv`: una fila por participante y característica (`5 × 8 = 40` pares, 80 respuestas), transcrita de los PDF corregidos. Columnas: `participante,caracteristica,respuesta_funcional,respuesta_disfuncional`. Las etiquetas son las literales de las opciones: `me gusta`, `espero que sea así`, `me resulta indiferente`, `puedo aceptarlo`, `no me gusta`.
- `moscow.csv`: 20 filas, una por requisito. Columnas: `requisito,tipo,enunciado,criterio_verificacion,horas,moscow,justificacion`. MoSCoW usa `M`, `S`, `C` o `W` (11 `M`/66 h, 7 `S`/40 h, 1 `C`/4 h, 1 `W`/4 h). `R09` bajó a `S` y `R12` pasó a `W` para que los Must no superen el 60 % del esfuerzo y para dejar constancia de lo que queda fuera de la versión 1.
- `votacion.csv`: 20 filas por votante, con enteros no negativos. Cada votante debe sumar exactamente 100.
- `.gitattributes` conserva los CSV con saltos LF para que las huellas SHA-256 sean reproducibles.

## Scripts

- `clasificar_kano.py`: aplica la tabla de evaluación a `kano_respuestas.csv`, escribe `kano_clasificado.csv` e imprime el conteo por característica. No decide desempates.
- `calcular_spearman.py`: convierte MoSCoW en 4/3/2/1, promedia rangos empatados y calcula Pearson sobre esos rangos. Valida que cada boleta sume 100.

Ejecución (Python 3, biblioteca estándar):

```bash
python datos/clasificar_kano.py
python datos/calcular_spearman.py
```
