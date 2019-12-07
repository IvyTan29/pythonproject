from User import User

class Student(User):

    def __init__(self, username, password):
        super().__init__(username, password)
        self.classes = []
        self.classesTook = []

    def PrereqCompleted (self, prereqlist):
        found = True

        # if (len(self.classesTook) == 0):
        #     found = False
        # else:
        for string in prereqlist:
            if (string not in self.classesTook):
                found = False
        
        return found

    def takeClass (self, subject):
        try:
            if (subject in self.classes):
                print ("You're currently taking this class!")

            
            elif (subject.isFull()):
                print ("Class is full!")

            elif (not(self.PrereqCompleted(subject.getPrerequisites()))):
                print ("Prerequisites have not been taken yet!")

            else:
                self.classes.append(subject)
                subject.addStudent(self)
        
        except ValueError:
            print("The limit assigned for this class is not in numbers. Please contact the Admin to fix the problem.")
            print ("Adding this class is currently not possible.")

    def dropClass (self, subject):
        self.classes.remove(subject)
        subject.removeStudent(self)

    def getClasses (self):
        return self.classes

    def viewClasses (self):  
        if (len(self.classes) == 0):
            print ("No classes to display.")
        
        else :
            for i in range(len(self.classes)):
                print ("\t\t[",(i+1),"] ", self.classes[i])

    def addPrerequisite (self):
        subject = input ("What class code is the subject you have already taken? ")
        self.classesTook.append(subject)

    def PrereqView (self):
        if (len(self.classesTook) == 0):
            print ("No classes to display.")
        else:
            for string in self.classesTook:
                print (string)
