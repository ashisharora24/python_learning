class MyException(Exception):
    def __init__(self,arg):
        self.msg=arg

    def check(dict):
        for k,v in dict.items():
            print('Name = {:15s} Balance = {:10.2f}'.format(k,v))
            if (v<2000.00):
                raise MyException("Balance is less")


    bank = {'Raj':5000,'Vani':55000,'Ajay':1990}

    try:
        check(bank)
    except MyException as me:
        print(me)
