num = int(input("Give me number: "))
x = num + num
ListOfDividers = []
while x <= 200:
    ListOfDividers.append(x)
    x = x + num
print(ListOfDividers)
