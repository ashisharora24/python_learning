name = "ashish"

if name == "arora":
    print(True)
elif name == "ashish":
    print(False)
else:
    print("None")


"""
else  block in while loop and forloop will only execute when the complete blocks without break
"""

i = 10
while i>0:
    print("hello")
    if i==5:
        break
    i-=1
else:
    print("else block")


"""
else  block in while loop and forloop will only execute when the complete blocks without break
"""

i = 10
for j in range(i):
    print(j)
    if j==5:
        break
else:
    print("else block")


"""continue will continue the loop , except that loop. else block will be executed """

for j in range(10):
    if j == 5:
        continue
    print(j)
else:
    print("this is else block")



a = "ashish1"

assert a=="ashish", " wrong name"
print("done")
