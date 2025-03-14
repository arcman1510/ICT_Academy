
#Q4
#Scrivi una funzione prime_factors(n: int) -> list[int] che trova i fattori primi di un numero n dato in input

#For example:
#print(prime_factors(4)) [2, 2]

def prime_factors(n: int) -> list[int]:
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
#print(prime_factors(4))


# Q1 Nel gioco del blackjack, il valore di una mano 
# è determinato dalla somma dei valori delle carte. 
# Ogni carta ha un valore compreso tra 2 e 11 compresi. 
# Tuttavia, se una mano contiene un asso, 
# il valore dell'asso può essere 1 o 11, a seconda di quale 
# sia più favorevole al giocatore in quel momento. 
# Dato un elenco di valori delle carte che rappresentano 
# una mano di blackjack, scrivi una funzione 
# per determinare il valore totale della mano.

def blackjack_hand_total(cards: list[int]) -> int:
    # elimina il pass e inserisci il tuo codice
    blackjack_hand_total:int = 0
    ace:int = 0
    for i in cards:
        if i  == 11:
            ace += 1
        else:
            blackjack_hand_total += i
    while ace > 0:
        if(blackjack_hand_total + 11) > 21:
            blackjack_hand_total += 1
            ace -= 1
        else:
            blackjack_hand_total += 11
            ace -= 1
    return blackjack_hand_total
    




#Q3
# Scrivi una funzione che accetta una stringa come input, 
# rimuove le parole non significative comuni stop_words 
# e restituisce un dizionario in cui le chiavi sono 
# parole univoche nel testo rimanente 
# (ignorando la distinzione tra maiuscole e minuscole 
# e la punteggiatura) e i valori sono le frequenze di quelle 
# parole.
#For example:

# Test
# stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
# text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
# print(word_frequency(text, stopwords))
# Result
# {'quick': 1, 'brown': 1, 'fox': 1, 
# 'jumps': 1, 'over': 1, 'lazy': 2, 'dog': 2, 'very': 1}
""""
def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:

    stopwords == []
    text == text.split()
    for i in text:
        if i in x == stopwords:
            text.remove(i)
        else:
            text.count(i)

"""

#Q2
"""
Hai il compito di indagare su un caso di numeri mancanti! 
Ti viene fornito un elenco di numeri univoci (nums) da 1 a n, 
dove n è la lunghezza dell'elenco. Sembra però che ci sia un problema: mancano alcuni numeri!

La tua missione è scrivere una funzione che prenda come input 
questo elenco di numeri (nums) potenzialmente incompleti. 
Questo elenco rappresenta i numeri esistenti, ma alcuni numeri tra 1 e n potrebbero mancare.

La funzione restituisce una nuova lista contenente 
tutti i numeri mancanti da 1 a n che non sono presenti nella lista originale. 

For example:
Test 
print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))
	
Result
[5, 6]
"""
"""
def findDisappearedNumbers(nums: list[int]) -> list[int]:
    missing_numbers =[]
    for i in range(1,len(nums)+1):
        if i not in nums:
            missing_numbers.append(i)
    return missing_numbers
"""

#Q5

"""

Sei un detective esperto nel mondo dei testi e un caso sconcertante è arrivato sulla tua scrivania. 
Due stringhe, s e t, sono i tuoi sospettati. 
La tua missione: determinare se s si nasconde in bella vista all'interno di t, ma con una svolta!

Qual è il problema?

Non puoi semplicemente confrontare le stringhe lettera per lettera. 
Immagina che s sia un personaggio subdolo che cerca di confondersi tra la folla (t). 
Potrebbero camuffarsi nascondendosi tra altri personaggi, ma non cambiano mai il loro ordine! 
Quindi, "ace" può intrufolarsi in "abcde" (rimuove semplicemente "b" e "d"), ma "aec" non funzionerebbe (l'ordine cambia).

Scrivi una funzione di interruzione del codice che prenda 
la stringa s (il carattere subdolo) e t (la folla) come input. 
Se è possibile trovare s in agguato all'interno di t mantenendo il suo travestimento (ordine), restituisce True. 
Altrimenti restituisce False. Dimostra le tue abilità da detective e svela la verità nascosta!

For example:
Test 

print(is_subsequence("abc", "ahbgdc"))
print(is_subsequence("axc", "ahbgdc"))



Result:
True
False

"""

def is_subsequence(s: str, t: str) -> bool:
    # elimina pass e inserisci il tuo codice
    t = iter(t)
    return all(c in t for c in s)
