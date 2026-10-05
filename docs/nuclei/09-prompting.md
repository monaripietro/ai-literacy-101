---
id: M09
titolo: Prompting, la lente d'ingrandimento
stato: scheda
stabilita: evolutivo
verificato_il: 2026-10-03
durata_indicativa: 2–3 ore
---

# M09 · Prompting, la lente d'ingrandimento

> Il prompt è una lente d'ingrandimento. L'LLM è il sole. Se non posizioni bene la lente, l'energia non si concentra e il fuoco non parte.

## Perché

Le aziende stanno rendendo i modelli sempre più capaci di capire anche i prompt scritti male. Il cerchio di luce arriva comunque per terra, ma diffuso: ottieni una risposta generica a una richiesta che non era a fuoco. Più focalizzi, più il risultato si avvicina alle tue aspettative.

Nel prompting non esistono il giusto e lo sbagliato. Ci sono "ha capito / non ha capito" e "ha funzionato / non ha funzionato rispetto alle mie aspettative". È **alchimia empirica**: provi, osservi, aggiusti.

## Obiettivi

- Passare dal *prompt ingenuo* al *prompt strutturato* (i cinque pilastri).
- Conoscere e provare quattro tecniche: few-shot, clarify before answering, meta prompting, reverse meta prompting.
- Usare delimitatori (Markdown) per rendere il prompt leggibile e riutilizzabile.
- Sapere quando ha senso un prompt lungo e strutturato e quando no.

## I cinque pilastri

