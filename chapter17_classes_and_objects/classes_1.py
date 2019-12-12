class Student:

    ''' this class is to handle student details and there related activities'''

    def __init__(self,name = "admin",age=33,year=2016,batch=2):
        self.name = name
        self.age = age
        self.year = year
        self.batch = batch

    def student_details(self):
        print("---------PRINTING DETAILS-----------")
        print("Name = ",self.name)
        print("Age = ",self.age)
        self.age += 1
        print("Age = ",self.age)
        print("Year = ",self.year)
        print("Batch = ",self.batch)
        print("-----------------------------------")
# ---------------------------------

std = Student()
print("std.name : ", std.name)
print("std.age : ", std.age)
print("std.year : ", std.year)
print("std.batch : ", std.batch)
std.student_details()

# update values in this object
std.name = "ashish"
std.age+=1

print("std.name : ", std.name)
print("std.age : ", std.age)
print("std.year : ", std.year)
print("std.batch : ", std.batch)
std.student_details()
# ---------------------------------
print("**************************************************")
print("**************************************************")
# ---------------------------------

std1 = Student("astha",10,10,10)
print("std1.name : ", std1.name)
print("std1.age : ", std1.age)
print("std1.year : ", std1.year)
print("std1.batch : ", std1.batch)
std1.student_details()

# update values in this object
std1.name = "ashish"
std1.age+=1

print("std.name : ", std1.name)
print("std.age : ", std1.age)
print("std.year : ", std1.year)
print("std.batch : ", std1.batch)
std1.student_details()

Student.student_details()
