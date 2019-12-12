class Students:
    def __init__(self):
        self.name = "Vishnu"
        self.age = 20
        self.marks = 900

    def talk(self):
        print("Hii i am ",self.name)
        print("my age is ", self.age)
        print("My marks ",self.marks)

s1 = Students()
s2 = Students()
s2.name = "Varun"
s2.age = 17
s2.marks = 950
s2.talk()
s1.talk()

# OUTPUT
# Hii i am  Vishnu
# my age is  20
# My marks  900
# Hii i am  Varun
# my age is  17
# My marks  950
# Hii i am  Vishnu
# my age is  20
# My marks  900
