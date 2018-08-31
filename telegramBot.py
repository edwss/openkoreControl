import os
from telegram.ext import Updater
from telegram.ext import CommandHandler
from datetime import datetime
import Process
import Openkore

directory = os.listdir('inventory/')
for i in range(0, len(directory)):
    print(directory[i])
    os.remove('inventory/' + directory[i])
directory = os.listdir('storage/')
for i in range(0, len(directory)):
    print(directory[i])
    os.remove('storage/' + directory[i])
directory = os.listdir('console/')
for i in range(0, len(directory)):
    print(directory[i])
    os.remove('console/' + directory[i])

# Token from Bot
updater = Updater(token='')
dispatcher = updater.dispatcher


def quitCommand(bot, update, args):
    name = args[0]
    b.stop(name)
    string = ""
    string += "Bot(" + name + ") Finalizado"
    bot.send_message(chat_id=update.message.chat_id, text=string)


def activeCommand(bot, update):
    string = ""
    string += "---- Lista de bots ativos ----\n"
    array = b.active()
    for i in range(0, len(array)):
        string += array[i] + '\n'
    bot.send_message(chat_id=update.message.chat_id, text=string)


def showStorage(bot, update, args):
    files = os.listdir('./storage/')
    for i in range(0, len(files)):
        if (args[0] in files[i]):
            with open('./storage/' + args[0] + '.txt') as file:
                string = ""
                string += "---- Mostrando storage(" + args[0] + ") ----\n"
                string += file.read()
                bot.send_message(chat_id=update.message.chat_id, text=string)


def showInventory(bot, update, args):
    files = os.listdir('./inventory/')
    for i in range(0, len(files)):
        if (args[0] in files[i]):
            with open('./inventory/' + args[0] + '.txt') as file:
                string = ""
                string += "---- Mostrando inventario(" + args[0] + ") ----\n"
                string += file.read()
                bot.send_message(chat_id=update.message.chat_id, text=string)


def readConsole(bot, update, args):
    string = ""
    files = os.listdir('./console/')
    for i in range(0, len(files)):
        if (args[0] in files[i]):
            fileHandle = open('./console/' + args[0] + '.txt')
            fileLines = fileHandle.readlines()
            fileHandle.close()
            string += "---- Mostrando 5 linhas do console ----\n"
            for l in range(-6, -1):
                if l != -2:
                    string += fileLines[l][4:-5] + '\n'
                else:
                    string += fileLines[l][4:5]
            bot.send_message(chat_id=update.message.chat_id, text=string)


def showBotList(bot, update):
    botList = b.showBotList()
    string = ""
    string += '---- Lista de bots disponiveis ----\n'
    for i in range(0, len(botList)):
        string += botList[i] + '\n'
    bot.send_message(chat_id=update.message.chat_id, text=string)


def startCommand(bot, update, args):
    string = ""
    name = args[0]
    option = args[1]
    if (b.checkBot(name)):
        b.start(option, name)
        string += "---- Bot(" + name + ") iniciado ----"
        bot.send_message(chat_id=update.message.chat_id, text=string)


def commandList(bot, update):
    string = ""
    string += "/quit botname - Kill a bot by name\n"
    string += "/start botname option - Start a bot by name with options 2 - Without Proxy 3 - With Proxy\n"
    string += '/botList - Show the avaliable bots to run\n'
    string += '/storage botname - Show storage by name\n'
    string += '/inventory botname - Show inventory by name\n'
    string += '/console botname - Show the last 5 lines from openkore\n'
    string += '/active - Show running bots\n'
    string += '/item name - Show the amount of item on storage and inventory of all bots\n'
    string += '/block - Show blocked accounts with date and time'
    bot.send_message(chat_id=update.message.chat_id, text=string)


def getItemsTotal(bot, update, args):
    # Working with Morango but not every item
    quantity = 0

    directory = os.listdir('inventory/')

    for i in range(0, len(directory)):
        with open('inventory/' + directory[i], 'r') as file:
            text = file.readlines()
        for i in range(0, len(text)):
            if args[0] in text[i][:-1]:
                text_split = text[i][:-1].split(' ')
                quantity += int(text_split[2])

    directory = os.listdir('storage/')

    for i in range(0, len(directory)):
        with open('storage/' + directory[i], 'r') as file:
            text = file.readlines()
        for i in range(0, len(text)):
            if args[0] in text[i][:-1]:
                text_split = text[i][:-1].split(' ')
                quantity += int(text_split[2])
    string = ""
    string += "---- Voce possui " + str(quantity) + " de " + args[0] + "----"
    bot.send_message(chat_id=update.message.chat_id, text=string)


