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

#So since I'm looking for the largest palindrome, I saved myself the time to iterate 'up' instead I chose to iterate 'down' from 1000 (999 is the first iteration then)
#The first layer while cycle iterates through x and the second while cycle iterates through y, that way every possible y will be tested against every possible x.
#The number is then saved as a string so I can check the commutability by simply inverting a list. Its a rather brute-force approach but it works.

# t = 0.4360978603363037 seconds
