class Emp:

    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID : ", self.id)
        print("Name  : ", self.name)
        print("Salary : ", self.salary)


class MyClass:

    @staticmethod
    def mymethod(e):
        e.salary += 1000
        e.display()


e = Emp(10, "Ashish", 10000)
e.display()
MyClass.mymethod(e)
