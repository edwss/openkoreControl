from telegram.ext import Updater
from telegram.ext import CommandHandler
import sys
import os
import time
String = []

reload(sys)
sys.setdefaultencoding('utf8')

updater = Updater(token='')

for i in range(1,len(sys.argv)):
        String.append(sys.argv[i])

String_final = ""
stringName = String[1].split('_')
stringName = stringName[1]
String[1] = stringName
if("0" in String[0]):
    i = 2
    cont = len(String)
    with open('../storage/'+String[1]+'.txt','w') as file:
        file.close()
    while(i < cont):
        with open('../storage/'+String[1]+'.txt','a') as file:
            try:
                file.write(String[i]+","+String[i+1]+'\n')
            except Exception as e:
                pass
        file.close()
        i += 2

if("1" in String[0]):
    String_final += "Nome: "+ String[1] + '\n'
    String_final += "Base Level: "+ String[2] + '\n'
    String_final += "Job Level: "+ String[3] + '\n'

    updater.bot.send_message(chat_id=507188149, text=String_final)

    i = 4
    cont = len(String)
    print(String)
    with open('../inventory/'+String[1]+'.txt','w') as file:
        file.close()

    while(i < cont):
        with open('../inventory/'+String[1]+'.txt','a') as file:
            try:
                file.write(String[i]+","+String[i+1]+'\n')
            except Exception as e:
                pass
        file.close()
        i += 2

if("2" in String[0]):
    with open('../disconnect/' + String[1] + '.txt', 'a') as file:
        disconnectTime = time.strftime('%d-%m-%Y,%H:%M:%S', time.localtime())
        file.write(String[1] + ',' + disconnectTime + '\n')
    file.close()

if("3" in String[0]):
    i = 2
    cont = len(String)
    with open('../inventory/'+String[1]+'.txt','w') as file:
        file.close()

    while(i < cont):
        with open('../inventory/'+String[1]+'.txt','a') as file:
            try:
                file.write(String[i]+","+String[i+1]+'\n')
            except Exception as e:
                pass
        file.close()
        i += 2
