---
id: M04
titolo: Complicato o complesso? Perché l'AI non si spiega
stato: scheda
stabilita: stabile
verificato_il: 2026-10-03
durata_indicativa: 30–45 minuti
---

# M04 · Complicato o complesso? Perché l'AI non si spiega

> L'intelligenza artificiale ha rotto il muro tra complicato e complesso.

## Perché

È la chiave per tre cose che altrimenti restano misteriose: perché neanche chi costruisce i modelli sa spiegare una risposta, perché compaiono capacità che nessuno aveva previsto, perché la legge europea vieta certi usi.

## Obiettivi

- Distinguere un sistema complicato da uno complesso con esempi quotidiani.
- Capire perché le reti neurali profonde sono *black box*, anche per chi le progetta.
- Collegare la non spiegabilità a responsabilità e regole (AI Act).
- Sostituire l'ansia con la consapevolezza.

## Concetti chiave

| Concetto | Come lo dico | Stabilità |
|---|---|---|
| Complicato | Un orologio, un'auto: si rompe un pezzo, lo trovi, lo sostituisci, torna come prima | stabile |
| Complesso | Le api, le formiche, una classe: elementi interconnessi, proprietà emergenti, sviluppo imprevedibile. Se manca una persona, la lezione cambia | stabile |
| Black box | Vedo cosa entra e cosa esce, non come avviene la trasformazione. Vale anche per gli ingegneri che costruiscono i modelli | stabile |
| Proprietà emergenti | Aumentando dati e calcolo, i modelli mostrano capacità che non ci aspettavamo | evolutivo |
| Responsabilità | Se il sistema non è spiegabile, chi risponde della decisione? Il giudice risponde del suo giudizio; il produttore del modello di solito no | evolutivo |
| AI Act | Approccio per livelli di rischio; alcuni usi vietati (es. social scoring) | evolutivo |

## Come lo conduco

1. **L'orologio** (5 min). Chiedo che orologio ha qualcuno in prima fila. Se si rompe un ingranaggio? Lo sostituisci. Funziona come prima.
2. **La classe** (5 min). Se domani una persona non c'è, la lezione cambia, in meglio o in peggio. Non si può prevedere.
3. **La rete da pesca** (5 min). La rete neurale come una rete di nodi che fanno calcoli. Sopra un certo numero di nodi si passa dal complicato al complesso.
4. **La conseguenza** (10 min). Se una chatbot si "rompe" non sai dove mettere le mani. Conosci i pezzi singoli, ma messi insieme non sai spiegare il risultato.
5. **Le regole** (10 min). La piramide del rischio dell'AI Act. Il caso del triage durante la pandemia: chi decide, e chi ne risponde?
6. **Niente ansia** (5 min). "Non vi chiedo di avere ansia. Vi chiedo di essere consapevoli."

## Frasi che uso

- "Sono solo calcoli. Ma calcoli sovrapposti in modo tale che non riesci più a risalire al processo."
- "Anche gli umani sbagliano, e anche lì non sappiamo spiegare perché."
- "AGI? Ad oggi è soprattutto marketing."

## Attività brevi

- **Complicato o complesso?** (5 min): due post-it alla lavagna, "complicato" e "complesso". La classe sistema degli esempi sotto l'uno o l'altro: un orologio, il traffico, un motore, un'economia, una rete neurale.
- **Giocare con una rete neurale** (15 min): [TensorFlow Playground](https://playground.tensorflow.org/), oppure il mio [Simulatore di rete neurale](https://www.monaripietro.it/retineurali/). Aggiungere neuroni e strati e osservare quando il comportamento smette di essere leggibile.

- **Il percettrone e le porte logiche** (15 min, per profili tecnici): un solo neurone artificiale nel simulatore. Somma pesata degli input più il bias, poi una soglia (0 o 1). Si regolano i pesi e il bias finché la tabella di verità dell'AND torna giusta, poi l'OR. Messaggio: un neurone si capisce, è una somma. Migliaia collegati in strati non si spiegano più.
- **Il peso come diametro del tubo**: l'input è l'acqua, il peso è il diametro del tubo. Decide quanto segnale passa.

## Punti critici e da verificare

- **AI Act e sanità**: l'AI Act vieta pratiche specifiche (es. il social scoring, perché porta a trattamenti dannosi per le persone) e classifica molti usi sanitari, come il triage di emergenza, **ad alto rischio**: consentiti, con obblighi di trasparenza e supervisione umana.
- **Spiegabilità**: la ricerca sull'interpretabilità (es. i lavori di Anthropic su come i modelli rappresentano concetti e calcoli) sta facendo progressi. "Non lo sapremo mai" è troppo forte: meglio "oggi lo sappiamo solo in parte".
- **"AGI è solo marketing"**: posizione personale, va marcata come tale.

## Risorse per approfondire

- *Neural Networks for Babies* ([video](https://youtu.be/IX6acE4l1YQ)): introduzione semplice.
