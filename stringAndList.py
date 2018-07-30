# python stringAndList.py
words = "It's thanksgving day. It's my birthday, too!"
print words.find("day") 

newWords = words.replace("day","month")
print newWords

def printMinMax(arr):
    print min(arr), max(arr)

printMinMax(["hello",2,54,-2,7,12,98,"world",100])

def firstAndLast(arr):
    print arr[0], arr[-1]
    newarr = arr[0], arr[-1]
    print newarr
    for value in newarr:
        print value

firstAndLast(["hello",2,54,-2,7,12,98,"world"])

def newList(arr):
    arr.sort()
    print arr
    half = arr[:len(arr)/2]
    secondHalf = arr[len(arr)/2:]
    print half
    print secondHalf
    secondHalf.insert(0,half)
    print secondHalf
  
newList([19,2,54,-2,7,12,98,32,10,-3,6])