// Dichiarazione e valorizzazione delle variabili
const annoCorrente = new Date().getFullYear();
const annoNascita = 1990; // Sostituisci con il tuo anno di nascita

// Calcolo dell'età
const eta = annoCorrente - annoNascita;

// Calcolo degli anni necessari per raggiungere i 100 anni
const anniMancanti = 100 - eta;

// Output dei risultati
console.log("Età della persona: " + eta + " anni");
console.log("Anni necessari per raggiungere i 100 anni: " + anniMancanti + " anni");