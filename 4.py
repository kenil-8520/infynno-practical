
a = int(input("enter number = "))
li = []
eli= []

for i in range(0, 5):
    val = int(input("Enter random number = "))
    li.append(val)

for i in li:
    if i % a == 0:
        eli.append(i)

print(eli)






