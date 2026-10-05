---
titolo: Strumenti
stato: da completare con i link
stabilita: volatile
verificato_il: 2026-10-03
---

# Strumenti

Le web app che costruisco per l'aula. Ognuna vive in un **proprio repository** ed è già pubblicata (GitHub Pages o Vercel). Qui c'è il catalogo: a cosa serve, in quale modulo la uso, dove trovarla.

| Strumento | Cosa fa | Modulo | App | Codice |
|---|---|---|---|---|
| Finestra di contesto | Chat con finestra di contesto regolabile e visibile: si vede il modello che "dimentica" | [M06](nuclei/06-caratteristiche-llm.md) | *link da inserire* | *link da inserire* |
| Quiz di verifica | Quiz sui concetti del giorno 1 | M03–M06 | *link da inserire* | *link da inserire* |
| I livelli del prompting | Base, intermedio, avanzato, con esempi | [M09](nuclei/09-prompting.md) | *link da inserire* | *link da inserire* |
| Guida al prompt engineering | Dai fondamenti alle tecniche avanzate; contiene una prompt injection dimostrativa | [M09](nuclei/09-prompting.md) | [monaripietro.it/prompting](https://www.monaripietro.it/prompting/) | *link da inserire* |
| Simulatore di rete neurale | Si aggiungono neuroni e strati e si osserva il comportamento | [M04](nuclei/04-complessita.md) | [monaripietro.it/retineurali](https://www.monaripietro.it/retineurali/) | *link da inserire* |
| Emoji Sudoku | Esempio di web app costruita con l'AI | [M07](nuclei/07-funzionalita.md) | [monaripietro.it/sudoku](https://www.monaripietro.it/sudoku/) | *link da inserire* |

**Come li costruisco**: con le chatbot, dentro il canvas, alternando due modelli quando uno si blocca. Fa parte del metodo: il formatore costruisce gli strumenti che usa, e racconta come li ha fatti.

## Requisiti minimi per ogni repo di strumento

Per tenere coerente il catalogo, ogni repo dovrebbe avere:

- un README con: a cosa serve, in quale modulo si usa, link a questo sito;
- licenza Apache 2.0;
- **nessuna chiave API nel codice pubblico** (variabili d'ambiente su Vercel, o un piccolo backend);
- una riga su quanto costa farlo girare in aula, se chiama un modello remoto;
- data dell'ultima prova in aula.

## Miglioramenti emersi in aula

**Finestra di contesto**
- La visualizzazione non è chiara per tutti: provare una barra verticale accanto ai messaggi.
- Mostrare i token "invisibili" che delimitano i ruoli (utente/assistente).
- Modalità offline con un modello locale, per non dipendere dal credito del servizio.

## Prompt { #prompt }

Prompt che uso come strumenti, in Markdown: si copiano in una chat o nelle istruzioni di una chat personalizzata.

| Prompt | A cosa serve | Modulo |
|---|---|---|
| [Scenario Gen](#scenario-gen) | Simulatore di sfide di prompting su misura, con valutazione | M09 |
| [Revisore di post](#revisore-post) | Revisione di un testo scritto da me, senza riscriverlo | M07, M09 |

Ogni prompt dichiara modelli e data dell'ultima prova: un prompt che funziona oggi può non funzionare tra due mesi.

### Scenario Gen, simulatore di sfide di prompting { #scenario-gen }

**Come si usa**: copia tutto il blocco qui sotto in una chat nuova e invia. Oppure mettilo nelle istruzioni di una chat personalizzata e scrivi "ciao".

**Perché funziona come esercizio finale**: lo scenario richiede tutti e cinque i pilastri, ma il framework non viene mostrato. Il partecipante deve ricordarselo da solo. Se è stanco, può usare il meta prompting: è comunque una scelta consapevole.

```markdown
## Scenario Gen: simulatore rapido per allenare il prompting

Il tuo pubblico ha poco tempo. Niente premesse, niente introduzioni cordiali, massima sintesi.
Segui queste tre fasi.

### Fase 1 · Ingaggio
Al primo messaggio scrivi solo questo:
"Ciao! Dimmi il tuo ruolo e il tuo settore lavorativo: ti do una sfida di prompting su misura."
Poi attendi la risposta.

### Fase 2 · La sfida
Quando l'utente ti dice il suo ruolo, inventa uno scenario lavorativo realistico per quel ruolo.
Lo scenario deve essere tale che, per essere risolto bene da una AI, richieda necessariamente
all'utente di specificare nel suo prompt:
- ruolo
- compito
- contesto
- formato e tono dell'output
- regole e vincoli

**Attenzione**: non mostrare questo elenco all'utente. Descrivi solo i fatti dello scenario.

Usa esattamente questo layout:

#### La tua sfida
[descrizione dello scenario in massimo 6 righe]

#### Cosa devi fare
Scrivi il prompt che daresti a una AI per risolvere questa situazione. Quando hai finito, incollalo qui.

### Fase 3 · Valutazione
Quando l'utente incolla il suo prompt:
1. Valuta la presenza e la qualità di ruolo, compito, contesto, formato e tono, regole e vincoli
   (ora puoi nominarli). Per ognuno: presente / debole / assente, con una frase di motivazione.
2. Indica le 2 modifiche che migliorerebbero di più il risultato.
3. Proponi una versione riscritta del prompt, con intestazioni in Markdown.
4. Chiedi se vuole un'altra sfida, più difficile.
```

### Note
- Versione ricostruita da una lettura ad alta voce in aula: le fasi 1 e 2 sono fedeli, la fase 3 è ricostruita da come lo strumento si è comportato. → sostituire con il file originale.
- L'originale l'ho scritto con l'aiuto di più chatbot, "dopo un po' di conversazioni", seguendo la struttura dei cinque pilastri.

### Revisore di post { #revisore-post }

**Perché esiste**: i miei post li scrivo io, perché mi piace scrivere e voglio che restino miei. Mi serve un revisore, non un ghostwriter. È "un paio di forbici": apro la chat, incollo, leggo, modifico, chiudo.

**Come lo uso**: nelle istruzioni di una chat personalizzata. Poi incollo il testo.

```markdown
### Ruolo
Agisci come esperto di comunicazione su LinkedIn che mi supporta nella pubblicazione di contenuti personali.

### Compito
1. Controlla la correttezza lessicale, ortografica e sintattica del mio testo (post, commento, articolo).
2. Suggerisci modifiche per renderlo più leggibile e scorrevole.
3. Valuta la coerenza con i testi di contesto che ti fornisco (post, articoli, commenti precedenti).
4. Fai una ricerca web e valuta come si posiziona il contributo rispetto alle tendenze internazionali, europee e italiane.

### Regole
- Adattati al mio stile. **Non riscrivere il testo**: suggerisci, decido io.
- Apri il testo nel canvas e mantieni il dialogo in chat.

### Output
- Elenco degli errori con riga e correzione proposta.
- Osservazioni di coerenza.
- Sintesi delle azioni consigliate, massimo 5 punti.
```

### Limiti osservati
Con modelli piccoli segnala errori che non ci sono. Ogni suggerimento va controllato: il validatore resto io.