| Pilastro | Cosa chiedersi | Esempio di trappola |
|---|---|---|
| **Ruolo** | Chi deve essere la chat? | "Agisci come mio padre": il modello non sa chi è tuo padre. Descrivilo |
| **Compito** | Cosa deve fare, concretamente? (diverso dall'obiettivo generale) | Un bambino con una bottiglia in mano: deve portarla, versarla, aprirla? |
| **Contesto** | Quali informazioni servono? Necessarie e sufficienti | Troppo contesto disperde, troppo poco lascia decidere al modello |
| **Output** | Formato (testo, tabella, elenco, CSV…) e tono | Se non lo dici, decide lui: titoletti, emoji, elenchi puntati |
| **Regole e vincoli** | Limiti, divieti, criteri | Un bando con 500 caratteri massimo: chiedine 450, perché non sa contare |

## Le tecniche

| Tecnica | In una frase | Quando la uso |
|---|---|---|
| **Few-shot** | Do esempi di cosa voglio, e anche di cosa *non* voglio | Classificazioni, formati ripetitivi, imitare uno stile |
| **Clarify before answering** | "Prima di rispondere fammi al massimo N domande, una alla volta" | Quando non ho le idee chiare. Per me è la tecnica che cambia di più l'uso quotidiano |
| **Meta prompting** | "Agisci come esperto di prompt e scrivi il prompt per ottenere…" | Per superare la paura della pagina bianca; poi lo modifico io |
| **Reverse meta prompting** | "Analizza questo testo di riferimento, poi scrivi un prompt per ottenere testi simili" | Uniformare uno stile, replicare un formato |

**Una scelta didattica:** il meta prompting lo insegno per ultimo. Se lo mostro subito, nessuno prova più a scrivere un prompt da sé.

**Un trucco che spiega molto:** chiedere al modello di analizzare prima e generare poi non serve a "farlo ragionare". Serve a mettere nella finestra di contesto informazioni che influenzeranno i token successivi.

## Come lo conduco

1. **La lente** (5 min).
2. **I cinque pilastri** (15 min), con il sito di supporto a tre livelli (base, intermedio, avanzato).
3. **La mail delicata** (30 min). Scheda: [mail al collaboratore](#prompt-mail-collaboratore). Si prende uno scenario scritto come muro di testo e lo si scompone nei cinque blocchi, come mattoncini Lego.
4. **Le quattro tecniche** (60 min), ognuna su uno scenario: classificare commenti (few-shot), organizzare un evento di team building (clarify), trasformare appunti di riunione in verbale (meta), poesia nello stile di un testo di riferimento (reverse).
5. **Markdown in due minuti** (10 min). Cancelletti, asterischi, trattini: per l'umano sono fastidiosi, per la macchina sono struttura.
6. **L'esame finale** (30 min). Il [simulatore di scenari](../strumenti.md#scenario-gen): un prompt che ti chiede ruolo e settore, ti dà una sfida su misura, valuta il tuo prompt e ti dà consigli.

## Frasi che uso

- "Chi ben comincia è a metà dell'opera: per i compiti complessi, partite da un buon prompt e poi conversate."
- "Quando non avete le idee chiare, fatevi fare le domande invece di scrivere cose a caso."
- "Se scrivete già bene, il prompting vi porta meno vantaggi. Se scrivete come capita, ve ne porta tanti."

## Attività brevi

Altri esercizi:

- **Indovina il prompt** (15 min): mostro una risposta, la classe ricostruisce il prompt che l'ha generata. Ingegneria inversa.
- **Prompt injection** (20 min): [Gandalf di Lakera](https://gandalf.lakera.ai/), un gioco a livelli in cui si convince il modello a rivelare una password. Poi una demo reale: una pagina web con istruzioni nascoste, da far riassumere a una chatbot o a un browser con AI. Il mio [sito sul prompting](https://www.monaripietro.it/prompting/) ne contiene una.
- **I prompt li scrivono meglio le macchine** (10 min): far scrivere il prompt alla chatbot partendo dall'obiettivo, poi confrontarlo con il nostro.

Dal percorso uno a uno:

- **Dalla chat lunga alla chat personalizzata** (30 min): quando una chat ha prodotto un risultato che ti piace, "leggi tutta la conversazione e scrivi le istruzioni per ottenere lo stesso risultato in una chat nuova". Quelle istruzioni diventano una chat personalizzata. Tre cose che si imparano strada facendo:
    - se le istruzioni superano il limite di caratteri, si chiede di comprimerle "mantenendo i vincoli";
    - caricare un documento di riferimento non basta: le istruzioni devono dire di usarlo;
    - si prova prima di condividerla con i colleghi.
- **Intervistami** (5 min): "fammi al massimo 5 domande, una per volta, prima di rispondere". I modelli che ragionano a volte lo fanno da soli.
- **Prompt injection in tre tempi** (20 min): (1) una pagina con istruzioni nascoste nel codice, mostrate con "visualizza sorgente"; (2) una chatbot commerciale la riassume senza eseguirle e, se richiesto, le elenca; (3) un modello piccolo, senza protezioni, le esegue. Le difese stanno sia nell'addestramento del modello sia nella pulizia del testo prima che arrivi al modello. Con gli agenti il rischio cresce.

## Punti critici e da verificare

- **Dati sul chain of thought**: il miglioramento (dal 17,7% al 78,7%) viene da Kojima et al. (2022), con un solo modello e su un benchmark di aritmetica. Va citato con questo contesto, non come percentuale generale.
- **Esercizi su scenari generici** (la mail, l'evento): alcuni partecipanti li sentono lontani dalla realtà ("una mail palesemente scritta con l'AI a un collaboratore da motivare viene sgamata"). È un feedback utile. Gli esercizi vanno portati sui problemi reali dei partecipanti.
- **Autenticità della scrittura**: in aula è nato un dibattito ("mi sento disonesta a farmi scrivere le mail"). Non ho una risposta unica: è una scelta personale e di contesto. Io i miei post li scrivo a mano e uso la chat come revisore. Il tema merita uno spazio dedicato, non una battuta.
- **Omologazione dello stile**: i testi rifiniti dall'AI tendono ad assomigliarsi tutti. Rompere le regole a un certo punto serve.

- **"Il prompting conta sempre meno"**: contano meno i trucchi (chiedere di ragionare passo passo serve poco ai modelli che ragionano già). Contano di più contesto, vincoli e verifica. Dirlo così evita di contraddire il resto del nucleo.

## Risorse per approfondire

- [Prompt Engineering Guide](https://www.promptingguide.ai/it) (in italiano).
- Guide dei produttori, da riverificare a ogni nuovo modello: le best practice di OpenAI e la guida al prompting di GPT-5 nell'OpenAI Cookbook.
- [Markdown Guide](https://www.markdownguide.org/): il formato in cui conviene scrivere i prompt lunghi.
- Dal prompt al contesto: Andrej Karpathy, [*Software Is Changing (Again)*](https://www.youtube.com/watch?v=LCEmiRjPEtQ); Sean Grove, [*The New Code*](https://www.youtube.com/watch?v=8rABwKRsec4) (sulla scrittura di specifiche); [Context-Engineering](https://github.com/davidkimai/Context-Engineering).
- Parole da conoscere: *context engineering*, *context window degradation* (le prestazioni calano quando il contesto è molto lungo), *spec-driven development*.

## Schede attività

### Dal muro di testo ai cinque pilastri { #prompt-mail-collaboratore }

**Durata:** 30 minuti · **Gruppo:** individuale o coppie · **Materiali:** lo scenario in testo · **Schermi:** sì

**In una frase:** prendere uno scenario scritto tutto attaccato e smontarlo in ruolo, compito, contesto, output, regole, come mattoncini Lego.

#### Lo scenario (esempio)
> Sei un team leader. Un tuo collaboratore ha appena inviato una presentazione per un cliente importante. Il lavoro è tecnicamente corretto ma poco chiaro, troppo lungo e senza focus sui benefici per il cliente. Devi scrivergli una mail per spiegargli come migliorarla senza demotivarlo. La presentazione va consegnata entro 24 ore. Il collaboratore è sensibile alle critiche e ci ha lavorato molto. Il cliente si aspetta un documento snello, visivo, orientato ai risultati. La mail deve essere professionale ma empatica, con esempi concreti.

#### Passaggi
1. Copiare lo scenario in una chat. Prima di inviarlo, riorganizzarlo con intestazioni: **Ruolo**, **Compito**, **Contesto**, **Output**, **Regole e vincoli**. La chat è il team leader o un consulente di comunicazione? Decidi tu.
2. Aggiungere quello che manca (tono, lunghezza).
3. Inviare. Confrontare con chi ha inviato il muro di testo.

#### Debriefing
- Cosa è cambiato nel risultato? E nella leggibilità del prompt per te, quando devi riusarlo o modificarlo?
- Quali informazioni erano contesto e quali vincoli?
- Mandereste davvero questa mail? *(In aula qualcuno ha detto di no: "il collaboratore se ne accorge". È una domanda legittima, e va discussa.)*

#### Variante consigliata
Lo stesso esercizio su una comunicazione delicata **reale** del proprio lavoro, togliendo i dati personali.
