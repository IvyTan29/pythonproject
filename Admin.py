from Class import Class
from User import User

class Admin(User):

    def addClass (self, enlistment):
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
                subcode = input ("What class code is the prerequisite? ")
                subject.addPrerequisite(subcode)
            else:
                ifPreReq = False

        enlistment.addClass(subject)

    def removeClass (self, enlistment):
        enlistment.viewClasses()
        choice = input ("\nChoose class to delete: ")
       
        while not(choice >= '1' and choice <= str(len(enlistment.getClasses()))):
            print ("Invalid Input! Try again.")
            choice = input ("\nChoose class to delete: ")
        
        enlistment.removeClass(enlistment.getClasses()[int(choice)-1])

