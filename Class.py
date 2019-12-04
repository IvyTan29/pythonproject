class Class:
    name = ""
    unit = ""
    limit = ""
    classcode = ""
    prerequisites = []
    students = []

    def __init__(self, unit, name, limit, classcode): 
        self.unit = unit
        self.name = name
        self.limit = limit
        self.classcode = classcode

    def addPrerequisite (self, classcode):
        self.prerequisites.append(classcode)

    def addStudent (self, student):
        self.students.append(student)

    def addStudent (self, student):
        self.students.remove(student)

    def isFull (self):
        return self.limit == len(self.students)
