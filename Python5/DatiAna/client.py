import json, requests
import sys


base_url = "http://127.0.0.1:8080"

def RichiediDatiCittadino():
    nome = input("inserisci nome cittadino: ")
    cognome = input("inserisci conome cittadino: ")
    dataNascita = input("inserisci data di nascita: ")
    cf = input("inserisci codice fiscale: ")
    jRequest = {"nome": nome, "cognome":cognome, "dataNascita":dataNascita, "codiceFiscale": cf}
    return jRequest


def CreaInterfaccia():
    print("Operazioni Disponibili")
    print("1. Inserisci cittadino (es. anno di nascita)")
    print("2. Richiedi dati cittadino (es. cert. residenza")
    print("3. Modifica dati cittadino")
    print("4. Elimina cittadino")
    print("5. Exit")

CreaInterfaccia()
s0per = input("seleziona operazione")
while (s0per != "5"):
    if s0per=="1":
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = RichiediDatiCittadino()
        try:
            response = requests.post(api_url, json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("Problemi di comunicazione con il server, ripristina")
        CreaInterfaccia()
        s0per = input("Selzinona")
