class Duck:
    def talk(self):
        print("Quack Quack")

class Human:
    def talk(self):
        print("bolo bolo")

def call_talk(obj):
    obj.talk()


x = Duck()
call_talk(x)
y = Human()
call_talk(y)
