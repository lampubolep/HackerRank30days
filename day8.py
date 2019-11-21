n = int(input())

phonebook = {}

for i in range(0, n):
    entry = str(input()).split(" ")

    name = entry[0]
    phone = int(entry[1])
    phonebook[name] = phone

for j in range(0, n):
    name = str(input())

    if name in phonebook:
        phone = phonebook[name]
        print(name+"="+str(phone))
    else:
        print("Not found")