# Manifiesto de evidencia (sin datos personales)

La carpeta `evidencias/` está ignorada por Git, salvo este archivo. Los originales se custodian fuera del repositorio; no se publican nombres, cédulas, correos, firmas, rostros, voces ni audios. Las duraciones y fechas no se estiman si no constan en el original.

| Código | Técnica | Archivo custodiado | Fecha | Duración | SHA-256 |
|---|---|---|---|---|---|
| --- | Consentimiento | `consentimiento_TA-IND-02.pdf` | 2026-11-27 (versión del documento) | No registrada | `A092B68DE048D5CD92E9F55AC0285BBAEE1747267FA359EE7A2DA8A8D3FD6007` |
| --- | Paquete de originales | `Cuestionarios_veterinaria_P1-P5_corregidos.zip` | No consta en el original | No registrada | `462715D6B82422815CEE73B39CEB445921361564ABA2348C07973CE285AEAFF3` |
| --- | Fuente de requisitos | `Downloads/moscow.csv` (original entregado) | 2026-11-28 (archivo entregado) | No aplica | `6B7482405C3D8F933738D135CF0E07A33DB87A8247A409508F67D46AA1F80A17` |
| --- | Fuente de requisitos | `Downloads/moscow_requisitos.xlsx` (original entregado) | 2026-11-28 (archivo entregado) | No aplica | `E221E6F037EE5AB407A159699F749FA818D5A8ACA60E258EC719FED498D4EBC8` |
| --- | Datos adaptados | `TA-IND-02/datos/moscow.csv` (versión corregida) | 2026-11-28 (revisión) | No aplica | `F2954660AC885804FB0469B363C1F03040BDB0A60469E94E4DAB62BA5435F424` |
| P1 | Entrevista y Kano | `P1_entrevista_y_kano.pdf` | No consta en el original | No registrada | `B30BF9728DD9460FDB5B58AEC4E4FD793A281EB73BAD5E2616677E5ABE21A3FE` |
| P2 | Entrevista y Kano | `P2_entrevista_y_kano.pdf` | No consta en el original | No registrada | `145060719CC97CDA42AC6A14064C1CA8BC76DBF2E7D33F54B1568299E2DC09D8` |
| P3 | Entrevista y Kano | `P3_entrevista_y_kano.pdf` | No consta en el original | No registrada | `E418D76E5E7E6021EDADB6B777F1183ACE09A2BD308A178186F0DD08B9C2B294` |
| P4 | Entrevista y Kano | `P4_entrevista_y_kano.pdf` | No consta en el original | No registrada | `48B110710A82F34C638A00E4810182EA5712B4729A03B5D9A75D58F1956939DB` |
| P5 | Entrevista y Kano | `P5_entrevista_y_kano.pdf` | No consta en el original | No registrada | `CE63C7BCB4B1270D9C654F6276003262A49A398CBADDE5CC50B827D77A5D4B44` |

Los códigos acordados son `P1`–`P5` para la entrevista y el cuestionario Kano, y `V1`–`V3` para la votación ponderada, conforme al consentimiento `TA-IND-02-CONS`. El autor confirmó que las cinco respuestas Kano son de personas reales. Las 40 filas de `../datos/kano_respuestas.csv` se transcribieron de los cinco PDF anteriores (80 respuestas). Los 20 requisitos de `../datos/moscow.csv` se transcribieron de los dos originales de Downloads, que coinciden en ID, tipo, horas y clasificación; la IA solo adaptó el esquema, convirtió `Must`/`Should`/`Could` a `M`/`S`/`C` y aplicó las correcciones autorizadas por el autor. Por eso la huella del archivo adaptado es distinta a la de los originales: ambas se registran arriba con nombres diferentes. No se generaron respuestas ni requisitos.

Observaciones de los originales corregidos, registradas sin alterarlos: usan `P1`–`P5`, no contienen la nota “simulado” ni el código `TA-TAR-02`; el encabezado dice `Trabajo: Priorización de requisitos` (sin el código `TA-IND-02`) y `Estudiante: Robinson Espinoza Jeanpierre`. Las fechas de los participantes aparecen en blanco. El ZIP `cONSENSAU.zip` fue revisado y **no corresponde** a TA-IND-02: sus ocho imágenes coinciden con consentimientos `ENTR-01`…`ENTR-15` de otro estudio; por eso no se registró como evidencia. El formulario `consentimiento_TA-IND-02.pdf` conserva nombre, código y firma en blanco; las huellas de los originales firmados `P1`–`P5` y `V1`–`V3` se añadirán cuando se entreguen los archivos correctos. Las boletas `V1`–`V3` y sus huellas se registrarán aquí cuando el autor las entregue; no se inventa ninguna huella ni voto.
