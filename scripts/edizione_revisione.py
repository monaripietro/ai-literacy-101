#!/usr/bin/env python3
"""Genera l'edizione di revisione: un unico documento lineare (.md + .docx)
con tutti i contenuti concettuali del sito, nell'ordine in cui si leggono.

Ogni modulo è seguito dalle sue attività e dai suoi schemi, così un concetto
si rivede una volta sola, nel suo contesto. Link, sezioni "Collegamenti" e
diagrammi Mermaid sono rimossi: qui conta il testo.

Uso:  python3 scripts/edizione_revisione.py   → revisione/edizione-revisione.{md,docx}
La cartella revisione/ è privata (gitignored).
"""
import datetime, glob, os, re, subprocess
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
OUT = os.path.join(ROOT, "revisione")

SCHEMI_EXTRA = {"M07": ["schemi/app-intorno-al-modello.md"]}


def load(rel):
    t = open(os.path.join(DOCS, rel), encoding="utf-8").read()
    meta = {}
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    if m:
        meta = yaml.safe_load(m.group(1)) or {}
        t = t[m.end():]
    return meta, t


def clean(t, shift=1):
    # via la sezione Collegamenti (logica dei link: si rivede a parte)
    t = re.sub(r"\n## Collegamenti\n.*?(?=\n## |\Z)", "\n", t, flags=re.S)
    # mermaid → segnaposto
    t = re.sub(r"```mermaid\n.*?```", "*[Diagramma: vedi sito]*", t, flags=re.S)
    # immagini → segnaposto
    t = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"*[Immagine: \1]*", t)
    # link → solo testo
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    # abbassa i titoli di `shift` livelli
    t = re.sub(r"^(#{1,5}) ", lambda m: "#" * min(len(m.group(1)) + shift, 6) + " ", t, flags=re.M)
    return t.strip()


def blocco(rel, shift=1):
    meta, t = load(rel)
    info = [f"`{rel}`"]
    for k in ("stato", "stabilita", "verificato_il", "durata", "durata_indicativa"):
        if meta.get(k):
            info.append(f"{k}: {meta[k]}")
    t = clean(t, shift)
    lines = t.split("\n", 1)
    head = lines[0]
    body = lines[1] if len(lines) > 1 else ""
    return f"{head}\n\n*Fonte: {' · '.join(info)}*\n\n{body.strip()}\n"


def main():
    os.makedirs(OUT, exist_ok=True)
    oggi = datetime.date.today().isoformat()
    parti = [f"""---
title: "AI literacy 101 — edizione di revisione"
subtitle: "Generata il {oggi}"
---

# Come usare questo documento

Contiene tutto il testo concettuale del sito, in ordine di lettura. Segue l'ordine del sito: ogni nucleo contiene già attività e schemi. Sotto ogni titolo c'è il file di origine: serve a riportare le correzioni nel repo.

Esclusi: strumenti, prompt, report di manutenzione, diagrammi.

Commenta direttamente sul testo. Tre etichette bastano:

- **CHIARIRE**: il concetto è giusto ma detto male o in modo vago.
- **SBAGLIATO**: il contenuto è errato o non è quello che faccio.
- **TAGLIA**: ripetuto, superfluo o non mio.

Tutto il resto, commento libero.
"""]

    nav = yaml.safe_load(re.sub(r"!!python/name:\S+", "''", open(os.path.join(ROOT, "mkdocs.yml"), encoding="utf-8").read()))["nav"]
    escludi = {"manutenzione.md", "strumenti.md"}

    def visita(voci, livello):
        for v in voci:
            for nome, val in v.items():
                if isinstance(val, list):
                    parti.append("#" * livello + f" {nome}\n")
                    visita(val, livello + 1)
                elif val not in escludi:
                    parti.append(blocco(val, shift=livello))
    visita(nav, 1)

    md = "\n\n".join(parti)
    md_path = os.path.join(OUT, "edizione-revisione.md")
    open(md_path, "w", encoding="utf-8").write(md)
    subprocess.run(["pandoc", md_path, "-o", os.path.join(OUT, "edizione-revisione.docx"), "--toc", "--toc-depth=2"], check=True)
    print("scritto", md_path, "e .docx;", len(md.split()), "parole")


if __name__ == "__main__":
    main()
