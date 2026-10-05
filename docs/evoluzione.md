---
titolo: Evoluzione della disciplina, registro datato
stato: vivo
stabilita: —
verificato_il: 2026-10-03
---

# Evoluzione della disciplina

Questo registro serve a una cosa: mostrare che l'AI literacy non è un corpus fisso. Ogni voce ha una data, cosa è cambiato, come l'ho visto in aula e cosa cambia nell'insegnamento.

Lo storico git del repo fa il resto: ogni modifica a un modulo è datata e consultabile.

**Regola**: qui si registrano solo cambiamenti osservati o verificati con una fonte. Le previsioni vanno altrove.

## Cosa non è cambiato (e non cambierà con il prossimo modello)

- Il machine learning apprende da esempi; il dataset è una porzione di realtà.
- Le due fasi: apprendimento e utilizzo. I modelli non imparano mentre li usiamo.
- Modello ≠ applicazione.
- L'LLM genera token per token, in modo probabilistico.
- Le risposte vanno validate da chi le usa.

## Registro

| Data | Cosa | Come l'ho visto in aula | Cosa cambia nell'insegnamento |
|---|---|---|---|
| 2023 | Le chatbot non azzeccano le rime baciate in italiano | Scrivendo la canzone didattica ho dovuto rinunciare all'aiuto della chatbot | — (memoria storica) |
| 2026-02 | Gli haiku generati in italiano hanno ancora il conteggio delle sillabe sbagliato | Attività haiku | L'osservazione regge; riverificare a ogni edizione |
| 2026-02 | Prime demo in aula di agenti personali e browser agentici | Demo in aula | Gli agenti entrano nel programma come anticipazione |
| 2026-06 | Gli agenti diventano un corso a sé | Introduzione breve in aula, rinvio a un corso dedicato | Il modulo M10 diventa un ponte, non un contenuto completo |
| 2026-06 | Finestre di contesto molto ampie nelle chat a pagamento | Lab finestra di contesto: "nelle chat non è quasi più un problema, negli agenti sì" | Il concetto si insegna con una demo a finestra ridotta, perché nelle chat reali non si vede più |
| 2026-06 | Molte app scelgono da sole il modello ("modalità automatica") e la ricerca web | Esercizio dell'autolavaggio: risposte diverse a seconda del modello assegnato | Insegnare a riconoscere quale modello e quali strumenti sono attivi |
| 2026-06 | La deep research accetta fonti personali (email, documenti) e un piano modificabile | Demo in aula | Insegnare a leggere e correggere il piano prima del lancio |
| 2026-06 | Diffusione dei modelli a pesi aperti usabili in locale su computer di fascia alta | Demo di chat locale | Il tema "dove girano i miei dati" diventa una scelta concreta e non solo teorica |

## Come aggiungere una voce

1. Data in formato AAAA-MM.
2. Cosa è cambiato, in una riga, con fonte se non è un'osservazione diretta.
3. Dove l'hai visto (aula, test personale, fonte).
4. Quale modulo va aggiornato. Aggiorna anche il suo `verificato_il`.
