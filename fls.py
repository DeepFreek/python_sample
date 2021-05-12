with open("train.txt") as file_obj:
    data=file_obj.read()
    print(data.rstrip())
for num in data:
    print("num is {}".format(num.rstrip()))