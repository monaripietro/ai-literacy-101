#!/usr/bin/env python3
"""Segnala i file Markdown la cui verifica è scaduta, in base alla stabilità.

Legge l'intestazione YAML di ogni file .md in docs/ e confronta
`verificato_il` con le soglie di `stabilita`.

Uso:  python3 scripts/check_freshness.py [--oggi AAAA-MM-GG]
"""
import argparse
import datetime as dt
import pathlib
import re
import sys

SOGLIE_GIORNI = {"volatile": 60, "evolutivo": 182, "stabile": 365}
RADICE = pathlib.Path(__file__).resolve().parent.parent


def leggi_intestazione(testo: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---", testo, re.S)
    if not m:
        return {}
    campi = {}
    for riga in m.group(1).splitlines():
        if ":" in riga:
            chiave, valore = riga.split(":", 1)
            campi[chiave.strip()] = valore.strip()
    return campi


def stabilita_principale(valore: str) -> str:
    for livello in ("volatile", "evolutivo", "stabile"):
        if valore.startswith(livello):
            return livello
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--oggi", help="data di riferimento AAAA-MM-GG")
    args = parser.parse_args()
    oggi = dt.date.fromisoformat(args.oggi) if args.oggi else dt.date.today()

    scaduti, senza_data = [], []
    for percorso in sorted((RADICE / "docs").rglob("*.md")):
        if percorso.name.startswith("_"):
            continue
        campi = leggi_intestazione(percorso.read_text(encoding="utf-8"))
        livello = stabilita_principale(campi.get("stabilita", ""))
        data = campi.get("verificato_il", "")
        rel = percorso.relative_to(RADICE)
        if not livello:
            continue
        try:
            verificato = dt.date.fromisoformat(data)
        except ValueError:
            senza_data.append(str(rel))
            continue
        eta = (oggi - verificato).days
        if eta > SOGLIE_GIORNI[livello]:
            scaduti.append((eta - SOGLIE_GIORNI[livello], livello, str(rel), data))

    if scaduti:
        print(f"Da riverificare al {oggi}:")
        for ritardo, livello, rel, data in sorted(scaduti, reverse=True):
            print(f"  [{livello:9}] {rel}  (verificato il {data}, scaduto da {ritardo} giorni)")
    else:
        print(f"Tutto in regola al {oggi}.")
    if senza_data:
        print("\nSenza data di verifica valida:")
        for rel in senza_data:
            print(f"  {rel}")
    return 1 if scaduti else 0


if __name__ == "__main__":
    sys.exit(main())
