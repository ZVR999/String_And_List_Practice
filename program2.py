# python program2.py
def program(lst):
    total = 0
    string = ''
    for value in lst:
        if isinstance(value,str):
            string += value + " "
        if isinstance(value,float):
            total += value
        if isinstance(value,int):
            total += value
    print string, total
    if string and total:
        print "The list you entered is of mixed types"
    
    elif string:
        print "The list you enter is of string type"
    else:
        print "The list you enter is of number type"

program(['magical unicorns', 19,'hello',98.98,'world'])
program([1,2,3,4,5,6])
program(['hello','goodbye','uhhhhh','nope'])
        