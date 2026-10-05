---
id: M06
titolo: L'LLM nudo e crudo, le caratteristiche intrinseche
stato: scheda
stabilita: evolutivo
verificato_il: 2026-10-03
durata_indicativa: 1–1,5 ore
---

# M06 · L'LLM nudo e crudo, le caratteristiche intrinseche

> Le risposte non vengono validate da niente prima di uscire. Chi le valida? L'utente.

## Perché

Le chatbot commerciali aggiungono ricerca web, memoria, strumenti. È utile, ma nasconde il comportamento del modello. Per capire davvero un LLM bisogna vederlo "nudo": un modello piccolo, senza ricerca web, uguale per tutti. Così i limiti diventano visibili.

## Obiettivi

Riconoscere, con esperimenti, quattro caratteristiche di ogni LLM:

1. è un **predittore del token successivo** (vedi [M05](05-anatomia-chatbot.md));
2. ha un **limite di conoscenza temporale** (*knowledge cutoff*);
3. **allucina**: produce risposte scorrette ma verosimili;
4. ha una **finestra di contesto**: una memoria di lavoro limitata.

## Concetti chiave

| Concetto | Come lo dico | Stabilità |
|---|---|---|
| Knowledge cutoff | Il modello sa le cose fino a un certo punto, quello in cui si ferma il dataset | stabile |
| Niente autocoscienza | Se gli chiedi il suo cutoff, ognuno di voi ottiene una data diversa: la sta generando, non la "sa" | stabile |
| Allucinazione | Risposta scorretta ma verosimile. La funzione dell'LLM è produrre testo plausibile, non vero | stabile |
| Nessun validatore | Nessuna azienda ha costruito un validatore delle risposte: la responsabilità è di chi le usa | evolutivo |
| Finestra di contesto | A ogni invio il modello rilegge tutta la conversazione entro un limite di token. Come la memoria di lavoro quando fai un calcolo con i riporti | stabile |
| Oblio | Quando la finestra è piena, i messaggi più vecchi escono e il modello "dimentica" | stabile |
| Dimensione della finestra | Oggi molto grande (centinaia di migliaia o milioni di token): nelle chat si nota poco, negli agenti è critica | volatile |

## Come lo conduco

Tutti sulla stessa chat gratuita e senza account, con un modello piccolo e senza ricerca web. Nel 2026 ho usato duck.ai. **Strumenti pari per tutti**: chi ha l'account pro non deve avere un'esperienza diversa.

