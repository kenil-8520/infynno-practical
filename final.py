station = 12
stop = 4
temp = 1
num = 1
for i in range(stop):
    i += 1
    temp *= i
t = station - stop + 1
while t != (station - 2 * stop + 1):
    num *= t
    t -= 1
print(int(num / temp))
