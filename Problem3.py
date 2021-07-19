#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

x = 600851475143
while x % 2 == 0:
    print(2)
    x = x / 2

for y in range(3, int(x**(1/2)) + 1, 2):
    while x % y == 0:
        print(y)
        x = x / y

if x > 2:
    print(int(x))

#Basic algorithm for prime factorisation that I made as one of our many homeworks for Programming 1 and Algorithmisation at MFFUK. 
#I just picked out the largest number it outputted. You could write it such as it only outputs the largest prime but I couldn't be bothered.

# t = 0.05101156234741211 seconds
