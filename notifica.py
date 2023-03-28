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
    border_radius = 10

    msg_text = MIMEText(f'''
        <html lang='pt-br'>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <head>
            <body style="width:60%; margin: 0px 20px; margin:auto;">
                <header style="background-color: #213951;
                        border-radius:{border_radius}px {border_radius}px 0px 0px; padding:3px 0px;">
                    <h1><img src="cid:logo" width="100" height="100"
                    style="margin:auto; display:block;"></h1>
                </header>
                <p style="color: #213951; font-size:23px; margin-left: 15px;">
                    {corpo_email}
                </p>
                <footer style="background-color: #213951; border-radius: 0px 0px {border_radius}px {border_radius}px;
                        padding:12px 0px;">
                    <p style="color:rgba(212, 222, 245, 1); font-size:12px; width: 100%; text-align: center;
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