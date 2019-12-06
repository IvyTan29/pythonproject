class Class:
    name = ""
    unit = ""
    limit = ""
    classcode = ""

    def __init__(self, unit, name, limit, classcode): 
        self.unit = unit
        self.name = name
        self.limit = limit
        self.classcode = classcode
        self.prerequisites = []
        self.students = []
    
    def getName (self):
        return self.name

    def getUnit (self):
        return self.unit

    def getLimit (self):
        return self.limit

    def getClassCode (self):
        return self.classcode

    def getPrerequisites (self):
        return self.prerequisites

    def getStudents (self):
        return self.students

    def addPrerequisite (self, classcode):
        self.prerequisites.append(classcode)

    def addStudent (self, student):
        self.students.append(student)

    def removeStudent (self, student):
        self.students.remove(student)

    def isFull (self):
        if (int(self.limit) == len(self.students)):
            return True
        else:
            return False

    def donePrerequisite (self, strPrereq):
        return strPrereq in self.prerequisites

    def __str__ (self):
        string = self.name + "\n\t\t       Class Code: " + self.classcode + "\n\t\t       Unit: " + self.unit + "\n\t\t       Limit: " + self.limit + "\n\t\t       Current Count: " + str(len(self.students)) + "\n\t\t       Prerequisites:"

        for prereq in self.prerequisites:
            string += "\n\t\t       "
            string += prereq
        
        return string
