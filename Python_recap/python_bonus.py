# Lista dei nomi
eroi = ["Midoriya", "Bakugo", "Todoroki"]
voti_eroi = []

# Raccogli voti con ciclo
for nome in eroi:
    voto = float(input(f"Inserisci il voto di {nome}: "))
    voti_eroi.append((nome, voto))  # Salviamo come tupla (nome, voto)

# Calcola media
media = round(sum(voto for _, voto in voti_eroi) / len(voti_eroi), 2)

# Stampiamo media
print(f"\nLa media dei voti degli eroi è: {media}")

# Verifica media complessiva
if media >= 6.0:
    print("🎉 Squadra promossa! Gli eroi hanno superato l'esame!\n")
else:
    print("💀 Squadra bocciata... Serve più allenamento!\n")

# Classifica e controllo individuale
print("📋 Classifica Eroi e Voti:")
for nome, voto in voti_eroi:
    stato = "✅ Promosso" if voto >= 6.0 else "❌ Bocciato"
    print(f"{nome}: {voto} - {stato}")


energia = int(input("Inserisci il livello di energia del tuo personaggio (0-100): "))

if energia >= 80:
    print("🟢 Livello massimo: modalità Ultra Instinct!")

elif 50 <= energia < 80:
    print("🟡 Livello buono: allenamento in corso…")

elif 1 <= energia < 50:
    print("🔴 Energia bassa: serve riposo o fagioli magici!")

elif energia == 0:
    print("⚫ KO tecnico. Chiamare supporto medico!")

else:
    print("Valore non valido. Inserisci un numero da 0 a 100.")
    
    
    
numero = int(input("Inserisci un numero: "))
for i in range(1, numero + 1):
    print(i)


def saluta_eroe(nome):
    print(f"Ehi {nome.upper()}, sei pronto per l'esame Python di domani?!")

# Chiamata della funzione
saluta_eroe("Manuel")

def somma(a, b):
    risultato = a + b
    return risultato

# Esecuzione
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))

totale = somma(numero1, numero2)
print(f"La somma dei due numeri è: {totale}")


def calcola_area(base, altezza):
    area = base * altezza
    return area

# Chiedi all’utente i valori
base = float(input("Inserisci la base del rettangolo: "))
altezza = float(input("Inserisci l’altezza del rettangolo: "))

# Richiama la funzione
risultato = calcola_area(base, altezza)

# Stampa il risultato
print(f"L’area del rettangolo è: {risultato}")

# Definizione della funzione
def calcola_perimetro(base, altezza):
    return 2 * (base + altezza)

# Input da parte dell’utente
base = float(input("Inserisci la base del rettangolo: "))
altezza = float(input("Inserisci l'altezza del rettangolo: "))

# Uso della funzione
perimetro = calcola_perimetro(base, altezza)

# Output
print(f"Il perimetro del rettangolo è: {perimetro}")
