class Masterkey:
    def __init__(self, args):
        self.args = args
        pass
    def add(self):
        lockname = str(input('Ingrese nombre o codigo del candado: '))
        username = str(input('Username: '))
        password = str(input('Password: '))

        print(lockname, username, password)
        pass
    def remove(self, lockname):
        pass
    def get(self, lockname):
        pass