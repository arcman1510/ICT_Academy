import json, requests, sys


base_url = "http://127.0.0.1:8080"


def CreaInterfaccia():
    print("Operazioni Disponibili")
    print("1. Inserisci cittadino (es. anno di nascita)")
    print("2. Richiedi dati cittadino (es. cert. residenza")
    print("3. Modifica dati cittadino")
    print("4. Elimina cittadino")
    print("5. Exit")

def GetDatiCittadino():
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    dataN = input("Inserisci la data di nascita (gg/mm/aaaa): ")
    codF = input("Inserisci il codice fiscale: ")
    datiCittadino = {
        "nome": nome, 
        "cognome": cognome, 
        "dataNascita": dataN, 
        "codFiscale": codF
    }
    return datiCittadino


def RichiediDatiCittadino():
    nome = input("inserisci nome cittadino: ")
    cognome = input("inserisci conome cittadino: ")
    dataNascita = input("inserisci data di nascita: ")
    cf = input("inserisci codice fiscale: ")
    jRequest = {"nome": nome, "cognome":cognome, "data nascita":dataNascita, "codice fiscale": cf}
    return jRequest

def GetCodicefiscale():
    cod = input('Inserisci codice fiscale: ')
    return {"codFiscale": cod}

CreaInterfaccia()
sOper = input("seleziona operazione")
while (s0per != "5"):
    if s0per == 1:
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = RichiediDatiCittadino()
        try:
            response = requests.post(api_url, json=jsonDataRequest)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")
        
    elif sOper == 2:
        print("Richiesta dati cittadino")
        api_url = base_url + "/read_cittadino"
        jsonDataRequest = GetCodicefiscale()
        response = requests.get(api_url + "/" + jsonDataRequest['codFiscale'])
        print(response.json())

    elif sOper == 3:
        print("Modifica cittadino")
        api_url = base_url + "/update_cittadino"
        jsonDataRequest = GetDatiCittadino()
        response = requests.post(api_url, json=jsonDataRequest)
        print(response.json())


    elif sOper == 4:
        print("Eliminazione cittadino")
        api_url = base_url + "/elimina_cittadino"
        jsonDataRequest = GetCodicefiscale()
        response = requests.post(api_url, json=jsonDataRequest)
        print(response.json())


    elif sOper == 5:
        print("Buona giornata!")
        sys.exit()
        
        
        CreaInterfaccia()
        s0per = input("Selzinona")
