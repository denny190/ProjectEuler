#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

def eratosthen(largenum, stopnum):
    sieve = [True] * x

    for i in range(2, x):
        if sieve[i]:
            for j in range(i ** 2, x, i):
                sieve[j] = False

    counter = 0
    for i in range(2, x):
        if sieve[i]:
            counter += 1
            if counter == 10001:
                print(i)

eratosthen(10000000)

#Maybe a little brute-forced again, but classic erastothen sieve algorithm of an arbitrarily large number paired with an if condition that stops the sieve
#upon reaching the desired prime. In thise case 10001st prime. 
