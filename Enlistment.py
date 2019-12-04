from Admin import Admin
from Student import Student

class Enlistment:
    classes = []
    users = []
    currentUser =""
    
    def logIn (self, idnumber, password, index):
        if (self.users[index].getPassword() != password):
            return False
        else:
            self.currentUser = self.users[index]
            return True

    def getClasses (self):
        return self.classes

    def getUsers (self):
        return self.users

    def getCurrentUser (self):
        return self.currentUser
    
    def setCurrentUser (self, user):
        self.currentUser = user

    def addUser (self, user):
        self.users.append(user)

    def LogInPage (self):
        print("\t\t\tLog-In")
        ans = input ("\nAre you new to this enlistment system? (y/n) ")

        while not(ans.lower() == 'y' or ans.lower() == 'n'):
            print ("Invalid Input! Try again.")
            ans = input ("Are you new to this enlistment system? (y/n) ")

        idnumber = input ("Enter ID Number: ")
        password = input ("Enter Password: ")

        isFound = False
        index = -1
        i = 0
        for i in range(len(self.users)):
            if (self.users[i].getIDNumber() == idnumber):
                isFound = True
                index = i

        if (isFound and ans == 'y'):
            print ("\nThe system detected that your ID number have already been registered.")
            ans = 'n'

        if (not isFound and ans == 'n'):
            print ("\nThe system detected that your ID number have not been registered.")
            ans = 'y'
            print ("Proceed to the initial registration part.")

        if (ans.lower() == 'y'):
            usertype = input ("\nAre you an admin or student? (a/s) ")

            while not(usertype.lower() == 'a' or usertype.lower() == 's'):
                print ("Invalid Input! Try again.")
                usertype = input ("Are you an admin or student? (a/s) ")

            if (usertype.lower() == 'a'):
                user = Admin (idnumber, password)
            elif (usertype.lower() == 's'):
                user = Student (idnumber, password)

            index = len(self.users)
            self.addUser(user)
            self.setCurrentUser(user)

        elif (ans.lower() == 'n'):
            while not self.logIn(idnumber,password, index):
                print ("\nPassword and ID Number does not match")
                password = input ("Retype Password: ")
            
            print ("Log-in successful!")

    def viewClasses (self):
        i = 1
        if (len(self.classes) == 0):
            print ("No classes to display.")
        
        else :
            for i in range(len(self.classes)):
                print ("\t\t[",i,"] ", self.classes[i-1])