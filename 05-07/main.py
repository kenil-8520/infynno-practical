from audioop import reverse
import json
import module

f = open('data.json')
data = json.loads(f.read())

# print(data)

for i in range(0, len(data["data"])):
    data["data"][i]["age"] = module.fage(data["data"][i]["DOB"])
    a = data["data"][i]["age"]
    # print(type(a))

for i in range(len(data["data"])):
    x = data['data'][i]["DOB"] = module.date_format(data['data'][i]["DOB"])

c = 0


def sort_name():
    l = data["data"].copy()
    l.sort(key = lambda x:x ['name'])
    for i in l:
        print(i)


def sort_age():
    l = data["data"].copy()
    l.sort(key = lambda x:x ['age'])
    for i in l:
        print(i)


def sort_DOB():
    l = data["data"].copy()
    l.sort(reverse=True ,key = lambda x:x ['age'])
    for i in l:
        print(i)


def step(c):
    for i in data["data"][c:c+5]:
        print(i)
    return

def paging():
    for i in data["data"][:5]:
        print(i)
    while True:
        print()
        print("P, 1, 2, 3, 4, 5, N")
        print("0 to go back to previous menu")
        print()
        n = input("enter P OR N = ")

        if n == "n" or n == "N":
            global c
            c +=5
            step(c)
            if c == 25:
                print("in the last page ")
        elif n == "p" or n == "P":
            c -=5
            step(c)
            if c < 0:
                print("in 1st page ")
        elif n == "1":
            for i in data["data"][:5]:
                print(i)
        elif n == "2":
            for i in data["data"][5:10]:
                print(i)
        elif n == "3":
            for i in data["data"][10:15]:
                print(i)
        elif n == "4":
            for i in data["data"][15:20]:
                print(i)
        elif n == "5":
            for i in data["data"][20:25]:
                print(i)
        elif n == "0":
            break
        else:
            print("invalid entery")
    return



def inp():
    n = int(input("enter age range = "))
    for i in range(len(data["data"])):
        if data["data"][i]["age"] < n:
            print(data["data"][i])


while True:
    print()
    print("1. for paging...")
    print("2. for filtering by name...")
    print("3. for filtering by age...")
    print("4. for filtering by DOB...")
    print("5. for filter by age...")
    print("0. Exit")
    print()
    n= input("enter number = ")
    if n == "1":
        paging()
    elif n == "2":
        sort_name()
    elif n == "3":
        sort_age()
    elif n == "4":
        sort_DOB()
    elif n == "5":
        inp()
    elif n == "0":
        break
