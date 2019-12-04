from Class import Class
from User import User

class Admin(User):

    def addClass (self):
        name = input ("Name of class: ")
        unit = input ("How many units is this class? ")
        classcode = input ("What is the class code of this class? ")
        limit = input ("How many students can this class hold? ")

        subject = Class(unit,name,limit,classcode)

        ifPreReq = True
        while ifPreReq:
            ans = input ("Are there any prerequisites for this class? (y/n) ")
            while not(ans.lower() == 'y' or ans.lower() == 'n'):
                print ("Invalid Input! Try again.")
                ans = input ("Are there any prerequisites for this class? (y/n) ")
            
            if (ans.lower() == 'y'):
                subcode = input ("What subject code is the prerequisite? ")
                subject.addPrerequisite(subcode)
            else:
                ifPreReq = False

        return subject

    #def removeClass (self):