1. **Il cutoff** (10 min). Domanda di attualità (chi è il Papa, chi ha vinto ieri). Poi: "qual è il tuo knowledge cutoff?". Confrontiamo le risposte in aula.
2. **Le allucinazioni** (20 min). Scheda: [caccia all'allucinazione](#caccia-allucinazione).
3. **La finestra di contesto** (25 min). Laboratorio con la web app che ho costruito, con finestra regolabile. Scheda: [finestra di contesto](#finestra-di-contesto). Strumento: [catalogo strumenti](../strumenti.md).

## Frasi che uso

- "Usare un LLM solo per chiedergli fatti è come avere una Ferrari per andare a 30 all'ora. Per quello vai in biblioteca."
- "Studiate di più, non di meno. I dettagli sbagliati nascosti nelle pieghe del testo li vedono gli esperti."
- "La risposta mediocre che a noi sembra forte, ci sembra forte perché siamo scarsi noi."

## Attività brevi

- **La legge che non esiste** (variante della caccia all'allucinazione): al posto dell'articolo della Costituzione, una legge di settore che il pubblico conosce. Si sceglie una legge vera del loro settore e si chiede un articolo "bis" che non esiste. Scegli sempre un riferimento del mondo dei partecipanti: l'allucinazione colpisce di più quando tocca il loro lavoro.

- **Il bias in 10 parole** (10 min): "meglio un'auto americana o cinese? Risposta definitiva in massimo 10 parole". Il vincolo costringe il modello a schierarsi. Poi: se la ripetessimo mille volte e contassimo le risposte, avremmo un test statistico. Il bias viene dai dati: polarizzazione, stereotipo, pregiudizio.
- **Chiudere l'allucinazione con la ricerca** (5 min): dopo l'articolo inesistente, la stessa domanda con "cerca online e dimmi quali fonti hai usato". La risposta diventa "non esiste".
- **Finestra di contesto e limiti d'uso non sono la stessa cosa**: la finestra è del modello; i limiti di messaggi e crediti li decide chi vende l'app.
- **Quando la chat si blocca** (10 min): alcune app professionali bloccano la chat quando la finestra è piena, e il lavoro sembra perso. Prima di arrivarci: "rileggi l'intera conversazione e fai una sintesi estrema dei punti chiave e del processo che ci ha portato al risultato". Con quella sintesi si apre una chat nuova, o si crea una chat personalizzata (nucleo 09).
- **Gli agenti mostrano quanto è piena la finestra, le chat di solito no.**

## Punti critici e da verificare

- **Gli esperimenti invecchiano.** L'articolo 189 o i link di YouTube potrebbero non produrre più allucinazioni con i modelli nuovi. Il principio resta, l'esempio va riverificato. → [manutenzione](../manutenzione.md)
- **duck.ai e i modelli disponibili**: volatili.
- **"Allucinazione"**: il termine stesso è discusso (antropomorfizza). Vale la pena dirlo in aula.

- **Finestra piena**: molte app oggi comprimono o riassumono in automatico invece di bloccarsi. Il comportamento dipende dall'app: va verificato prima del corso.
- **"Un milione di token"**: vale solo per alcuni modelli, e le app spesso mettono limiti propri. Un milione di token sono circa 750.000 parole in inglese: molti libri, non tre o quattro.

## Schede attività

### Caccia all'allucinazione { #caccia-allucinazione }

**Durata:** 20 minuti · **Gruppo:** individuale · **Materiali:** una chatbot gratuita con un modello piccolo e senza ricerca web, un motore di ricerca · **Schermi:** sì

**In una frase:** chiedere cose che non esistono e guardare con quanta sicurezza la macchina risponde.

#### Passaggi
1. **L'articolo che non c'è.** "Riassumi l'articolo 189 della Costituzione italiana." Poi si cerca con un motore di ricerca normale, non con la chat: gli articoli sono 139.
2. **I link perfetti.** "Dammi tre video YouTube per imparare a suonare l'ukulele." Si cliccano i link.
3. **"Sei sicuro?"** Dopo una risposta corretta, chiedere "sei sicuro?". Spesso ritratta.

#### Debriefing
- Perché le risposte sono così credibili? Perché la funzione dell'LLM è produrre testo verosimile, non vero.
- Chi ha validato la risposta prima che ve la desse? Nessuno.
- Se foste esperti di diritto costituzionale, ve ne sareste accorti subito? E nel vostro campo?

#### Cosa può andare storto
Con modelli più recenti o con la ricerca web attiva, questi esempi possono non funzionare più. Va benissimo mostrarlo: la ricerca web *mitiga* le allucinazioni, non le elimina. Tenere esempi di riserva aggiornati (vedi [manutenzione](../manutenzione.md)).

### Vedere la finestra di contesto { #finestra-di-contesto }

**Durata:** 25 minuti · **Gruppo:** individuale · **Materiali:** la web app della finestra di contesto · **Schermi:** sì — web app "Finestra di contesto" (vedi catalogo strumenti)

**In una frase:** una chat con la memoria di lavoro regolabile e visibile, per vedere il modello che dimentica.

#### Passaggi
1. Aprire la web app. La finestra di contesto è impostata bassa (200–1000 token) e si vede colorata la parte di conversazione che il modello legge.
2. Scrivere un'informazione: "mi piacciono le ciliegie". Non usare dati personali.
3. Chattare d'altro: una poesia, una barzelletta, una storiella.
4. Chiedere: "qual è il frutto che mi piace?". Se l'informazione è uscita dalla finestra, il modello non lo sa più.
5. Allargare la finestra e rifare la domanda.
6. Variante: con finestra a 200 token, chiedere un racconto di 1000 parole. Al messaggio dopo è come una chat vergine.

#### Debriefing
- Perché il modello "dimentica"? A ogni invio rilegge solo quello che sta nella finestra.
- Perché non prende un pezzo del messaggio precedente? Ci sono token invisibili che dicono chi ha scritto cosa: tagliare a metà romperebbe la struttura della conversazione.
- Nelle chat commerciali la finestra è enorme e questo problema si vede poco. Negli agenti invece è centrale.

#### Cosa può andare storto
La demo si appoggia a un modello remoto: se finisce il credito o salta la connessione, non risponde. Ho chiesto feedback in aula per migliorarla: la visualizzazione della finestra non è ancora chiara per tutti.

#### Esempio guidato: il nome che esce dalla finestra

Una chat reale con un modello locale (Cogito) e una finestra di contesto fissata a **1000 token**:

1. "Ciao, mi chiamo Max. Ricordatelo!" Il modello risponde "Ciao Max".
2. "Ora crea una storia molto lunga sullo sport." La storia occupa circa 1.500 token.
3. "Come mi chiamo?" → "Non so come ti chiami."

Sulla board la chat è evidenziata a blocchi colorati, con il conteggio dei token di ogni blocco: si vede la finestra che scende seguendo la conversazione e la parte iniziale che esce. Bonus: la storia contiene a sua volta fatti inventati. Due limiti in un solo esempio.
