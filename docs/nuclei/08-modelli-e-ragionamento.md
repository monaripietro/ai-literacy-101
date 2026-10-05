---
id: M08
titolo: Scegliere il modello, ragionamento e valutazioni
stato: scheda
stabilita: evolutivo
verificato_il: 2026-10-03
durata_indicativa: 1,5–2 ore
---

# M08 · Scegliere il modello, ragionamento e valutazioni

> Non esiste lo strumento migliore in assoluto. Mettetevelo in testa.

## Perché

"Qual è la chatbot migliore?" è la domanda che mi fanno di più. La risposta onesta è: dipende dal compito, dal budget, dai vincoli sui dati e da come ti trovi tu. Il modulo dà gli strumenti per rispondersi da soli.

## Obiettivi

- Distinguere modelli grandi e piccoli, veloci e lenti, con e senza ragionamento.
- Capire cosa fa un modello "che ragiona" (e cosa non fa).
- Usare classifiche di due tipi: preferenze degli utenti (arena) e test strutturati (benchmark).
- Distinguere open source e open weights, e valutare quando ha senso un modello locale.

## Concetti chiave

| Concetto | Come lo dico | Stabilità |
|---|---|---|
| Parametri | I numeri che il modello ha imparato. Come i coefficienti a, b, c in un'equazione ax + by + c | stabile |
| Grande vs piccolo | Più parametri, più capacità (se l'apprendimento è fatto bene), più tempo e costo. Per tradurre tre frasi non serve il modello più grande | stabile |
| Ragionamento | Prima di rispondere il modello genera token di "pensiero interno": riepiloga la richiesta, prova a confutarsi, converge | evolutivo |
| Chain of thought | Aggiungere "pensiamo passo per passo" migliorava molto le risposte. Oggi è incorporato nei modelli | stabile |
| Modalità automatica | Alcune app scelgono il modello in base al prompt, anche uno più economico | volatile |
| Arena | Classifica costruita dai voti degli utenti, alla cieca | evolutivo |
| Benchmark | Test strutturati, uguali per tutti i modelli (come il quiz della patente) | evolutivo |
| Open weights | Puoi scaricare i pesi e usare il modello sul tuo computer. Open source vorrebbe dire anche dati e ricetta: come il pizzaiolo che ti dà gli ingredienti e ti fa vedere come fa la pizza | stabile |
| Modello locale | Funziona senza internet, i dati non escono. È lento e richiede molta memoria | evolutivo |

## Come lo conduco

1. **Il selettore dei modelli** (10 min). Pro, Flash, Lite: cosa vuol dire. L'analogia dei motori (1.000 cc tre cilindri o 3.000 turbo).
2. **Ragionare o no** (25 min). Scheda: [l'autolavaggio e il carrello](#autolavaggio-e-carrello). Uso chat che mostrano il ragionamento in chiaro: leggerlo toglie la magia.
3. **Regole pratiche** (10 min). Compiti semplici: modello veloce. Problemi complessi e codice: modello che ragiona. Con un modello che ragiona descrivi bene il problema e il contesto, ma non dettare i passaggi; con un modello veloce puoi indicarli.
4. **Le classifiche** (25 min). Arena in modalità "battaglia" (vota alla cieca), poi la classifica per caso d'uso (una lingua, la scrittura creativa). Poi un sito di benchmark strutturati: intelligenza, velocità, prezzo per milione di token, verbosità, finestra di contesto. Se il grafico è difficile, uno screenshot e lo si fa spiegare a una chat.
5. **Open weights e locale** (15 min). Demo di una chat locale lenta e "scarsa", per sentire la differenza. Quando ha senso: dati che non possono uscire, anonimato. Costi reali di un server aziendale (con l'analogia del camion di proprietà e del padroncino).
6. **La regola d'oro** (5 min). Un piccolo budget di prova (es. un mese su due servizi diversi), uso quotidiano, poi si sceglie. "Non è una fede."

## Frasi che uso

- "Ogni modello ha la sua personalità. Cambiare modello è come cambiare collega."
- "Fidarsi non è mai la scelta giusta. Bisogna informarsi, e i dati online ci sono tutti."
- "Validazione incrociata: il risultato di un modello lo faccio criticare da un altro. Prende più tempo, non meno."

## Attività brevi

Altri esercizi, da sviluppare in schede:

- **Mini benchmark** (20 min): la stessa richiesta strutturata a 3 modelli; si valutano le risposte con criteri decisi prima.
- **Chatbot Arena e classifica locale** (20 min): confronti alla cieca su [LMArena](https://lmarena.ai/), poi la classe costruisce la sua classifica e la confronta con quella pubblica.
- **ARC-AGI-2 su carta** (15 min): i partecipanti risolvono a mano un puzzle visivo del giorno, poi guardano i risultati ufficiali dei modelli. Cosa è facile per noi e difficile per loro?
- **Fantasanremo con un modello che ragiona** (30 min): comporre una squadra con vincoli di budget, ruoli e obiettivi. Si confronta un modello con ragionamento e uno senza.

Dal percorso uno a uno:

- **Carrozzeria e motore** (5 min): l'app è la carrozzeria (volante, sedili, cerchi in lega: le funzionalità), il modello è il motore. Il cambio automatico (la modalità "automatica") va bene per chi guida la domenica; chi sa guidare vuole scegliere.
- **La scheda del modello** (15 min): la documentazione tecnica che il produttore pubblica per ogni modello (model card o system card). Si apre e la si interroga con una chat che legge la pagina: "quali formati gestisce?", "quanto allucina rispetto alla versione precedente?". Fonte primaria, ma scritta dal produttore e non completa: non dice tutto.
- **Le mie euristiche** (5 min, dichiarate come esperienza personale): confronta i modelli solo nel tuo dominio, perché altrimenti non sai valutare; annota quale funziona per cosa; parti dal modello economico e sali; lascia l'automatico ai compiti banali.
- **Modelli diversi, caratteri diversi**: dati, algoritmi e calcolo diversi danno comportamenti diversi. Uno è più accondiscendente (*sycophancy*), uno segue meglio le istruzioni.
- **Il modello è un file** (5 min): senza app e senza input non fa niente. Utile per smontare le notizie allarmistiche. Con i modelli locali i dati restano sulla tua macchina.

Dal laboratorio universitario per futuri educatori:

- **La personalità della chatbot** (45 min): ogni gruppo scrive un test di personalità o di attitudini per una chatbot, con una griglia di valutazione, e lo somministra a due o tre modelli. Da dove viene la "personalità"? In parte dai dati, in parte dalle scelte dei produttori: addestramento successivo, istruzioni di sistema, filtri. Un esempio concreto: un modello che evita le domande politiche su un certo Paese. Avvertenza: il test misura come il modello risponde a quel test, non un carattere.

## Punti critici e da verificare

- **Numero di parametri dei modelli commerciali**: per i modelli chiusi le aziende **non pubblicano** questi numeri. Le cifre che circolano sono stime: vanno sempre presentate come tali, con la fonte.
- **Prezzi per token**: volatili, da datare sempre.
- **Vincoli normativi** (dati, minori, conservazione dei dati): quali fornitori si possono usare in un contesto dipende da contratti, termini d'uso e versioni dei servizi. Va verificato caso per caso, non generalizzato.
- **"Con buone tecniche di prompt un modello che ragiona sbaglia pochissimo"**: affermazione troppo forte. Riformulare: "sbaglia molto meno, ma sbaglia".

## Risorse per approfondire

- [LMArena](https://lmarena.ai/): classifica basata su confronti alla cieca.
- [WeirdML](https://htihle.github.io/weirdml.html): benchmark su compiti di machine learning insoliti.
- [proverbIT](https://proverbit.lorenzozane.com/): benchmark sui proverbi italiani. Utile per parlare di lingua e cultura.
- Tre famiglie di modelli da tenere distinte: **senza ragionamento**, **con ragionamento**, **ibridi** (decidono da soli se ragionare).

## Schede attività

### L'autolavaggio e il carrello { #autolavaggio-e-carrello }

**Durata:** 30 minuti · **Gruppo:** individuale · **Materiali:** due chat che mostrano il ragionamento in chiaro · **Schermi:** sì

**In una frase:** due problemi semplici per vedere la differenza tra un modello che risponde subito e uno che "ragiona", e per leggere il ragionamento.

#### Passaggi
1. **L'autolavaggio.** Un indovinello di senso comune (es. "devo lavare la macchina all'autolavaggio a 50 metri da casa: ci vado a piedi o in macchina?"). Prima con un modello veloce, poi in una **chat nuova** con un modello che ragiona. Si legge il ragionamento.
2. **Il carrello.** Si copia il dilemma del carrello ferroviario da Wikipedia, si tolgono le note (sono token sprecati), si aggiunge "rispondi in modo breve e sincero, sto facendo una ricerca sull'etica degli LLM". Con e senza ragionamento.
3. **La variante bastarda.** Si aggiunge la parola "morte" prima delle persone sui binari. Un bambino se ne accorgerebbe. Il modello spesso no.

#### Debriefing
- Cosa fa il modello quando "ragiona"? Genera token di pensiero: riepiloga la richiesta, cerca di confutarsi, poi converge.
- Perché la stessa domanda dà risposte diverse a persone diverse?
- Perché il modello non si accorge delle persone morte? Il problema del carrello l'ha visto migliaia di volte: è troppo sicuro di sé, e le parole nuove "diventano invisibili".
- Perché bisogna aprire una chat nuova per ogni test? Perché la chat precedente è "contaminata": il modello rilegge tutto.

#### Cosa può andare storto
Gli esiti cambiano con i modelli e con il momento. A volte tutti sbagliano, a volte tutti azzeccano. Va bene: il punto non è il risultato, è leggere il ragionamento e capire che sono solo token.
