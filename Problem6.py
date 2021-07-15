#The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... 10^2 = 385
#The square of the sum of the first ten natural numbers is, (1 + 2 + .... 10)^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is. 3025 - 385 = 2640
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

num1 = sum([x for x in range(1,101)])**2
num2 = sum([y**2 for y in range(1,101)])
print(num1 - num2)

#This would be easy even with a calculator and paper. There is not much to explain.
#My original algorithm was a little larger so I decided to save the more compact version by user ivanux on Euler archives. 
