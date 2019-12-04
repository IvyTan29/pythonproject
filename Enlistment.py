class Enlistment:
    classes = []
    user = []

    def logIn (self, idnumber, password):
        isFound = False
        index = ""
        i = 0
        for i in range(len(user)):
            if (self.user[i].getIDNumber() == idnumber):
                isFound = True
                index = i
        
        if (isFound == False):
            print ("User not found.")
            return False
        else:
            if (self.user[index].getPassword() != password):
                print ("Password Wrong")
                return False
            else:
                return True
        
    def setUser (self, user):
        self.user = user