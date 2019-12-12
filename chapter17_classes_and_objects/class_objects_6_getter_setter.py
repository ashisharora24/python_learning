class Student:

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

n = int(input("Enter the number of students : "))
i = 0
while (i<n):
    s = Student()
    s.setName(input("enter name : "))
    s.setMarks(int(input("enter marks : ")))

    print("Name Entered : ", s.getName())
    print("marks Entered : ", s.getMarks())

    i+=1
