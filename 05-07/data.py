import json
from mmap import PAGESIZE
from pydoc import pager
import module

f = open('data.json')
data = json.loads(f.read())

# print(data)

for i in range(0, len(data["data"])):
    data["data"][i]["age"] = module.fage(data["data"][i]["DOB"])
    a = data["data"][i]["age"]


for i in range(len(data["data"])):
    data['data'][i]["DOB"] = module.date_format(data['data'][i]["DOB"])


c = 0
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


while True:
    print("1. for paging...")
    print("2. for filtering...")
    print("0. Exit")
    n= input("enter number = ")
    if n == "1":
        paging()
    elif n == "2":
        print("sorting")
    elif n == "0":
        break



