#!/usr/bin/env python3
"""Calcula rho de Spearman entre MoSCoW y la votacion ponderada.

Entradas:
  moscow.csv   -> requisito,moscow (M=4, S=3, C=2, W=1)
  votacion.csv -> participante,requisito,puntos

Usa rangos promediados para los empates y Pearson sobre esos rangos.
Valida que cada votante sume exactamente 100 puntos.
No modifica los CSV de entrada.
"""
import csv
import math
from pathlib import Path

BASE = Path(__file__).resolve().parent
MOSCOW = BASE / "moscow.csv"
VOTACION = BASE / "votacion.csv"
VALOR = {"M": 4, "S": 3, "C": 2, "W": 1}


def leer(ruta):
    with open(ruta, encoding="utf-8", newline="") as archivo:
        return list(csv.DictReader(archivo))


def rangos_promediados(pares):
    """pares: [(clave, valor)]. Devuelve {clave: rango} con empates promediados."""
    orden = sorted(pares, key=lambda par: par[1])
    resultado = {}
    i = 0
    while i < len(orden):
        j = i
        while j + 1 < len(orden) and orden[j + 1][1] == orden[i][1]:
            j += 1
        rango = ((i + 1) + (j + 1)) / 2.0
        for k in range(i, j + 1):
            resultado[orden[k][0]] = rango
        i = j + 1
    return resultado


def main():
    moscow = leer(MOSCOW)
    votos = leer(VOTACION)
    if not moscow or not votos:
        print("Los CSV estan vacios; no hay datos para calcular rho.")
        return

    m = {}
    for fila in moscow:
        categoria = fila["moscow"].strip().upper()
        if categoria not in VALOR:
            raise SystemExit(f"Categoria MoSCoW no valida: {categoria}")
        m[fila["requisito"].strip()] = VALOR[categoria]

    totales = {}
    por_votante = {}
    for fila in votos:
        req = fila["requisito"].strip()
        puntos = int(fila["puntos"])
        if puntos < 0:
            raise SystemExit("Los puntos no pueden ser negativos")
        totales[req] = totales.get(req, 0) + puntos
        votante = fila["participante"].strip()
        por_votante[votante] = por_votante.get(votante, 0) + puntos

    incorrectos = [v for v, s in por_votante.items() if s != 100]
    if incorrectos:
        raise SystemExit(f"Boletas que no suman 100: {', '.join(incorrectos)}")

    ids = sorted(m)
    if set(totales) != set(ids):
        raise SystemExit("Los requisitos de votacion y MoSCoW no coinciden")

    rm = rangos_promediados([(i, m[i]) for i in ids])
    rv = rangos_promediados([(i, totales[i]) for i in ids])
    x = [rm[i] for i in ids]
    y = [rv[i] for i in ids]
    mx = sum(x) / len(x)
    my = sum(y) / len(y)
    numerador = sum((a - mx) * (b - my) for a, b in zip(x, y))
    dx = sum((a - mx) ** 2 for a in x)
    dy = sum((b - my) ** 2 for b in y)
    rho = numerador / math.sqrt(dx * dy)

    print(f"n = {len(ids)}")
    print(f"votantes = {len(por_votante)}")
    print(f"total de puntos = {sum(totales.values())}")
    print(f"rho de Spearman = {rho:.4f}")


if __name__ == "__main__":
    main()
