from User import User

class Student(User):
    classes = []

    def takeClass (self, subject):
        self.classes.append(subject)

    def dropClass (self, subject):
        self.classes.remove(subject)