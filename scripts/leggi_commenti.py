#!/usr/bin/env python3
"""Estrae i commenti da un .docx di revisione e li associa al file di origine.

Uso:  python3 scripts/leggi_commenti.py revisione/edizione-revisione-commentata.docx
Output: revisione/commenti.md (file d'origine · testo commentato · commento)
"""
import os, re, sys
from docx import Document
from docx.oxml.ns import qn

src = sys.argv[1]
doc = Document(src)
testi = {c.comment_id: c.text for c in doc.comments}

righe, fonte = [], "?"
for p in doc.paragraphs:
    m = re.match(r"Fonte: (\S+)", p.text)
    if m:
        fonte = m.group(1)
    el = p._p
    aperti = {}
    for node in el.iter():
        if node.tag == qn("w:commentRangeStart"):
            aperti[int(node.get(qn("w:id")))] = ""
        elif node.tag == qn("w:t"):
            for k in aperti:
                aperti[k] += node.text or ""
        elif node.tag == qn("w:commentReference"):
            cid = int(node.get(qn("w:id")))
            ancora = aperti.pop(cid, p.text)[:120]
            righe.append((fonte, ancora.strip(), testi.get(cid, "").strip()))

out = os.path.join(os.path.dirname(src), "commenti.md")
with open(out, "w", encoding="utf-8") as f:
    f.write("| # | File | Testo | Commento |\n|---|---|---|---|\n")
    for i, (a, b, c) in enumerate(righe, 1):
        f.write(f"| {i} | `{a}` | {b.replace('|', '/')} | {c.replace('|', '/')} |\n")
print(len(righe), "commenti →", out)
