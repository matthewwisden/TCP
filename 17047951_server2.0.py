import socket


class Transition:
    def passive_open(self):
        print("Error!")
        return False

    def syn(self):
        print("Error!")
        return False

    def ack(self):
        print("Error!")
        return False

    def syn_ack(self):
        print("Error!")
        return False

    def fin(self):
        print("Error!")
        return False

    def fin(self):
        print("Error!")
        return False

    def timeout(self):
        print("Error!")
        return False


class closed(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def closed(self):
        print("At closed state")
        return True

    def passive_open(self):
        print("passive opening")
        self.CurrentContext.setState("LISTEN")
        return True


class listen(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def syn(self):
        syn_ack
        return True


class syn_Rec(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def ack(self):
        return True


class established(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def fin(self):
        ack
        return True


class close_wait(State, Transition):
    def close(self):
        fin
        return True


class last_Ack(State, Transition):
    def timeout(self):
        return True


class server(statecontect, Transition):
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 5001
        self.availableStates["CLOSED"] = closed(self)
        self.availableStates["LISTEN"] = listen(self)
        self.availableStates["SYN_REC"] = syn_Rec(self)
        self.availableStates["ESTABLISHED"] = established(self)
        self.availableStates["CLOSE_WAIT"] = close_wait(self)
        self.availableStates["LAST_ACK"] = last_Ack(self)
        print("CLOSING STATE")
        self.setState("IDLE")

    def closed(self):
        return self.CurrentState.closed()

    def listen(self):
        self.socket = socket()
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            self.connection, self.connection_address = self.socket.accept()  # connection acceptance
            return True
        except Exception as err:
            print(err)
            exit()

    def syn_Rec(self):
        return self.CurrentState.syn_Rec()

    def established(self):
        return self.CurrentState.established()

    def established(self):
        self.socket = socket()
        try:
            self.socket.connect((self.host, self.port))
            self.connection_address = self.host
        except Exception as err:
            print(err)
            exit()

        def close_wait(self):
            return self.CurrentState.close_wait()

        def last_Ack(self):
            return self.CurrentState.last_ack()

if  __name__ == '__main__':
    if len(argv) < 2:
        argv.append("client")

    activeServer



if __name__ == '__main__':
    Main()