from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#dados
opcoes = {
    "frutas" : ["Maçã","Banana","Laranja"],
    "carros" : ["ford","fiat","ferrari"]
}

#serviço web
@app.route('/get_opcoes',methods=["GET"])
def get_opcoes():
    categoria = request.args.get('categoria')
    if categoria and categoria in opcoes:
        return jsonify(opcoes[categoria])
    return jsonify([])

@app.route('/json')
def json():
    dados={'nome':'Joaquim','email':'joaquim@gmail.com','idade':15}
    return jsonify(dados)

app.run(debug=True)