class Sample:

    def __init__(self):
        self.x = 10

    def modify(self):
        self.x +=1

    def display(self):
        print(self.x)


s1 = Sample()
s2 = Sample()

s1.modify()
s1.display()
s2.display()
