Names=["max","dmitry"]
print("My friend is {}".format(Names[0]))
print("My friend is {}".format(Names[1]))

Gosti=["maxwell","Fedor","max"]
for name in Gosti:
    print("i'd like to invite {}".format(name))

CantInv=Gosti.pop()
print("{} cant came us".format(CantInv))

NewGuest="Dima"

Gosti.append(NewGuest)

for name in Gosti:
    print("i'd like to invite {}".format(name))

Gosti.insert(0,"Margo")
Gosti.insert(2,"Denis")

for name in Gosti:
    print("i'd like to invite {}".format(name))

numbers=list(range(1,6))
print(numbers)

cubs=[number**3 for number in range(1,10)]
print(cubs)