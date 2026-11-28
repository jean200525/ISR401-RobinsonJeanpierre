#!/usr/bin/env python3
"""Calcula los rho de Spearman de TA-IND-02 sobre los mismos requisitos.

Entradas (UTF-8): moscow.csv, kano_caracteristicas.csv, kano_respuestas.csv,
votacion.csv. Salida: tres_rhos.csv. Solo usa la biblioteca estandar.

Los rangos se promedian en caso de empate y el rho se calcula como
correlacion de Pearson sobre esos rangos. El programa se detiene si alguna
boleta no suma exactamente 100 puntos.
"""
import csv
import math
import os

BASE = os.path.dirname(os.path.abspath(__file__))


def leer(nombre):
    with open(os.path.join(BASE, nombre), encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def rangos(pares):
    """pares: iterable de (clave, valor) -> dict clave -> rango promediado."""
    orden = sorted(pares, key=lambda p: p[1])
    salida = {}
    i = 0
    while i < len(orden):
        j = i
        while j + 1 < len(orden) and orden[j + 1][1] == orden[i][1]:
            j += 1
        r = ((i + 1) + (j + 1)) / 2.0
        for k in range(i, j + 1):
            salida[orden[k][0]] = r
        i = j + 1
    return salida


def rho(x, y):
    mx = sum(x) / len(x)
    my = sum(y) / len(y)
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    dx = sum((a - mx) ** 2 for a in x)
    dy = sum((b - my) ** 2 for b in y)
    return num / math.sqrt(dx * dy)


moscow = {f["requisito"]: {"M": 4, "S": 3, "C": 2, "W": 1}[f["moscow"]]
          for f in leer("moscow.csv")}

votos = {}
sumas = {}
for fila in leer("votacion.csv"):
    req = fila["requisito"]
    puntos = int(fila["puntos"])
    votos[req] = votos.get(req, 0) + puntos
    nombre = fila["participante"]
    sumas[nombre] = sumas.get(nombre, 0) + puntos

if set(sumas.values()) != {100}:
    raise ValueError("Cada votante debe sumar 100; se obtuvo %r" % sumas)

# Tabla de evaluacion Kano: fila = respuesta funcional, columna = disfuncional.
TABLA = [
    ["Q", "A", "A", "A", "O"],
    ["R", "I", "I", "I", "M"],
    ["R", "I", "I", "I", "M"],
    ["R", "I", "I", "I", "M"],
    ["R", "R", "R", "R", "Q"],
]
INDICE = {
    "me gusta": 0,
    "espero que sea así": 1,
    "me resulta indiferente": 2,
    "puedo aceptarlo": 3,
    "no me gusta": 4,
}

conteo = {}
for fila in leer("kano_respuestas.csv"):
    ch = fila["caracteristica"]
    conteo.setdefault(ch, dict.fromkeys("AIMSORQ", 0))
    cat = TABLA[INDICE[fila["respuesta_funcional"]]][
        INDICE[fila["respuesta_disfuncional"]]
    ]
    conteo[ch][cat] += 1

better = {}
for fila in leer("kano_caracteristicas.csv"):
    c = conteo[fila["id"]]
    better[fila["requisito_relacionado"]] = (c["A"] + c["O"]) / 5.0

ids20 = sorted(moscow)
rm20 = rangos((i, moscow[i]) for i in ids20)
rv20 = rangos((i, votos[i]) for i in ids20)
rho20 = rho([rm20[i] for i in ids20], [rv20[i] for i in ids20])

comunes = sorted(better)
rm = rangos((i, moscow[i]) for i in comunes)
rv = rangos((i, votos[i]) for i in comunes)
rk = rangos((i, better[i]) for i in comunes)

resultados = [
    ("MoSCoW-voto (20 requisitos)", len(ids20), rho20),
    ("MoSCoW-Kano (8 enlazados)", len(comunes),
     rho([rm[i] for i in comunes], [rk[i] for i in comunes])),
    ("MoSCoW-voto (8 enlazados)", len(comunes),
     rho([rm[i] for i in comunes], [rv[i] for i in comunes])),
    ("Kano-voto (8 enlazados)", len(comunes),
     rho([rk[i] for i in comunes], [rv[i] for i in comunes])),
]

with open(os.path.join(BASE, "tres_rhos.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["comparacion", "n", "rho"])
    for nombre, n, valor in resultados:
        w.writerow([nombre, n, f"{valor:.4f}"])

for nombre, n, valor in resultados:
    print(f"{nombre} (n={n}): {valor:.4f}")
