# from tokenize import Double


lst = ["1", "3", "A", "RAJ", "AADI", "$", "A", "E", "I", "O", "U", "323", "4", "8", "10", "100", "1000","1"]


def check(lst):
    if lst[0] == lst[-1]:
        print("first and last are same")
    else:
        print("not same")


def count(lst):
    n = len(lst)
    print("Number of elements in the list ", n)

def demo(lst):
    d=[]
    c=[]
    for i in lst:
        if i.isdigit():
            d.append(int(i))
        else:
            c.append(i)
    print("integer from list = ",d)
    print("string from list = ",c)

def search(lst):
    print ("element on ",lst.index('AADI'),"index")


def vowel(lst):
    vowels = 'aeiouAEIOU'
    count = 0
    vl=[]

    for char in lst:
        if char in vowels:
            count += 1
            vl.append(char)
    print(f"Vowels= {vl}")



check(lst)
count(lst)
demo(lst)
vowel(lst)
search(lst)


