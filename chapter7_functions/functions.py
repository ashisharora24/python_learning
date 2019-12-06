'''
    difference between function and method

    a function can be writting independently as a python program
    called by its name

    method:
    when a function is written inside the class, then it becomes method

    called as :
        1. classname.methodname()
        2. objectname.methodname()
'''

#-------------------------------------------------------------------------------
'''
    defining function

    syntax:
        def functionname(attributes_passing):
            logic
            return
'''
def function_testing(name):
    string="my name is "+name
    return string

print(function_testing("ashish"))


#-------------------------------------------------------------------------------
'''function inside another function'''

def display(str):
    def msg():
        return "How are you"
    return str+msg()
print(display("ashish"))


#-------------------------------------------------------------------------------
'''function having function as parameter'''

def display1(fun):
    return fun()+" how are you"
def msg():
    return "ashish arora"
print(display1(msg))


# ------------------------------------------------------------------------------
''' function returning another function'''
def display2():
    def msg():
        return "how are you "
    return msg()

print(display2())

#-------------------------------------------------------------------------------
'''pass by object reference'''

def testing_reference(a,b=10):
    print("------------------")
    print("id(a) : ", id(a))
    print("id(b) : ", id(b))

a = 10
b = 20
print("id(a) : ", id(a))
print("id(b) : ", id(b))
testing_reference(a,b)

# output:
# id(a) :  1627811120
# id(b) :  1627811440
# ------------------
# id(a) :  1627811120
# id(b) :  1627811440


#   but in case of list, refence doesnt work
def testing_list_reference(a):
    print("------------------")
    print("id(a) : ", id(a))

a = ['10','20']
print("id(a) : ", id(a))
testing_reference(a)


#-------------------------------------------------------------------------------
'''
Arguments are of 4 types:
    1. positional arguments
    2. keywords argument
    3. default arguments
    4. variable arguments
'''

# positional argument:
def msg1(a, b):
    print(a, b)

msg1("a", "b")

# keyword argument
def msg3(a, b):
    print(a,b)

msg3(a="a",b="b")

# default argument
def msg4(a="a",b="b"):
    print(a,b)

msg4()


# variable length argument
def msg5(farg, *args):
    print(farg)
    for i in args:
        print(i)
msg5(1,2,3,4)

# variable argument passed as normal but received as dictionary
def msg6(farg, **kwargs):
    print(farg)

    for x,y in kwargs.items():
        print(x,y)

dict = {'a':'a','b':'b','c':'c'}
msg6("ashish",a='a',b='b',c='c')


#-------------------------------------------------------------------------------
'''local variable'''

a = 1   # global variable
print(a)
print("outside : ", id(a))
def msg7():
    b=1 # local variable
    a=2 # this is local variable not global
        # you cannot modify global variable inside function directly

    print("inside : ",a)
    print("inside id : ",id(a))

msg7()
print(a)
print("outside : ", id(a))



#-------------------------------------------------------------------------------

''' global variable which can be modified inside function'''

a = 1
def msg8():
    global a
    a = 2
msg8()
# this will modify the variable a at gloabl level



#-------------------------------------------------------------------------------
'''recursion'''
def msg9(num):
    print(num)
    if num>0:
        msg9(num-1)
    else:
        return
msg9(5)



#-------------------------------------------------------------------------------
''' lambda Function'''

# normal function
def msg10(x):
    return x**2
print(msg10(2))


# lambda function
f = lambda x:x**2
print( f(5) )


'''
how does this work:
function name is replaced by lambda : msg10 --> lambda
parameters are placed as it is after lambda  : msg10(x)--> lambda x
return expression is placed after ':'  -->  lambda x:x**2
'''
def msg11(x, y):
    return x**y
print(msg11(2,3))


# lambda function
f = lambda x, y:x**y
print( f(2,3) )


#-------------------------------------------------------------------------------
''' how lambda function reduces code'''

def is_even(x):
    if x%2==0:
        return True
    return False

lst = [1,2,3,4,5,6,7,8,9]

lst = list(filter(is_even,lst))
print(lst)


'''this complete code can be simplfied in one line'''
lst = [1,2,3,4,5,6,7,8,9]
lst = list(filter(lambda x:x%2==0,lst))
print(lst)


#-------------------------------------------------------------------------------
'''
    function decorator
    accepts function as argument and returns a function
'''
def msg12(fun):
    def inner():
        value = fun()
        return value+2
    return inner()

def msg13():
    return 10

result = msg12(msg13)
print(result)



# ------------------------------------------------------------------------------
'''special variable : __name__
    this special variabl is created by python automaticallyait tells where the python program is executed

    if the program is executed directly then it will contain the value '__main__'
    or
    if the program is executed through module then it will contains module name
    '''
