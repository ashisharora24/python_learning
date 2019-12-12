class Father:


    def __init__(self):
        self.property = 5000

class Son1(Father):

    def display(self):
        print("Son1 : ", self.property)


class Son2(Father):

    def __init__(self):
        self.property = 10000


    def display(self):
        print("Son2 : ", self.property)

s1 = Son1()
s1.display()
s2 = Son2()
s2.display()
