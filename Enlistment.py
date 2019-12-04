class Enlistment:
    classes = []
    users = []
    
    def logIn (self, idnumber, password):
        isFound = False
        index = ""
        i = 0
        for i in range(len(users)):
            if (self.user[i].getIDNumber() == idnumber):
                isFound = True
                index = i
        
        if (isFound == False):
            print ("User not found.")
            return False
        else:
            if (self.users[index].getPassword() != password):
                print ("Password Wrong")
                return False
            else:
                return True

    def getClasses (self):
        return classes

    def getUsers (self):
        return users

    def addUser (self, user):
        self.users.append(user)