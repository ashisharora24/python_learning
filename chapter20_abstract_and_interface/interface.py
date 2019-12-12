from abc import ABC

class Database(ABC):

    def connect(self):
        pass

    def disconnect(self):
        pass

class Oracle(Database):

    def connect(self,input):
        print("Oracle Connect")

    def disconnect(self,input):
        print("Oracle disconnect")

class MSSQL(Database):
    def connect(self,input):
        print("MSSQL connect")

    def disconnect(self,input):
        print("MSSQL disconnect")

print("Connect to database : ")
print("MSSQL or Oracle")
str = input("Enter your selection : ")
classname = globals()[str]
x = classname()
x.connect("ashish")
x.disconnect("arora")
