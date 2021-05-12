import json

def read_name():
    with open("fav_name.json",'r') as file:
        name = json.load(file)
        print("your name is {}".format(name))
        return name

def enter_name():
    with open("fav_name.json", "w") as file:
        name = input("what is your name?\n")
        json.dump(name, file)
        return name

try:
    read_name()
    ans=input("Is it your's name?\n")
    if (ans!='Y'):
        name=enter_name()
        print("I will remember you {}".format(name))
    else:
        name=read_name()
        print("Bye {}".format(name))
except:
    enter_name()