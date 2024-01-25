#   Analyze a string to check if it contains two of the same letter in a row.
#   E.g, "Hello" has 'l' twice in a row, 
#   while the string "nono" does not have two identical letters in a row.

#   Function must return 'True' if there are two identical letters in a row in the string,
    #and 'False' otherwise 

def double_letters(string): 
    ans =  True if ([(False if string[i] != string[i+1] else True) for i in range(len(string) -1)].count(True)) >= 1 else False
    return ans

print(double_letters("Hello")) #It returns & prints True 
print(double_letters("nono")) #It returns & prints False