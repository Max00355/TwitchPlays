import socket
from data import cmds

class IRCBot:
    def __init__(self):
        self.channel = ""
        self.host = "irc.twitch.tv"
        self.port = 6667
        self.name = ""
        self.password = ""
        self.possible = ["left", "right", "a", "b", "up", "down", "start", "l", "r", "select"]

    def main(self):
        
        sock = socket.socket()
        sock.connect((self.host, self.port))
        sock.send("PASS {0}\r\n".format(self.password))
        sock.send("NICK {0}\n\r".format(self.name)) 
        sock.send("USER {0} {0} {0}: {0}\r\n".format(self.name))
        sock.send("JOIN {0}\r\n".format(self.channel))
        while True:
            data = sock.recv(1024)
            if "PING" in data:
                sock.send("PONG\r\n")
            if __name__ == "__main__":
                print data
            data = data.split(" :")
            if len(data) > 1:
                data[1] = data[1].lower()
                data[1] = data[1].replace("\n", '').replace("\r", '')
                if data[1] in self.possible:
                    print data[1]
                    cmds.append(data[1])

if __name__ == "__main__":
    IRCBot().main()
