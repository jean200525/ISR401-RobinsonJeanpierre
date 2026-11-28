# Instrumentos en blanco de TA-IND-02

Los archivos de esta carpeta son plantillas vacías. El autor las aplica a las personas participantes; la IA solo las transcribió a LaTeX y compiló los PDF.

- `entrevista_ta_ind_02.pdf`: 20 preguntas de entrevista sobre el funcionamiento actual y el sistema propuesto.
- `cuestionario_kano_ta_ind_02.pdf`: 8 características con su pregunta funcional y disfuncional.
- Códigos acordados: `P1`–`P5` para Kano y `V1`–`V3` para votación, según el consentimiento `TA-IND-02-CONS`.
- Opciones Kano: A = Me gusta, B = Espero que sea así, C = Me resulta indiferente, D = Puedo aceptarlo, E = No me gusta.

## Transcripción

- `datos/kano_respuestas.csv`: una fila por participante y característica (`5 × 8 = 40` pares, es decir 80 respuestas). Columnas: `participante,caracteristica,respuesta_funcional,respuesta_disfuncional`.
- `datos/votacion.csv`: 20 filas por votante, con enteros no negativos que suman exactamente 100. Columnas: `participante,requisito,puntos`.
- `datos/moscow.csv`: una fila por requisito con tipo, enunciado, criterio de verificación, horas, MoSCoW y justificación.
- `datos/kano_caracteristicas.csv`: las 8 características del cuestionario; la columna `requisito_relacionado` se completa cuando el autor define los 20 requisitos.

No se llenan respuestas, votos ni requisitos por adelantado.
