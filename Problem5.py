#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

nlist = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = 2520
iterable = 0

while True:
    if all(n % x == 0 for x in nlist):
        break
    else:
        n = n + 2520

print(n)

#So I can significantly speed up the algorithm by removing numbers I have to iterate through. 
#If its divisible by numbers between 11-20 it WILL be divisible by numbers between 1-10. Elementary stuff.
#The algorithm itself is, again, kinda brute-force. I use a dead simple while cycle to iterate through multiples of 2520
#(another way to speed it up is to iterate by adding 20 or 2520 instead of adding 1)
#Once all modulos of n%x, where x are elements in nlist, equal 0 we have our number and we can exit the cycle.
