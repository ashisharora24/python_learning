class Automobile:

    # this is class variable
    objectCount = 0

    # this is constructor and is used to initiate instance variable
    # it can also  act upon class variable
    def __init__(self, type="land_Vehicle", tyresCount = 4):
        Automobile.objectCount += 1
        self.type = type
        self.tyresCount = tyresCount

    def setCompany(self, company = "maruti"):
        self.company = company
        print("id(company) : ", id(company))
        print("id(self.company) : ", id(self.company))
    def setTyresCount(self, tyresCount = 4):
        self.tyresCount = tyresCount
        print("id(tyreCount) : ", id(self.tyresCount))
    def getCompany(self):
        return self.company
    def getTyresCount(self):
        return self.tyresCount

    def increaseTyre(self):
        self.tyresCount+=1
        print("id(self.tyre..) : ", id(self.tyresCount))


    # this is instance month
    def price(self):
        if self.tyres==1:
            return 1000
        elif self.tyres==2:
            return 2000
        elif self.tyres==3:
            return 3000
        else:
            return 4000

    @classmethod
    def classObjectCheck(cls):
        return cls.objectCount

    # static method
    @staticmethod
    def staticObjectCheck():
        return Automobile.objectCount

# calling static method:
# Classname.StaticMethod()
Automobile.staticObjectCheck()


# you can call class variable directly as
#  Classname.variable
print(Automobile.objectCount)

# you can call class methods directly as
#  Classname.methodname
print(Automobile.classObjectCheck())


# creating the class object to start instance
s1 = Automobile()
typreCount1 = 5
print("id(typreCount1) : ", id(typreCount1))
s1.setTyresCount(typreCount1)
s1.increaseTyre()
print("id(typreCount1) : ", id(typreCount1))
print(typreCount1)
print(s1.getTyresCount())
