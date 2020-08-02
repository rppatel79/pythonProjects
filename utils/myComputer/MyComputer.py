from requests import get
import socket


class MyComputer:
    class __MyComputerSingleton:
        def __init__(self):
            hostname = socket.gethostname()
            self.internalIp = socket.gethostbyname(hostname)
            self.externalIp = get('https://api.ipify.org').text
            print("Internal IP: " + self.internalIp)
            print("External IP: " + self.externalIp)

    singletonInstance = __MyComputerSingleton()

    def __init__(self):
        if not MyComputer.singletonInstance:
            MyComputer.singletonInstance = MyComputer.__MyComputerSingleton()

    def getInternalIp(self):
        return self.singletonInstance.internalIp

    def getExternalIp(self):
        return self.singletonInstance.externalIp


if __name__ == '__main__':
    myComputer = MyComputer()
    print(myComputer.getExternalIp())
    print(myComputer.getInternalIp())
