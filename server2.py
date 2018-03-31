#!/usr/bin/python3

import sys
from twisted.python import log
from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, Protocol


def ctf_fun(data):
    response = data.decode().rstrip('\n')
    s_response = response.split(',')
    log.msg('We got {}'.format(response))
    if 'SecDSM!' in s_response[1]:
        return "Authentication Successful.\n"
    else:
        return "Authentication failed!  This attempt will be logged...\n"


class CTFServerProtocol(Protocol):
    def dataReceived(self, data):
        log.msg('Data received {}'.format(data))
        d_data = data.decode()

        if 'SecDSM!' in d_data:
            self.transport.write('You are trusted.....\n'.encode())
            self.transport.write('\n'.encode())
            self.transport.write('\n'.encode())
            self.transport.write('Decide to network\n'.encode())
            self.transport.write('\n'.encode())
            self.transport.write('Use every letter you write\n'.encode())
            self.transport.write('Every conversation you have\n'.encode())
            self.transport.write('Every meeting you attend\n'.encode())
            self.transport.write('To express your fundamental beliefs and dreams\n'.encode())
            self.transport.write('Affirm to others the vision of the world you want\n'.encode())
            self.transport.write('Network through thought\n'.encode())
            self.transport.write('Network through action\n'.encode())
            self.transport.write('Network through love\n'.encode())
            self.transport.write('Network through the spirit\n'.encode())
            self.transport.write('You are the center of the world\n'.encode())
            self.transport.write('You are a free, immensely powerful source\n'.encode())
            self.transport.write('of life and goodness\n'.encode())
            self.transport.write('Affirm it\n'.encode())
            self.transport.write('Spread it\n'.encode())
            self.transport.write('Radiate it\n'.encode())
            self.transport.write('Think day and night about it\n'.encode())
            self.transport.write('And you will see a miracle happen:\n'.encode())
            self.transport.write('the greatness of your own life.\n'.encode())
            self.transport.write('In a world of big powers, media, and monopolies\n'.encode())
            self.transport.write('But of six billion individuals\n'.encode())
            self.transport.write('Networking is the new freedom\n'.encode())
            self.transport.write('the new democracy\n'.encode())
            self.transport.write('a new form of happiness.\n'.encode())
            self.transport.write('\n'.encode())
            self.transport.write('Robert Muller\n'.encode())
            self.transport.write('\n'.encode())

        elif "515" in d_data:
            log.msg('FLAG Found!')
            self.transport.write('FLAG-N3tw0rk_c0ding_!$_Fun\n'.encode())

        else:
            greeting = 'Hello {}\nDo I know you?\n'.format(d_data)
            self.transport.write(greeting.encode())

            #result = ctf_fun(data)
            #self.transport.write(result.encode())

    def connectionMade(self):
        log.msg('Client connection from {}'.format(self.transport.getPeer()))
        greeting = 'What is your name?\n\n'
        self.transport.write(greeting.encode())

    def connectionLost(self, reason):
        log.msg('Lost connection because {}'.format(reason))


class CTFServerFactory(ServerFactory):
    def buildProtocol(self, addr):
        return CTFServerProtocol()


def main():
    log.startLogging(sys.stdout)
    #log.startLogging(open('/tmp/py_server.log', 'a'))
    log.msg('Start your engines...')
    reactor.listenTCP(16000, CTFServerFactory())
    reactor.run()


if __name__ == '__main__':
    main()
