print("Hello, Django girls!")
if 3 > 2:
    print("It works")

if 5 > 2:
    print("5 is indeed greater than 2")
else:
    print("5 is not greater than 2")
#私の名前↓
name = "ai"
if name =="tsunematsu":
    print("Hey tsunematsu")
elif name == "ai":
    print("Hey ai!")
else:
    print("Hey anonymous!")
def hi(name):
    print("Hi" + name + "!")

girls = ["nari","yuria","ai"]
for name in girls:
    hi(name)
    print("Next girl")