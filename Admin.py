import Class

class Admin(User):

    def addClass (self):
        name = input ("Name of class: ")
        unit = input ("How many units is this class?")
        classcode = input ("What is the class code of this class?")
        limit = input ("How many students can this class hold?")

        subject = Class(unit,name,limit,classcode)

        ifPreReq = True
        while ifPreReq:
            ifPreReq = input ("Are there any prerequisites for this class? (True/False)")
            while not(ifPreReq == True and ifPreReq == False):
                print ("Invalid Input! Try again.")
                ifPreReq = input ("Are there any prerequisites for this class? (True/False)")
            
            if (ifPreReq == True):
                subcode = input ("What subject code is the prerequisite?")
                subject.addPrerequisite(subcode)

        return subject

    #def removeClass (self):
