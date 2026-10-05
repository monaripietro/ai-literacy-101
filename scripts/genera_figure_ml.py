#!/usr/bin/env python3
"""Genera le figure originali sul machine learning (licenza CC BY 4.0).

Sostituiscono le immagini prese dal web nelle slide della board.
Uso: python3 scripts/genera_figure_ml.py → docs/schemi/ml-*.svg
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "schemi")
INK, MUTED, A, B, C = "#1f2933", "#6b7280", "#2563eb", "#ea580c", "#16a34a"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "svg.fonttype": "none"})
rng = np.random.default_rng(7)


def pulisci(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color("#cbd5e1")


def tipi_apprendimento():
    fig = plt.figure(figsize=(12, 6.4))
    titoli = ["Supervisionato", "Non supervisionato", "Per rinforzo"]
    riceve = ["esempi con la risposta giusta\n(etichette)", "esempi senza etichette", "premi e penalità\nper le azioni che fa"]
    problemi = ["classificazione · regressione", "raggruppamento (clustering)\nriduzione delle dimensioni", "decidere una sequenza di azioni"]
    esempi = ["filtro antispam · dettatura\nprevisione del traffico",
              "segmentare clienti\nraggruppare documenti simili",
              "giochi (scacchi, Go) · robotica\naddestramento finale delle chatbot"]
    for i in range(3):
        ax = fig.add_axes([0.04 + i * 0.32, 0.42, 0.28, 0.42])
        pulisci(ax)
        if i == 0:
            x1 = rng.normal([1, 1], 0.45, (25, 2)); x2 = rng.normal([2.6, 2.4], 0.45, (25, 2))
            ax.scatter(*x1.T, c=A, s=28, marker="o"); ax.scatter(*x2.T, c=B, s=34, marker="^")
            ax.plot([0, 3.6], [3.3, 0.2], color=INK, lw=1.5, ls="--")
        elif i == 1:
            for m in ([1, 1], [2.8, 1.2], [1.9, 2.9]):
                p = rng.normal(m, 0.32, (18, 2)); ax.scatter(*p.T, c="#94a3b8", s=28)
                ax.add_patch(plt.Circle(m, 0.75, fill=False, ec=C, lw=1.5, ls="--"))
        else:
            ax.set_xlim(0, 10); ax.set_ylim(0, 10)
            for (x, y, t) in [(2.5, 5, "agente"), (7.5, 5, "ambiente")]:
                ax.add_patch(FancyBboxPatch((x - 1.6, y - 0.9), 3.2, 1.8, boxstyle="round,pad=0.2", fc="#f1f5f9", ec=INK))
                ax.text(x, y, t, ha="center", va="center")
            ax.add_patch(FancyArrowPatch((3.5, 6.6), (6.5, 6.6), connectionstyle="arc3,rad=-0.4", arrowstyle="-|>", mutation_scale=14, color=INK))
            ax.add_patch(FancyArrowPatch((6.5, 3.4), (3.5, 3.4), connectionstyle="arc3,rad=-0.4", arrowstyle="-|>", mutation_scale=14, color=C))
            ax.text(5, 8.4, "azione", ha="center", color=INK); ax.text(5, 1.4, "premio / penalità", ha="center", color=C)
        x0 = 0.04 + i * 0.32 + 0.14
        fig.text(x0, 0.89, titoli[i], ha="center", fontsize=15, weight="bold", color=INK)
        fig.text(x0, 0.33, "riceve", ha="center", fontsize=9, color=MUTED)
        fig.text(x0, 0.27, riceve[i], ha="center", va="center", color=INK)
        fig.text(x0, 0.19, "problemi tipici", ha="center", fontsize=9, color=MUTED)
        fig.text(x0, 0.14, problemi[i], ha="center", va="center", color=INK)
        fig.text(x0, 0.07, esempi[i], ha="center", va="center", fontsize=10, color=MUTED, style="italic")
    fig.text(0.5, 0.965, "Tre modi in cui una macchina apprende", ha="center", fontsize=17, weight="bold", color=INK)
    fig.savefig(os.path.join(OUT, "ml-tipi-apprendimento.svg"), bbox_inches="tight")
    plt.close(fig)


def adattamento():
    fig, axes = plt.subplots(2, 3, figsize=(12, 7.2))
    nomi = ["Troppo semplice\n(underfitting)", "Giusto\n(generalizza)", "Troppo aderente\n(overfitting)"]
    # classificazione
    xa = rng.normal([1, 1], 0.6, (30, 2)); xb = rng.normal([2.4, 2.4], 0.6, (30, 2))
    gx, gy = np.meshgrid(np.linspace(-1, 4.5, 300), np.linspace(-1, 4.5, 300))
    for j, ax in enumerate(axes[0]):
        pulisci(ax)
        ax.scatter(*xa.T, c=A, s=22); ax.scatter(*xb.T, c=B, s=26, marker="^")
        if j == 0:
            ax.axhline(1.7, color=INK, lw=1.8)
        elif j == 1:
            ax.plot([-1, 4.5], [4.4, -1.1], color=INK, lw=1.8)
        else:
            pts = np.vstack([xa, xb]); lab = np.r_[np.zeros(30), np.ones(30)]
            d = ((gx[..., None] - pts[:, 0]) ** 2 + (gy[..., None] - pts[:, 1]) ** 2)
            z = lab[d.argmin(-1)]
            ax.contour(gx, gy, z, levels=[0.5], colors=INK, linewidths=1.6)
        ax.set_xlim(-1, 4.5); ax.set_ylim(-1, 4.5)
        ax.set_title(nomi[j], fontsize=12, color=INK)
    axes[0][0].set_ylabel("Classificazione", fontsize=13, color=INK)
    # regressione
    x = np.sort(rng.uniform(0, 1, 18)); y = np.sin(2 * np.pi * x) + rng.normal(0, 0.18, x.size)
    xs = np.linspace(0, 1, 400)
    for j, ax in enumerate(axes[1]):
        pulisci(ax)
        ax.scatter(x, y, c=A, s=22, zorder=3)
        deg = [1, 3, 15][j]
        coef = np.polyfit(x, y, deg)
        ax.plot(xs, np.clip(np.polyval(coef, xs), -2, 2), color=INK, lw=1.8)
        ax.set_ylim(-1.8, 1.8)
    axes[1][0].set_ylabel("Regressione", fontsize=13, color=INK)
    fig.suptitle("Quanto il modello si adatta agli esempi", fontsize=16, weight="bold", color=INK)
    fig.text(0.5, 0.005, "L'obiettivo non è ricordare gli esempi, ma funzionare su dati nuovi, mai visti.",
             ha="center", fontsize=11, color=MUTED, style="italic")
    fig.tight_layout(rect=[0, 0.03, 1, 0.96])
    fig.savefig(os.path.join(OUT, "ml-adattamento.svg"), bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    tipi_apprendimento()
    adattamento()
    print("ok")
