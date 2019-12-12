class Duck:
    def talk(self):
        print("Quack Quack")

class Human:
    def talk(self):
        print("bolo bolo")

# while designing call_talk we are not worried whether its duck or human.
# all we know it will talk
# so call_talk can we used for more than one form
# thats why its called polymorphism
def call_talk(obj):
    obj.talk()


x = Duck()
call_talk(x)
y = Human()
call_talk(y)
