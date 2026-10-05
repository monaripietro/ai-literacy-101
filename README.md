# AI literacy, by Pietro Monari

**Sito navigabile:** https://ailit101.monaripietro.it/

> Conoscere per partecipare in modo attivo e consapevole alla rivoluzione dell'intelligenza artificiale generativa.

Questo repository raccoglie il mio modo di insegnare l'AI literacy: cosa insegno, in che ordine, con quali attività e perché.

Le lezioni le tengo dal 2019: corsi aziendali, master, università, scuola. Le trascrizioni restano private. Qui pubblico quello che può servire a chi forma altre persone: il metodo, i moduli, le attività pronte all'uso, gli strumenti che costruisco, gli errori da evitare.

**Per chi è:** formatori junior e senior, docenti, insegnanti, chi organizza corsi sull'AI.
**Per chi non è:** chi cerca un elenco di prompt magici. Qui ce ne sono, ma non sono il punto.

---

## Come è fatto

| Percorso | Cosa trovi |
|---|---|
| [`docs/metodo.md`](docs/metodo.md) · [`fondamenta.md`](docs/fondamenta.md) | Metodo e principi; fondamenta alla prova dell'aula |
| [`docs/nuclei/`](docs/nuclei/) | Un file per nucleo tematico: concetti, conduzione, attività e schemi insieme |
| [`docs/glossario.md`](docs/glossario.md) | I termini, definiti come li uso in aula |
| [`docs/strumenti.md`](docs/strumenti.md) | Web app (ognuna nel suo repo) e prompt |
| [`docs/fonti.md`](docs/fonti.md) · [`docs/evoluzione.md`](docs/evoluzione.md) | Bibliografia; registro datato di cosa cambia |
| [`docs/schemi/`](docs/schemi/) | Solo i file delle figure (SVG, Excalidraw), generati da `scripts/` |
| [`docs/manutenzione.md`](docs/manutenzione.md) | Cosa va riverificato e quando |

## Stabile, evolutivo, volatile

L'AI cambia ogni settimana. Una parte di quello che insegno resta valida per anni, un'altra scade in un mese. Per questo ogni pagina dichiara nell'intestazione quanto è stabile:

- **stabile**: concetti che non cambiano con il prossimo modello (cos'è il machine learning, cos'è un dataset, la differenza tra modello e applicazione).
- **evolutivo**: concetti validi ma che si spostano (finestra di contesto, ragionamento, agenti).
- **volatile**: nomi di modelli, prezzi, interfacce, funzionalità di una specifica app. Scade in fretta.

Ogni pagina ha anche la data dell'ultima verifica (`verificato_il`). Lo storico git mostra come è cambiata nel tempo. È voluto: la cronologia del repo è anche la cronologia della disciplina.

## Stato

Prima versione: 3 ottobre 2026. Il materiale viene dai miei corsi del 2026. I nuclei sono a diversi livelli di completezza: vedi l'intestazione `stato` di ogni file.

## Licenze

- Testi, schemi e attività: [CC BY 4.0](LICENSE). Puoi riusare, adattare e anche usare commercialmente, citando la fonte.
- Codice in `scripts/`: [Apache 2.0](LICENSE-CODE). Anche le web app, ognuna nel proprio repository, sono Apache 2.0.

Citazione suggerita: *Pietro Monari, AI literacy by Pietro Monari, 2026, https://github.com/monaripietro/ai-literacy-101*

## Contatti

Pietro Monari — progettista educativo e formatore sull'intelligenza artificiale.

## Il sito

Il sito è generato con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) a partire dalla cartella `docs/` e pubblicato su GitHub Pages da una GitHub Action a ogni push su `main`.

Per vederlo in locale:

```bash
pip install -r requirements.txt
mkdocs serve
```
