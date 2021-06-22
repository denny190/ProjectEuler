fnum = [1,2]
sum = 2
while fnum[1] < 4000000:
    fnum = fnum[::-1]
    fnum[1] = fnum[0] + fnum[1]
    if fnum[1] % 2 == 0:
        sum = sum + fnum[1]
    #print(fnum, sum)

print(sum)
