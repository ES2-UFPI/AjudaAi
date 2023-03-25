import smtplib
import mimetypes
from email.utils import make_msgid
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

autenticacao = {
    'login': 'nao.responder.ajudaai@gmail.com',
    'senha': 'gqxuhvqqypshpwha'
}


def enviar_email_para(assunto, addr, corpo_email, server_email):
    msg = MIMEMultipart('principal')
    image_cid = make_msgid()

    msg['To'] = addr
    msg['Subject'] = assunto
    msg['From'] = f"AjudaAi {autenticacao['login']}"
    msg.add_header('Content-Type', 'text/html')
    msg_alternativa = MIMEMultipart('alternativa')
    msg.attach(msg_alternativa)
    border_radius = 0

    msg_text = MIMEText(f'''
        <html lang='pt-br'>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <head>
            <body style="width:90%; margin:auto; background-color: #1a1a2e;">
                <header>
                    <h1 style="padding-top:30px;"><img src="cid:logo" width="100" height="100" style="margin:auto; display:block;"></h1>
                </header>
                <div style="color:#213951; background-color:#1a1a2e; padding:10px 10px 10px 10px;">
                    <div style="border-top:5px solid #7fcecb; margin:0px 1.5%; display:inline-block; width:47%; height:200px">
                    
                    </div>
                    <div style="background-color:#7fcecb; margin:5px 1%; display:inline-block; width:47%; height:200px">
                        
                    </div>
                </div>
                <div style="color:#213951; background-color:#1a1a2e; padding:10px 10px 10px 10px;">
                    <div style="background-color:#7fcecb; margin:5px 1.5%; display:inline-block; width:47%; height:200px">
                        
                    </div>
                    <div style="border-top:5px solid #7fcecb; margin:0px 1%; display:inline-block; width:47%; height:200px">
                    
                    </div>
                </div>
                <footer style="background-color: #7fcecb; border-radius: 0px 0px {border_radius}px {border_radius}px;
                        padding:13px 0px;">
                    <p style="color:#1a1a2e; font-size:12px; width: 100%; text-align: center;
                        margin: auto; display:block;">
                        ©2023 AjudaAi   |   Todos os direitos reservados.
                    </p>
                </footer>
            </body>
        </html>
    ''', 'html')
    msg_alternativa.attach(msg_text)

    with open('static/img/remove bg logo.png', 'rb') as img:
        imagem = MIMEImage(img.read())
        imagem.add_header('Content-ID', '<logo>')

    msg.attach(imagem)
    server_email.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))


def enviar_emails(assunto, addr, corpo):
    server_email = smtplib.SMTP('smtp.gmail.com:587')   # conectando ao servidor SMTP do Gmail via TLS
    server_email.starttls()                             # habilita a criptografia na conexão. Se a conexão for SSl, já vem configurado
    server_email.login(autenticacao['login'], autenticacao['senha'])

    for to in addr:
        enviar_email_para(assunto, to, corpo, server_email)
    server_email.close()
    
    
enviar_emails('Teste caio', ['caiofeitosa@ufpi.edu.br'], 'Testando 123')
