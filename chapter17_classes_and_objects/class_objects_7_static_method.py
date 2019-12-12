class MyClass:

    n=0

    def __init__(self):
        MyClass.n += 1

    @staticmethod
    def no_of_object():
        print("No of object : ", MyClass.n)


obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

MyClass.no_of_object()
