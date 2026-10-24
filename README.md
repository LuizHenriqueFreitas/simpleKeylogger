### KEYLOGGER

Um key logger é basicamente um mecanismo de espionagem que fica ouvindo algum periférico do    
PC infectado, por exemplo registrando todas as teclas pressionadas pelo usuário.

Um mecanismo como esse pode ser usado para registrar informações em um arquivo de maneira    
sorrateira e conseguir informações confidenciais, desde credenciais de acesso até fofocas   
em mensagens de texto.


---


#### Este projeto

O projeto aqui apresentado é um Keylogger MUITO simples, mesmo assim ele é capaz de munitorar    
o uso de um teclado com alguns tratamentos de captura, como tratando teclas de função, tipo    
[ SPACE ], [ ENTER ], [ ESC ], entre outros, porém, com certeza tem alguma configuração de forma-   
tação melhor do que a que estamos usando.

Arquivos ".pyw" rodam em segundo plano no windows, caso um script como esse seja imbutido em um   
software, e tenha essa terminologia, o windows possívelmente vai deixar o spayware passar livre.

Keyloggers mais avançados conseguem enviar periodicamente os arquivos de log, que são gerados   
conforme o uso do sistema pelos seus usuários.


---


### Como Rodar

Basta ter python instalado em seu computador e rodar o script "keylogger.py" deste repositório,   
enquanto o terminal estiver rodando ele estará ouvindo seu teclado e gravando num arquivo de texto   
chamado "log.txt", esse arquivo texto está no mesmo diretório do script.