# python findCharacters.py
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []
def findC(lst):
    for value in lst:
        if value.count(char) != 0:
            new_list.append(value)
    print new_list
findC(word_list)    
