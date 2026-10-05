#!/usr/bin/env python3
"""Genera docs/schemi/foglietto.excalidraw: i due lati del "foglietto" (M03).

Modifica i testi qui sotto e rilancia:  python3 scripts/genera_excalidraw.py
Il file si apre su https://excalidraw.com (File → Apri).
"""
import json
import pathlib
import random

random.seed(42)
RADICE = pathlib.Path(__file__).resolve().parent.parent
USCITA = RADICE / "docs" / "schemi" / "foglietto.excalidraw"

FONT_MANO = 1  # Virgil, lo stile "a mano" di Excalidraw
elementi = []


def _base(tipo, x, y, w, h, **extra):
    el = {
        "id": f"{tipo}-{len(elementi)}",
        "type": tipo, "x": x, "y": y, "width": w, "height": h,
        "angle": 0, "strokeColor": extra.pop("stroke", "#1e1e1e"),
        "backgroundColor": extra.pop("bg", "transparent"),
        "fillStyle": "hachure", "strokeWidth": extra.pop("sw", 2),
        "strokeStyle": extra.pop("style", "solid"), "roughness": 1,
        "opacity": 100, "groupIds": [], "frameId": None,
        "roundness": extra.pop("roundness", None),
        "seed": random.randint(1, 2**31), "version": 1,
        "versionNonce": random.randint(1, 2**31), "isDeleted": False,
        "boundElements": [], "updated": 1, "link": None, "locked": False,
    }
    el.update(extra)
    elementi.append(el)
    return el


def testo(x, y, contenuto, size=20, colore="#1e1e1e", align="left"):
    """Un elemento di testo per riga: si legge bene ovunque, anche negli export SVG."""
    for n, riga in enumerate(contenuto.split("\n")):
        _base("text", x, y + n * size * 1.3, len(riga) * size * 0.58, size * 1.6,
              stroke=colore, text=riga, originalText=riga, fontSize=size,
              fontFamily=FONT_MANO, textAlign=align, verticalAlign="top",
              containerId=None, lineHeight=1.25, autoResize=True)


def rettangolo(x, y, w, h, **kw):
    return _base("rectangle", x, y, w, h, roundness={"type": 3}, **kw)


def ellisse(x, y, w, h, **kw):
    return _base("ellipse", x, y, w, h, **kw)


def freccia(x1, y1, x2, y2, **kw):
    return _base("arrow", x1, y1, x2 - x1, y2 - y1,
                 points=[[0, 0], [x2 - x1, y2 - y1]], lastCommittedPoint=None,
                 startBinding=None, endBinding=None, startArrowhead=None,
                 endArrowhead="arrow", roundness={"type": 2}, **kw)


# ---------- LATO A: gli insiemi ----------
# cornice invisibile: tiene margine attorno ai titoli negli export
_base("rectangle", -40, -130, 1820, 840, stroke="transparent")
testo(0, -80, "LATO A · gli insiemi", 28)
ellisse(0, 0, 760, 540, stroke="#1971c2")
testo(200, 40, "INTELLIGENZA ARTIFICIALE\n(informatica, matematica, psicologia,\nfilosofia, etica…)", 20, "#1971c2")
ellisse(90, 140, 580, 370, stroke="#2f9e44")
testo(230, 170, "MACHINE LEARNING\nmacchine che apprendono\nin modo automatico DA ESEMPI", 20, "#2f9e44")
ellisse(180, 280, 400, 210, stroke="#e8590c")
testo(280, 300, "DEEP LEARNING\nreti neurali in\nconfigurazioni complesse", 18, "#e8590c")
ellisse(310, 395, 140, 70, stroke="#9c36b5")
testo(350, 415, "chatbot", 18, "#9c36b5")

# ---------- LATO B: le 6 caselle ----------
OX, OY, W, H, GAP = 900, 0, 250, 200, 50
testo(OX, -80, "LATO B · le due fasi", 28)
testo(OX, OY - 32, "FASE 1 · APPRENDIMENTO (training)", 18, "#1971c2")
caselle_sopra = [
    "1 · DATASET\nla porzione di realtà\nda cui la macchina\napprende",
    "2 · SUPERCOMPUTER\n(con il mantello!)\n+ ALGORITMO di\napprendimento",
    "3 · MODELLO ALLENATO\nuno o più file\npieni di numeri",
]
caselle_sotto = [
    "4 · APPLICAZIONE\nil corpo del modello\n(tablet + dito)",
    "5 · INPUT\ndati nuovi,\nmai visti",
    "6 · OUTPUT\nuna previsione\n(margine d'errore)",
]
Y2 = OY + H + 110
for i, t in enumerate(caselle_sopra):
    x = OX + i * (W + GAP)
    rettangolo(x, OY, W, H, stroke="#1971c2")
    testo(x + 15, OY + 20, t, 18)
    if i < 2:
        freccia(x + W + 8, OY + H / 2, x + W + GAP - 8, OY + H / 2)
for i, t in enumerate(caselle_sotto):
    x = OX + i * (W + GAP)
    rettangolo(x, Y2, W, H, stroke="#2f9e44")
    testo(x + 15, Y2 + 20, t, 18)
testo(OX, Y2 - 32, "FASE 2 · UTILIZZO (deploy)  ← noi stiamo sempre qui", 18, "#2f9e44")
testo(OX + 2 * (W + GAP) + 20, OY + H + 22, "test → messa in produzione", 16, "#868e96")
freccia(OX + 2 * (W + GAP) + W / 2, OY + H + 50, OX + W - 10, Y2 - 55, stroke="#868e96", style="dashed")

documento = {
    "type": "excalidraw", "version": 2,
    "source": "https://github.com/ (AI literacy by Pietro Monari)",
    "elements": elementi,
    "appState": {"viewBackgroundColor": "#ffffff", "gridSize": None},
    "files": {},
}
USCITA.write_text(json.dumps(documento, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Scritto {USCITA.relative_to(RADICE)} con {len(elementi)} elementi")
