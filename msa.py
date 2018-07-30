#python msa.py  copy this and right click terminal instead of having to retype

#Part 1
for number in range(1,1001):
    if number % 2 == 1:
        print number
#Part 2
for number in range(5,1000001,5):
    print number
#Sum List
def sumL(list):
    sum = 0
    for value in list:
        sum += value
    print sum

sumL([1,2,5,10,255,3])
#Average List
def avgL(list):
    sum = 0
    for value in list:
        sum += value
    print sum/len(list)

avgL([1,2,5,10,255,3])
