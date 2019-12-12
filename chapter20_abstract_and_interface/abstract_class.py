from abc import ABC

class MyClass(ABC):

    @abstractmethod
    def calculate(self,x):
        pass

class sub1(MyClass):

    def calculate(self, x):
        print("square : ", x*x)


class sub2(MyClass):

    def calculate(self, x):
        print("squareroot : ", math.sqrt(x))

obj1 = sub1()
obj1.calculate(10)
obj2 = sub2()
obj2.calculate(100)


# 1. abstract class can have
#     1. constructor
#     2. concrete method
#     3. abstract method
#
# 2. you cannot create object for abstract class
#
# 3. you can create objects of subclass (child class)
#
# 4. abstract method need to be defined in subclass
