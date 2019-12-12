class Person:

    def __init__(self):
        self.name = "Ashish"
        self.db = self.DOB()

    def display(self):
        print("Name : ", self.name)

    class DOB:

        def __init__(self):
            self.dd = 10
            self.mm = 5
            self.yy = 1988

        def display(self):
            print('DOB = {}/{}/{}'.format(self.dd, self.mm, self.yy))


p = Person()
p.display()
u = p.DOB()
u.display()
