# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

x = 1000
y = 1000
palindrome = [0]

while x > 99:
    x -= 1
    y = 1000

    while y > 99:
        y -= 1
        xy = x * y
        a = str(xy)

        if a == a[::-1]:

            if int(a) > palindrome[0]:
                palindrome[0] = int(a)

print(*palindrome)
