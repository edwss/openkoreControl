Foi somente testado em ambiente linux até então.

Configure o arquivo dentro da pasta config.

bot_name = "botname" sem as aspas. Para adicionar mais bots.
openkore_folder é a localização onde está a pasta do openkore.
real_folder é onde está a aplicação em python.

bot_name = botname irá rodar o openkore com o pametro --config=botname.txt, portanto além de adicionar esse parametro na config é necessário a adição de um arquivo de configuração dentro da pasta config do openkore.

No arquivo telegramBot adicione o token do bot gerado pela api do telegram.

Dentro da pasta plugin existe um plugin que faz uma cópia dos eventos gerados pelo openkore, lá é necessário alterar o diretório onde se encontra o código log.py. Exemplo: no meu caso o arquivo log.py se encontra em : "/home/eduardo/botControl/log.py"

Além disso é necessário a utilização do multiposeidon, a remoção das cores do console.


