while True:
    top=input("Enter topping ")
    if top=="quit":
        break
    else:
        print("chosen topping is {}".format(top))
#============================================================
sndwch=["1","2","3"]
ended=[]
while sndwch:
    ended.append(sndwch.pop())
print(ended)