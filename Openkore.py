import time

debug = False

class Bot:
    def __init__(self, process):
        self.process = process
        with open('./config/folders.txt', 'r') as file:
            lines = file.readlines()
        self.activeBot = []
        self.names = []
        self.diretoriesOpenkore = []
        self.realDirectories = []
        i = 0
        while i < len(lines):
            if 'bot_name' in lines[i]:
                name = lines[i].split(' ')
                self.names.append(name[2][:-1])
            if 'openkore_folder' in lines[i]:
                folder = lines[i].split(' ')
                self.diretoriesOpenkore.append(folder[2][:-1])
            if 'real_folder' in lines[i]:
                folder = lines[i].split(' ')
                self.realDirectories.append(folder[2][:-1])
            i += 1
        if not debug:
            self.cwd = self.realDirectories[0] + self.diretoriesOpenkore[0]
            self.process.add("perl src/Poseidon/poseidon.pl &", "Poseidon", self.cwd)
            time.sleep(10)

    def start(self, option, name=''):
        if "1" in option:
            print("Inicando todos bots")
            # Running all registered bots in lootMode
            for i in range(0, len(self.names)):
                self.process.add(
                    "perl openkore.pl --config=control/" + self.names[i] + ".txt  >  ../console/" + self.names[
                        i] + ".txt &", self.names[i] + " Openkore", self.cwd)
                self.activeBot.append(self.names[i])
        if "2" in option:
            print("Iniciando bot:" + name)
            # Running an specific bot by name
            self.process.add("perl openkore.pl --config=control/" + name + ".txt  > ../console/" + name + ".txt &",
                             name + " Openkore", self.cwd)
            self.activeBot.append(name)
        if "3" in option:
            print("Iniciando bot:" + name + " with PROXY")
            # Running an specific bot by name
            self.process.add(
                "perl openkore.pl --config=control/" + name + ".txt --sys=control/sys2.txt > ../console/" + name + ".txt &",
                name + " Openkore", self.cwd)
            self.activeBot.append(name)

    def active(self):
        # Return the list of active bots
        return self.activeBot

    def showBotList(self):
        # Return the list of possibles bots to run
        return self.names

    def checkBot(self, name):
        # Check if the typed bot is in the list
        for i in range(0, len(self.names)):
            if name in self.names[i]:
                return 1

    def stop(self, name):
        # Kill the bot by name
        try:
            self.activeBot.remove(name)
            self.process.kill(name + " Openkore")
        except:
            pass

    def getcwd(self):
        return self.cwd
