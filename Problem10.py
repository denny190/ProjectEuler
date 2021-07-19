#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

def eratosthen(x):
    sum = 0
    sieve = [True] * x

    for i in range(2, x):
        if sieve[i]:
            for j in range(i ** 2, x, i):
                sieve[j] = False

    for i in range(2, x):
        if sieve[i]:
            sum = sum + i

    return sum

print(eratosthen(2000000))

#I recycled my erastothen sieve algorithm from Problem 7 and made minor changes so it returns a sum of primes below the max number.
#Probably not the most efficient solution, but still pretty fast thanks to the power of modern computers. 

#t = 0.3870868682861328 seconds
