
nlist = [11, 13, 14, 16, 17, 18, 19, 20]
n = 2520
iterable = 0

while True:
    if all(n % x == 0 for x in nlist):
        break
    else:
        n = n + 2520

print(n)
