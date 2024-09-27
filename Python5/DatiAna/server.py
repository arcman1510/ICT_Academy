from flask import Flask, json, request
from myjson import JsonSerialize,JsonDeserialize



sFileAnagrafe = "./anagrafe.json"
api = Flask(__name__)

@api.route('/add_cittadino', methods=['POST'])

def GestisciAddCittadino():
    #prende i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata" + content_type)
    if content_type=="application/json":
        jRequest = request.json
        print(jRequest)
        sCodiceFiscale = jRequest["codice fiscale"]
        print("Ricevuto " + sCodiceFiscale)
        #caricare l'anagrafe
        dAnagrafe = JsonDeserialize(sFileAnagrafe)
        if sCodiceFiscale not in dAnagrafe:
            dAnagrafe[sCodiceFiscale] = jRequest
            JsonSerialize(dAnagrafe,sFileAnagrafe)
            jResponse = {"Error":"00", "Msg": "ok"}
            return json.dumps(jResponse),200
        else:
            jResponse = {"Errore":"001", "Msg": "codice fiscale già inserito"}
            return json.dumps(jResponse),200
    else:
        return "Errore, formato non riconosciuto", 401
    
api.run(host="127.0.0.1", port=8080)