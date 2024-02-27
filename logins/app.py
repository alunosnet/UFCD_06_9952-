from flask import Flask, redirect, request, render_template, session
from flask_session import Session

app=Flask(__name__)

#configuração dos cookies de sessão
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method=="POST":
        #validar as credenciais
        email=request.form.get("email")
        password=request.form.get("password")
        #ISTO DEVIA SER OBTIDO A PARTIR DA BASE DE DADOS
        if email=="joaquim@gmail.com" and password=="12345":
            #iniciar sessão
            session["email"]=email
            session["perfil"]="cliente"
            return redirect("/Privado")
        if email=="admin@gmail.com" and password=="12345":
            #iniciar sessão como admin
            session["email"]=email
            session["perfil"]="admin"
            return redirect("/AreaAdmin")
        mensagem="O login falhou. Tenta novamente."
        return render_template("login.html",mensagem=mensagem)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

############################################################
###### PRIVADO #############################################
@app.route("/Privado")
def privado():
    #verificar se tem sessão iniciada
    if "email" not in session:
        return redirect("/login")
    
    return render_template("privado.html")

#########################################################
##### ADMIN #############################################
@app.route("/AreaAdmin")
def areaadmin():
    #verificar se tem sessão iniciada como admin
    if "perfil" not in session or session["perfil"]!="admin":
        return redirect("/login")
    return render_template("areaadmin.html")

app.run(debug=True)
