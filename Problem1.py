# If we list all the natural numbers below 10 that are
# multiples of 3 and 5, we get 3,5,6 and 9. The sum of these
# multiples is 23. Find the sum of all multiples of 3 or 5 below 1000.

sum = 0
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        sum = sum + x

print(sum)

# This wasn't much of a challenge for python thanks to the modulo operator
# I'm iterating through all numbers between 0 and 1000 to look for numbers that are multiples of 3 OR 5 and adding them to a sum, easy peasy.
