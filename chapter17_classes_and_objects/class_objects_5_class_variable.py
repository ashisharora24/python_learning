class Sample:

    # class variables
    x = 10

    @classmethod
    def modify(cls):
        cls.x +=1

    def display(cls):
        print(cls.x)


s1 = Sample()
s2 = Sample()


s1.display()
s2.display()

s1.modify()

s1.display()
s2.display()

s2.modify()

s1.display()
s2.display()


# this action is happeing for object s1 level only
# the memory holded by s1.x is been operated with +=
# so this will not change s2.x value
s1.x+=1
print(s1.x)
print(s2.x)

s2.modify()
s1.display()
s2.display()
