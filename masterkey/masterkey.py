from .dbconn import DbConn
from .crypt import Crypt
import clipboard

class Masterkey:

    def __init__(self):
        pass
    def add(self):
        lockname = str(input('Ingrese nombre o codigo del candado: '))
        username = str(input('Username: '))
        password = str(input('Password: '))

        db = DbConn()
        db.addAccount(lockname, username, password)
        print('\nThe new account for lock '+lockname+' has been created successfully')
        pass
    def remove(self, lockname):
        pass
    def get(self, lockname):
        db = DbConn()
        data = db.getAccount(lockname)
        input('Should i put the username in the clipboard?[Y]')
        clipboard.copy(data[0])
        input('Should i put the password in the clipboard?[Y]')
        clipboard.copy(data[1])
        return data
    def generatekey(self):
        Crypt().generatekey()
        print('The master.key file has been created')
        pass