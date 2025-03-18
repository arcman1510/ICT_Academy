// Input: numero di secondi
let secondiTotali = 12560; // Puoi cambiare questo valore

// Calcolo delle ore, minuti e secondi
let ore = Math.floor(secondiTotali / 3600); // 1 ora = 3600 secondi
let secondiRimanenti = secondiTotali % 3600; // Secondi rimanenti dopo aver calcolato le ore
let minuti = Math.floor(secondiRimanenti / 60); // 1 minuto = 60 secondi
let secondi = secondiRimanenti % 60; // Secondi rimanenti dopo aver calcolato i minuti

// Output del risultato
console.log(`${ore} ore, ${minuti} minuti e ${secondi} secondi`);