lst = [1,2,3,4,5,6]
lst[0], lst[-1] = lst[-1], lst[0]
print(lst)

lsta = [2,1,8,5,3,10,6]
lsta.sort()
print("list in ascending order",lsta)

lstd = [2,1,8,5,3,10,6]
lstd.sort(reverse=True)
print("list in descending order",lstd)


l = [1,2,3,4,5,6,7,8,9,10]
le=[]
lo =[]

for i in l:
    if i % 2 == 0:
        le.append(i)
    else:
        lo.append(i)

print("odd",lo)
print("even",le)



def check (str):
	return str == str[::-1]

str = input("enter string to check for palindrome = ")

ans = check(str)

if ans:
	print("palindrome string")
else:
	print("not a palindrome string")


string = input("enter string = ")
char = input("enter character to check = ")
c = string.count(char)
print("no of count = ",c)


