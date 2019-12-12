class Duck:
    def bark(self):
        print("Quack Quack")

class Human:
    def talk(self):
        print("bolo bolo")

def call_talk(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj,"bark"):
        obj.bark()

e = Duck()
call_talk(e)
h = Human()
call_talk(h)
