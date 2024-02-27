from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

#configuração do servidor de emails
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '6bd237da07383e'
app.config['MAIL_PASSWORD'] = 'c0480541862fce'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail=Mail(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/enviar_email',methods=["POST"])
def enviar_email():
    email_destino=request.form.get('email')
    assunto=request.form.get('assunto')
    texto=request.form.get('texto')
    mensagem=Message(assunto,
                     sender='meu_email@gmail.com',
                     recipients=[email_destino])
    mensagem.body=texto
    mail.send(mensagem)
    return "Email enviado com sucesso"

app.run(debug=True)