from pykeyboard import PyKeyboard
import irc
import time
import thread
from data import cmds

class Simulator:
    def __init__(self):
        self.keyboard = {
        
                "left": "1",
                "right": "2",
                "up":"3",
                "down":"4",
                "a":"5",
                "b":"6",
                "l":"7",
                "select":"8",
                "start":"9",
                "r":"-",
                }
        
    def run(self):
        while True:
            if cmds:
                self.execute(cmds[0])
                cmds.remove(cmds[0])
            time.sleep(1)

    def execute(self, key):
        keyboard = PyKeyboard()
        if key in self.keyboard:
            for x in range(101):
                keyboard.type_string(self.keyboard[key])

if __name__ == "__main__":
    thread.start_new_thread(irc.IRCBot().main, ())
    run = Simulator()
    run.run()
