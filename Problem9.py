#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

for a in range(1,1000):
    for b in range(1,1000):
        c = 1000 - a - b
        if (a**2 + b**2) == c**2:
            print(a*b*c)
          
#Gotta say this problem was slightly less interesting than I expected it to be. It just goes down to iterating through the numbers again. 
#I did find some time-saving shortcuts at a blog called RadiusOfCircle, generating number c with the condition c = 1000-a-b. 
#Other than that, pretty straightforward

# t = 0.7771751880645752 seconds 
#time to solve could be reduced by having the two for cycles in a function so I can exit the nested loop when it finds the first triplet via returns statement.
#because technically there are two solutions to this since a and b commute in this instance. Thats why we get two solutions for which a1 = b2 and a2 = b1.
