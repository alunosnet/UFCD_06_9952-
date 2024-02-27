from flask import Flask, redirect, request,render_template, session
from flask_session import Session
import os
from werkzeug.utils import secure_filename

app=Flask(__name__)

app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

#definir a pasta para guardar ficheiros
UPLOAD_FOLDER=os.path.join(app.root_path,"imagens")
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")

    if request.method=="POST":
        #validação das credenciais
        email=request.form.get("email")
        password=request.form.get("palavra_passe")
        if email=="joaquim@gmail.com" and password=="12345":
            #iniciar sessão
            session["email"]=email
            session["perfil"]="admin"
            return redirect("/Privado")
        if email=="maria@gmail.com" and password=="12345":
            #iniciar sessão
            session["email"]=email
            session["perfil"]="user"
            return redirect("/AreaUser")
        mensagem="O login falhou. Tente novamente"
        return render_template("login.html",mensagem=mensagem)

@app.route("/Privado")
def privado():
    #validar sessão
    if "email" not in session:
        return redirect("/login")
    if session["perfil"]!="admin":
        return redirect("/login")
    return render_template("privado.html")

@app.route("/AreaUser")
def areauser():
    #validar sessão
    if "email" not in session:
        return redirect("/login")
    if session["perfil"]!="user":
        return redirect("/login")
    return render_template("areauser.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/upload",methods=["GET","POST"])
def enviar_ficheiro():
    if request.method=="GET":
        return render_template("ficheiros.html")
    else:
        #guardar o ficheiro
        ficheiro = request.files["ficheiro"]
        nome_ficheiro=secure_filename(ficheiro.filename)
        ficheiro.save(os.path.join(app.config["UPLOAD_FOLDER"],nome_ficheiro))
        return "O ficheiro foi guardado com sucesso"
        
app.run()