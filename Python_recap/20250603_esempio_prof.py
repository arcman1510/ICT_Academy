list_1: list = [1, 2, 3, 4, 5]
list_2: list = ["Ciao", 1, 2.55, True, False, [1, 2, [5, 6, 7, 8]]]
list_1[0] = 1000


print(f"Il valore interno è: {list_2[5][2][0]}")
print(f"Il valore è: {list_2[0]}")

list_2.append([1, 2, 3])
#elemento_rimosso = list_2.pop(0)

#print(elemento_rimosso)
print(list_2)


print(list_2[0:3])

tuple_1: tuple = ("Ciao",)
print(f"Il tipo di questa variabile è: {type(tuple_1)}, L'elemento all'indice 0 è {tuple_1[0]}")
#tuple_1[0] = "Flavio"


dict_1: dict = {"key1": 12, "key2": "valore2", "key3": {"key1_2": 23}}

print(dict_1)
dict_1["key1"] = 48
print(dict_1["key3"]["key1_2"])

dict_1["key"] = 12
print(dict_1)


# 1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
#    la chiave è già presente, somma il valore al valore già associato alla chiave.


esempio: list[tuple] = [("Chiave1", "Valore1"), ("Chiave2", "Valore2"), ("Chiave2", "Valore3")]



def funzione(lista_di_tuple: list[tuple]) -> dict:
    
    nuovo_dizionario: dict = {}
    
    for element in lista_di_tuple:
        
        chiave = element[0]
        valore = element[1]
        
        if chiave in nuovo_dizionario:
            
            nuovo_dizionario[chiave] += valore
            
        else:
            
            nuovo_dizionario[chiave] = valore
            
    return nuovo_dizionario
        
dizionario: dict = funzione(lista_di_tuple=esempio)
print(dizionario)        



# 2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
#    classifichi i numeri in liste separate per numeri positivi e negativi.

lista_di_numeri: list = [1, 2, -3, 4, -6, 7]

def positivi_negativi(lista_nuova) -> dict:
    
    dizionario: dict = {"positivi": [], "negativi": []}
    
    for element in lista_nuova:
    
        if element >= 0:
            
            dizionario["positivi"].append(element)
            
        else:
            
            dizionario["negativi"].append(element)
            
    return dizionario

elementi_filtrati: dict = positivi_negativi(lista_nuova=lista_di_numeri)
print(elementi_filtrati)



# 3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
#    restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
#    con i prezzi aumentati del 10%.

dizionario_di_prodotti: dict = {"Penna": 1.5, "Righello": 0.85, "Telefono": 500.50}

