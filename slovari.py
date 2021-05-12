favorite_numbers={"Max":3,
                  "Den":2,
                  "Dima":1
                  }
print("Max's favorite number is {}".format(favorite_numbers["Max"]))
print("Den's favorite number is {}".format(favorite_numbers["Den"]))
print("Dima's favorite number is {}".format(favorite_numbers["Dima"]))
print(sorted(favorite_numbers.values()))
#=======================================================================
glossary={"OOP":"object oriented programming",
          "Class":"pack of methods",
          "car":"machine to delever people"
          }
for key,value in glossary.items():
    print(key,"\n",key,"-","{}".format(value))
#=======================================================================
rivers={"nile":"Egypt",
        "Lena":"Russia",
        "Amazonka":"Brazil"
        }
for k,v in rivers.items():
    print("The {} runs through {}".format(k,v))
for key in rivers.keys():
    print(key)
for value in rivers.values():
    print(value)
#=======================================================================
fav_lang={"Max":"C",
          "Dima":"C",
          "Den":"Python",
          "Sergey":"Python"
          }
name_list=["Max","Ira","Dima"]
for name in name_list:
    if name in fav_lang.keys():
        print("Thanks {} for your answer".format(name))
    else:
        print("{} pidoras!".format(name))
#=======================================================================
Max={"Age":21,
     "Country":"NN",
     "Kaf":"Sm5"}
Dima={"Age":21,
     "Country":"Elets",
     "Kaf":"Sm5"}
Den={"Age":21,
     "Country":"Msk",
     "Kaf":"Sm7"}
people=[Max,Dima,Den]
for man in people:
    for k,v in man.items():
        print("{} is {}".format(k,v))
#======================================================================
fav_numb={"Max":[1,2,3],
          "Den":[3,4,5],
          "Dima":[6,7,8]
          }
for k in fav_numb.keys():
    print("{} fav numbers are {}".format(k,fav_numb[k]))
#======================================================================
Cities={"Msk":{"population":2000000,"area":1000},
        "pekin":{"population":5000000,"area":3000},
        "London":{"population":8000000,"area":4000},
        }
for k in Cities.keys():
    print("{}".format(k))
    for key,value in Cities[k].items():
        print(key,"-{}".format(value))

