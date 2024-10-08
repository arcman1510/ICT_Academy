from flask import Flask, render_template ,request

api = Flask(__name__)

utenti = [["Mario","Rossi","Via della Sierra Nevada, 60","Roma","1985-08-05","0"],["Luigi","Verdi","Viale Europa","Roma","1980-07-07","0"],["pasquale","verdi","via navigli","Milano","1999-16-04","0"]]


@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@api.route('/regok', methods=['GET'])
def regOk():
    return render_template('reg_ok.html')

@api.route('/regko', methods=['GET'])
def regKo():
    return render_template('reg_ko.html')


@api.route('/login', methods=['GET'])
def accedi():
    return render_template('login.html')

@api.route('/registrati', methods=['GET'])
def accedi1():
    return render_template('formreg.html')



@api.route('/registrazione', methods=['GET'])
def registrazione():

    nome = request.args.get("nome")
    cognome = request.args.get("cognome")
    dataNascita = request.args.get("dataNascita")
    indirizzo = request.args.get("indirizzo")
    citta = request.args.get("citta")

    lr : list[str] = [nome,cognome,indirizzo,citta,dataNascita,"0"]
    for i in utenti:
        if lr == i:
                i[-1] = "1"
                return render_template('reg_ok.html')
        
    return render_template('reg_ko.html')


@api.route('/accesso',methods= ['GET'])
def accesso():

    nome = request.args.get("nome")
    cognome = request.args.get("cognome")
    la : list[str] = [nome,cognome]

    for i in utenti:
        if la[0] == i[0] and la[1] == i[1] and i[-1] == "1":
             
            return render_template('acc_ok.html')
    
        return render_template('acc_ko.html')



api.run(host ="0.0.0.0",port=8085)