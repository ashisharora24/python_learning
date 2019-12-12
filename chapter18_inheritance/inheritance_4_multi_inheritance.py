class Father:

    def __init__(self):
        print("Father")

class A(Father):

    def __init__(self):
        print("A start")
        super().__init__()
        print("A end")

class B(Father):

    def __init__(self):
        print("B start")
        super().__init__()
        print("B end")

class C(Father):

    def __init__(self):
        print("C start")
        super().__init__()
        print("C end")

class X(A,B):

    def __init__(self):
        print("X start")
        super().__init__()
        print("X end")

class Y(B, C):

    def __init__(self):
        print("Y start")
        super().__init__()
        print("Y end")

class P(X,Y, C):

    def __init__(self):
        print("P start")
        super().__init__()
        print("P end")

e = P()


# OUTPUT ::
# P start
# X start
# A start
# Y start
# B start
# C start
# Father
# C end
# B end
# Y end
# A end
# X end
# P end
