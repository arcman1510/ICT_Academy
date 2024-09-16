from flask import Flask, render_template

api = Flask(__name__)

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/regok', methods=['GET'])
def regok():
    return render_template('reg_ok.html')

@api.route('/regko', methods=['GET'])
def regko():
    return render_template('regko.html')

@api.route('/registrati', methods=['GET'])
def registra():
    return render_template('reg_ok.html')


api.run(host="127.0.0.1", port=8085)