def getBlocked(bot, update):
    string = ""
    directory = os.listdir('./console/')
    for i in range(0, len(directory)):
        with open('./console/' + directory[i], 'r') as file:
            lines_formated = []
            lines = file.readlines()
            for l in range(0, len(lines)):
                lines_formated.append(lines[l][4:-5])
                if "exit" in lines_formated[l]:
                    name = directory[i].split('.')
                    b.stop(name[0])
                if "Password Error for account" in lines_formated[l]:
                    login = lines_formated[l].split('[')
                    login = login[1][:-1]
                    with open('blocked.txt', 'a') as file:
                        file.write(login + " - " + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + '\n')
    with open('blocked.txt', 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines)):
            string += lines[i] + '\n'
    bot.send_message(chat_id=update.message.chat_id, text=string)


def addProxy(bot, update, args):
    name = args[0]
    proxy = args[1].split(':')
    proxyHost = proxy[0]
    proxyPort = proxy[1]
    proxyExists = 0

    with open(b.getcwd() + 'control/' + name + '.txt', 'r') as file:
        lines = file.readlines()
        file.close()
        for i in range(0, len(lines)):
            if 'koreProxy_ip' in lines[i]:
                with open(b.getcwd() + 'control/' + name + '.txt', 'w') as file:
                    lines[i] = "koreProxy_ip " + proxyHost + '\n'
                    file.writelines(lines)
                file.close()
                proxyExists += 1
            if 'koreProxy_port' in lines[i]:
                with open(b.getcwd() + 'control/' + name + '.txt', 'w') as file:
                    lines[i] = "koreProxy_port " + proxyPort + '\n'
                    file.writelines(lines)
                file.close()
                proxyExists += 1

    if proxyExists != 2:
        with open(b.getcwd() + 'control/' + name + '.txt', 'r') as file:
            lines = file.readlines()
            file.close()
            for i in range(0, len(lines)):
                if 'koreProxy_ip' in lines[i]:
                    lines.remove(lines[lines.index(lines[i])])
                if 'koreProxy_port' in lines[i]:
                    lines.remove(lines[lines.index(lines[i])])

        with open(b.getcwd() + 'control/' + name + '.txt', 'w') as file:
            lines.append("koreProxy_ip " + proxyHost + '\n')
            lines.append("koreProxy_port " + proxyPort + '\n')
            lines.append("koreProxy_timeout 20\n")
            lines.append("koreProxy_protocol 20\n")
            file.writelines(lines)
            file.close()


proxyHandler = CommandHandler('proxy', addProxy, pass_args=True)
getItemHandler = CommandHandler('item', getItemsTotal, pass_args=True)
commandHandler = CommandHandler('commands', commandList)
quitHandler = CommandHandler('quit', quitCommand, pass_args=True)
startHandler = CommandHandler('start', startCommand, pass_args=True)
botListHandler = CommandHandler('botList', showBotList)
activeHandler = CommandHandler('active', activeCommand)
storageHandler = CommandHandler('storage', showStorage, pass_args=True)
inventoryHandler = CommandHandler('inventory', showInventory, pass_args=True)
consoleHandler = CommandHandler('console', readConsole, pass_args=True)
blockHandler = CommandHandler('block', getBlocked)

dispatcher.add_handler(proxyHandler)
dispatcher.add_handler(getItemHandler)
dispatcher.add_handler(commandHandler)
dispatcher.add_handler(activeHandler)
dispatcher.add_handler(startHandler)
dispatcher.add_handler(botListHandler)
dispatcher.add_handler(quitHandler)
dispatcher.add_handler(storageHandler)
dispatcher.add_handler(inventoryHandler)
dispatcher.add_handler(consoleHandler)
dispatcher.add_handler(blockHandler)

t = Process.Process()
b = Openkore.Bot(t)

try:
    t.listProcess()
    updater.start_polling()
    updater.idle()
    t.killAll()
except KeyboardInterrupt:
    quit()
