class Enlistment:
    classes = []
    users = []
    
    def logIn (self, idnumber, password, index):
        if (self.users[index].getPassword() != password):
            return False
        else:
            return True

    def getClasses (self):
        return self.classes

    def getUsers (self):
        return self.users

    def addUser (self, user):
        self.users.append(user)