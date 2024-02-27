from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

#Definir a pasta onde vamos guardar imagens
UPLOAD_FOLDER = os.path.join(app.root_path,"static")
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route('/',methods=['GET','POST'])
def upload_imagem():
    if request.method=='GET':
        return render_template("index.html")
    if request.method=='POST':
        #o ficheiro enviado
        ficheiro=request.files['ficheiro']
        nome=secure_filename(ficheiro.filename)
        ficheiro.save(os.path.join(app.config['UPLOAD_FOLDER'],nome))
        #mostrar a imagem ao utilizador
        return f"Imagem {nome} enviada com sucesso! <img src='static/{nome}' />"
    

app.run()