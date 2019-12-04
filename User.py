class User:
    idnumber = ""
    password = ""

    def __init__(self,idnumber,password):
        self.idnumber = idnumber
        self.password = password

    
    def getIDNumber(self) :
        return self.idnumber

    def getPassword(self) :
        return self.password

