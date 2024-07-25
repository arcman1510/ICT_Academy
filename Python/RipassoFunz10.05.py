"""

PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

For example:
Test 	Result

contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))

"""

def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    contatto = {'profile': name, 'email': email, 'telefono': telefono}

    return contatto
contatto1 = create_contact("Lollito Chicano" "chicanofromeastla@hotmail.com")
print(contatto1)


def update_contact(contatto: dict, name: str, email: str =None, telefono: int=None) -> dict:
   
    if contatto['profile'] == name:
        if email:
            contatto['email'] = email
        if telefono:
            contatto ['telefono'] = telefono

    return contatto

contatto1 = update_contact(contatto1, "Lollito Chicano", telefono=420420420420)
print(contatto1)

"""


Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.

For example:
Test 	Result

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))

	

{'Alice': [90, 85], 'Bob': [75]}

print(aggrega_voti([])) 


"""

def aggrega_voti(registro: list[dict]) -> dict:
    nuovo_registro = {}

    for studente in registro:
        nome = studente['name']
        voto = studente['voto']

        if nome in nuovo_registro:
            nuovo_registro[nome].append(voto)
            print(nuovo_registro[nome])
        else:
            nuovo_registro[nome] = [voto]

    return nuovo_registro
print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
