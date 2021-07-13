x = int(input())
while x % 2 == 0:
    print(2)
    x = x / 2

for y in range(3, int(x**(1/2)) + 1, 2):
    while x % y == 0:
        print(y)
        x = x / y

if x > 2:
    print(int(x))
