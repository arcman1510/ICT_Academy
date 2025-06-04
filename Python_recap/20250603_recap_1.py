#1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
# #Se la chiave è già presente, somma il valore al valore già associato alla chiave.

esempio: list[tuple] = [("Chiave1", "Valore1"), ("Chiave2", "Valore2"), ("Chiave3", "Valore3")]

def funzione(lista_di_tuple: list[tuple]) -> dict:
    
    nuovo_dizionario: dict = {}
    
    for element in lista_di_tuple:
        
        chiave = element[0]
        valore = element[1]
        
        if chiave in nuovo_dizionario:
            
            nuovo_dizionario[chiave] += valore
        
        else:
            
            nuovo_dizionario[chiave] = valore
            
            
dizionario: dict = funzione(lista_di_tuple=esempio)
print(dizionario) 


#2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario 
#che classifi chi i numeri in liste separate per numeri positivi e negativi.



def classifica_numeri(lista):
    positivi = []
    negativi = []
    for num in lista:
        if num >= 0:
            positivi.append(num)
        else:
            negativi.append(num)
    return {
        "positivi": positivi,
        "negativi": negativi
    }

lista: list = [1, 2, -3, 4, -6, 7]

def positivi_negativi(list) -> dict:
    
    dizionario: dict = {"positivi": [], "negativi": []}
    
    for element in lista:
        
        if element >= 0:
            
            dizionario["positivi"].append(element)
            
        else:
            
            dizionario["negativi"].append(element)
            
    return dizionario

elementi_filtrati: dict = positivi_negativi(lista=lista)
print(elementi_filtrati)




def filtra_prodotti(prodotti):
    risultato = {}
    for nome, prezzo in prodotti.items():
        if prezzo < 50:
            nuovo_prezzo = round(prezzo * 1.10, 2)
            risultato[nome] = nuovo_prezzo
    return risultato

#3) Scrivi una funzione che accetti un dizionario di prodotti 
# con i relativi prezzi e restituisca un nuovo dizionario con 
# solo i prodotti che hanno un prezzo inferiore a 50, 
# ma con i prezzi aumentati del 10% e arrotondati a due cifre decimali.

prodotti_input: dict = {
    "pane": 43.3,
    "latte": 55.5,
    "pasta": 22.5,
    "olio": 47.9
}

def filtra_prodotti(prodotti: dict[str, float]) -> dict[str, float]:
    nuovo_dizionario: dict = {}
    
    for prodotto in prodotti:
        prezzo = prodotti[prodotto]
        
        if prezzo < 50:
            nuovo_prezzo = round(prezzo * 1.10, 2)
            nuovo_dizionario[prodotto] = nuovo_prezzo
            
    return nuovo_dizionario


prodotti_filtrati: dict = filtra_prodotti(prodotti=prodotti_input)
print(prodotti_filtrati)
