---
titolo: Glossario
stato: bozza
stabilita: stabile (salvo dove indicato)
verificato_il: 2026-10-03
---

# Glossario

Le definizioni come le uso in aula. Non sono le più rigorose possibili: sono quelle che permettono a una persona non tecnica di capirsi con un tecnico.

### Intelligenza artificiale
Disciplina transdisciplinare (informatica, matematica, ma anche psicologia, filosofia, etica) che studia sistemi capaci di svolgere compiti che associamo all'intelligenza. È un insieme molto più grande del machine learning.

### Machine learning
*Apprendimento automatico*. Macchine che apprendono in modo automatico **da esempi**, senza che qualcuno le programmi passo per passo.

### Deep learning
Machine learning che usa reti neurali artificiali in configurazioni complesse. Tutta l'AI generativa di oggi è deep learning.

### Dataset
L'insieme degli esempi da cui la macchina apprende. **La porzione di realtà da cui la macchina apprende.**

### Algoritmo di apprendimento
La sequenza di calcoli che trova i pattern negli esempi. (Algoritmo = sequenza di operazioni.)

### Modello allenato
Uno o più file pieni di numeri che contengono ciò che la macchina ha imparato. Da solo non fa niente.

### Parametri / pesi
I numeri che compongono il modello allenato. "Modello più grande" = più parametri.

### Applicazione
Il software che permette di usare un modello. ChatGPT è un'applicazione; GPT-x è un modello.

### Input / prompt
Dati nuovi dati al modello. Nelle chatbot il prompt è un'istruzione in linguaggio naturale.

### Inferenza
Detta anche output: la risposta del modello. È sempre una previsione, quindi sempre con un margine d'errore.

### Training / deploy
Le due fasi: prima si impara, poi (dopo il test) si mette in produzione e si usa. Gli utenti stanno sempre nella seconda.

### Token
Sequenza di caratteri a cui è associato un numero. Le chatbot leggono e scrivono token, non parole.

### LLM
*Large language model*, modello di linguaggio di grandi dimensioni. Il modello allenato che fa funzionare la generazione di testo. Un predittore del token successivo.

### Knowledge cutoff
Il punto nel tempo in cui finiscono i dati da cui il modello ha imparato.

### Allucinazione
Risposta scorretta ma verosimile. (Il termine è discusso perché antropomorfizza.)

### Finestra di contesto
Il numero massimo di token che il modello rilegge a ogni invio. La sua memoria di lavoro. *Stabilità: il concetto è stabile, le dimensioni sono volatili.*

### Ragionamento (modelli *reasoning*)
Modelli che, prima di rispondere, generano token di "pensiero interno" per analizzare la richiesta e verificarsi. *Evolutivo.*

### Chain of thought
Tecnica che fa esplicitare i passaggi intermedi ("pensiamo passo per passo"). Oggi incorporata nei modelli.

### RAG
*Retrieval-augmented generation*: tecniche per recuperare pezzi pertinenti di documenti e passarli al modello. È uno dei modi in cui vengono gestiti gli allegati.

### Code interpreter
Funzionalità in cui il modello scrive codice (di solito Python) che viene eseguito davvero, per esempio per fare calcoli.

### Chat personalizzata
Una chat con istruzioni, file e strumenti fissi. Nomi commerciali: GPT, Gem, "agente" (in Microsoft Copilot). *Volatile nei nomi.*

### Agente
Sistema che, dato un obiettivo, pianifica, sceglie gli strumenti, esegue e verifica in autonomia. *Evolutivo.*

### Open source / open weights
Open weights: puoi scaricare i pesi del modello e usarlo dove vuoi. Open source: anche dati, codice di addestramento, ricetta.

### Black box
Sistema di cui vedi ingressi e uscite ma non il processo interno. Le reti neurali profonde lo sono, in parte, anche per chi le costruisce.

### GIGO
*Garbage in, garbage out*. Esempi spazzatura, risultati spazzatura.

### Sycophancy (piaggeria)
La tendenza dei modelli a darti ragione e a lodarti. È un comportamento appreso, non un'emozione.

### Turco meccanico
Automa scacchista del Settecento con un umano nascosto dentro. Per estensione: automazione apparente che nasconde lavoro umano.
