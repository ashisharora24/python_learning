class Teacher:

    def setID(self, id):
        self.id = id

    def getID(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

class Student(Teacher):

    def setRollNumber(self, rollnumber):
        self.rollnumber = rollnumber

    def getRollNumber(self):
        return self.rollnumber


s = Student()
s.setID(1)
s.setName("ashish")
s.setRollNumber(1234)

print(s.getID())
print(s.getName())
print(s.getRollNumber())
