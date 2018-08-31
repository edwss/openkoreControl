import signal
import subprocess
import os

class Process:
    def __init__(self):
        self.names = []
        self.process = []

    def listProcess(self):
        print(self.names)

    def add(self, command, name, cwd):
        self.process.append(
            subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True, preexec_fn=os.setsid,
                             cwd=cwd))
        self.names.append(name)

    def kill(self, name):
        try:
            os.killpg(os.getpgid(self.process[self.names.index(name)].pid), signal.SIGTERM)
            print(self.process[self.names.index(name)].pid)
            self.process.remove(self.process[self.names.index(name)])
            self.names.remove(name)
        except:
            pass

    def killAll(self):
        for i in range(0, len(self.names)):
            print(self.process[i].pid)
            os.killpg(os.getpgid(self.process[i].pid), signal.SIGTERM)