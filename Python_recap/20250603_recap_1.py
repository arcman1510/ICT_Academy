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


print("")
print("")

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

elementi_filtrati: dict = positivi_negativi(list=lista)
print(elementi_filtrati)

print("")
print("")

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
    """
  
    """
      
       
    for prodotto in prodotti:
        prezzo = prodotti[prodotto]
        
        if prezzo < 50:
            nuovo_prezzo = round(prezzo * 1.10, 2)
            nuovo_dizionario[prodotto] = nuovo_prezzo
            
    return nuovo_dizionario


prodotti_filtrati: dict = filtra_prodotti(prodotti=prodotti_input)
print(prodotti_filtrati)


#Funzioni
#1) Scrivi una funzione che verifi ca se una combinazione di condizioni (X, Y, e Z)
# è soddisfatta per procedere con un'azione. 
# L'azione può procedere solo se la condizione X è vera 
# e almeno una tra Y e Z è vera. 
# La funzione deve ritornare "Azione permessa" oppure "Azione negata" 
# a seconda delle condizioni che sono soddisfatte.


def condizione(X: bool, Y: bool, Z: bool):

    if X == True and (Y == True or Z == True):
        
        return "Azione permessa"
    
    else:
        
        return "Azione negata"
    
    
X: bool = True
Y: bool = False
Z: bool = False

print(condizione(X,Y,Z))


#Ci torna ci torna.... ci ritorna "Azione permessa" (battutina delle 10 di mattina)

def condizione(numero: int) -> str:
    
    
    valore_1: int = 10
    valore_2: int = 15
    valore_3: int = 20
    
    if (numero == valore_1 or numero == valore_2) and numero < valore_3:
        
        return "Azione permessa"
    
    else:
        
        return "Azione negata"
    
    
    #2) Scrivi una funzione che moltiplica tutti i numeri interi 
    # di una lista che sono minori di un 
    # dato valore intero defi nito threshold.
    
    # threshold -> soglia
    
lista: list[int] = [1, 2, 3, 4]
    
def prodotto(lista: list[int], soglia: int) -> int:
    
    prodotto_cumulato: int = 1
        
    for valore in lista:
        
        if valore > soglia:
            
            continue
        
        else:
            
            prodotto_cumulato = prodotto_cumulato * valore
            #prodotto_cumulato *= valore
            
            """prodotto = 1
            for numero in lista_numeri:
            if numero < threshold:
            prodotto *= numero
            return prodotto"""
        
    return prodotto_cumulato    
            


# scrivi una funzione che calcola il fattoriale di un numero.
# n! = n * (n-1) * (n -2) *...*1
# 5! = 5 * 4 * 3 * 2 * 1


"""
lista: list[int] = [5, 4, 3, 2, 1]
def fattoriale(num: int) ->:
    
    prodotto = int = 1
    
    for valore in lista:
        fatt = num * valore
        
    return fatt
"""

def fattoriale(numero: int) -> int:
    
    prodotto = int = 1
    
    for i in range(numero):
        
        prodotto *= (numero - 1)
        
    return prodotto


# iterazione numero 1: (5 - 0) * 1 -> 5
# iterazione numero 2: (5 - 1) * 5 -> 5 * 4 = 20
# iterazione numero 3: (5 - 2) * 20 -> 3 *20 * 4 = 20

print(fattoriale(numero=100))