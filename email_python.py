import smtplib
from email.message import EmailMessage
from email_settings import *

# Configuração de quem envia
EMAIL_ADRESS = ADRESS
EMAIL_PASSWORD = PASSWORD

# Criação do e-mail instanciando EmailMessage (título, quem envia, quem recebe)
title = 'Message for you'
send = EMAIL_ADRESS
receive = ['iury@moakt.cc']

message = EmailMessage()
message['Subject'] = title
message['From'] = send
message['To'] = receive
message.set_content('Apenas uma mensagem de teste para envio de e-mail utilizando Python.')

# Envio de e-mail (Especifica o provedor de e-mail que está sendo utilizado (GMAIL))
server = 'smtp.gmail.com'
port = 465
with smtplib.SMTP_SSL(server,port) as smtp:
    # Realiza o login do e-mail de quem envia e realiza o envio da mensagem
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    smtp.send_message(message)
