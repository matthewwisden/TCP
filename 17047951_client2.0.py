import socket


class Transition:
    def active_open(self):
        print("Error!")
        return False

    def rst(self):
        print("Error!")
        return False

    def timeout(self):
        print("Error!")
        return False

    def syn(self):
        print("Error!")
        return False

    def syn_ack(self):
        print("Error!")
        return False

    def ack(self):
        print("Error!")
        return False

    def closed(self):
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

    def active_open(self):
        print("active opening")
        self.CurrentContext.setState("SYN_Sent")


class syn_Sent(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def rst(self):
        return True

    def timeout(self):
        rst
        return True

    def syn_ack(self):
        return True


class established(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def close(self):
        return True


class fin_wait_1(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def ack(self):
        return True


class fin_wait_2(State, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def fin(self):
        ack
        return True


class time_Wait(state, Transition):
    def __init__(self, Context):
        State.__init__(self, Context)

    def timeout(self):
        return True

def Main():

    # host = "127.0.0.1"
    # port = 5001
    # s = socket.socket()
    # s.connect((host, port))
    # cleartext = input("Message: ")
    # while cleartext != "Q":
    #     cyphertext = ss_encrypt_decrypt(cleartext, "UniversityOfSouthWales", True)
    #     print("Sending: " + cyphertext)
    #     s.send(cyphertext.encode())
    #     cyphertext = s.recv(1024)
    #     print("Decrypting...")
    #     cleartext = ss_encrypt_decrypt(cyphertext.decode(), "UniversityOfSouthWales", False)
    #     print("Received: " + cleartext)
    #     cleartext = input("Message: ")
     s.close()

if __name__=='__main__':
    Main()