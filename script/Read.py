##this file reads select lines from a credential file but is nto secure yet.

class Read:
    def __init__(self, filename):
        self.filename = filename
        self.__lines__ = []
        self.read()

    def read(self):
        with open(self.filename) as file:
            self.__lines__ = [line.strip() for line in file.readlines()]

    def client_ID(self):
        return self.__lines__[1]

    def client_secret(self):
        return self.__lines__[3]

    def password(self):
        return self.__lines__[5]

    def user_agent(self):
        return self.__lines__[7]

    def user_name(self):
        return self.__lines__[9]

