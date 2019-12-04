class Class:
    name = ""
    unit = ""
    limit = ""
    classcode = ""
    prerequisites = []
    
    def __init__(self, unit, name, limit, classcode): 
        self.unit = unit
        self.name = name
        self.limit = limit
        self.classcode = classcode

    def addPrerequisite (self, classcode):
        self.prerequisites.append(classcode)
