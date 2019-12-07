'''
    try:
        - Code under scan
    except:
        - if there is error then this will be executed.
        - we can have multiple except block
        - madatory block
    else:
        - this block will only be executed if no error occurs
        - not madatory block
    finally:
        - this block is executed no matter error comes or not
        - not madatory block

'''

try:
    print("this is try block")
    print(10/0)
except ArithmeticError:
    print("this is except block")
except Exception:
    print("this is except block")
else:
    print("this is else block")
finally:
    print("this is finally block")
