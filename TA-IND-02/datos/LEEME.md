# Formato de los datos de TA-IND-02

Los CSV están vacíos a la espera de los datos reales que tabule el autor. La IA solo preparó las plantillas y los scripts; no generó participantes, respuestas ni votos.

## Códigos

- Cuestionario Kano y entrevista: `P1`–`P5`, según el consentimiento `TA-IND-02-CONS`.
- Votación ponderada: `V1`–`V3`, según el mismo consentimiento.
- La correspondencia entre Participantes y votantes se documentará en el manifiesto cuando se reciban los originales.

## Archivos

- `kano_caracteristicas.csv`: 8 características Kano con pregunta funcional y disfuncional. La columna `requisito_relacionado` se completa cuando el autor defina `R01`–`R20`.
- `kano_respuestas.csv`: una fila por participante y característica (`5 × 8 = 40` pares, 80 respuestas). Columnas: `participante,caracteristica,respuesta_funcional,respuesta_disfuncional`.
- `moscow.csv`: una fila por requisito. Columnas: `requisito,tipo,enunciado,criterio_verificacion,horas,moscow,justificacion`. MoSCoW usa `M`, `S`, `C` o `W`.
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
