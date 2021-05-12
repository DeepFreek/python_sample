def message(text):
    print("your fav book is {}".format(text))
def country(city,countr="Russia"):
    print("{} is in {}".format(city,countr))
country("Moscow")
country(countr="China",city="Pekin")
country("Japan","Tokyo")