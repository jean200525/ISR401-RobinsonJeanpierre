#!/usr/bin/env python3
"""Clasifica respuestas Kano con la tabla de evaluacion estandar.

Entrada: kano_respuestas.csv
  participante,caracteristica,respuesta_funcional,respuesta_disfuncional
Salida: kano_clasificado.csv (mismas columnas + categoria) y resumen por caracteristica.

No modifica el CSV de entrada y no decide empates: solo cuenta categorias.
"""
import csv
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent
ENTRADA = BASE / "kano_respuestas.csv"
SALIDA = BASE / "kano_clasificado.csv"

NOMBRES = ["me gusta", "debe ser así", "me da igual", "lo tolero", "no me gusta"]
ALIAS = {
    "a": 0, "me gusta": 0,
    "b": 1, "debe ser así": 1, "espero que sea así": 1,
    "c": 2, "me da igual": 2, "me resulta indiferente": 2,
    "d": 3, "lo tolero": 3, "puedo aceptarlo": 3,
    "e": 4, "no me gusta": 4,
}

# Filas = respuesta funcional, columnas = respuesta disfuncional.
# A: atractiva, I: indiferente, M: basicidad, O: desempeño, R: reversa, Q: cuestionable.
TABLA = [
    ["Q", "A", "A", "A", "O"],
    ["R", "I", "I", "I", "M"],
    ["R", "I", "I", "I", "M"],
    ["R", "I", "I", "I", "M"],
    ["R", "R", "R", "R", "Q"],
]


def indice(texto):
    clave = " ".join(texto.strip().lower().split())
    if clave not in ALIAS:
        raise SystemExit(f"Respuesta no valida: {texto!r}")
    return ALIAS[clave]


def main():
    with open(ENTRADA, encoding="utf-8", newline="") as archivo:
        filas = list(csv.DictReader(archivo))
    if not filas:
        print("El CSV de respuestas esta vacio; no hay datos para clasificar.")
        return

    campos = list(filas[0].keys()) + ["categoria"]
    conteo = defaultdict(Counter)
    salida = []
    for fila in filas:
        f = indice(fila["respuesta_funcional"])
        d = indice(fila["respuesta_disfuncional"])
        categoria = TABLA[f][d]
        nueva = dict(fila)
        nueva["categoria"] = categoria
        salida.append(nueva)
        conteo[fila["caracteristica"]][categoria] += 1

    with open(SALIDA, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(salida)

    for caracteristica in sorted(conteo):
        resumen = ", ".join(f"{k}={v}" for k, v in sorted(conteo[caracteristica].items()))
        print(f"{caracteristica}: {resumen}")
    print(f"Filas clasificadas: {len(salida)} -> {SALIDA.name}")


if __name__ == "__main__":
    main()
