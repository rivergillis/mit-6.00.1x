def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    resurively defined
    '''
    midpoint = (len(aStr)//2)
    if char == aStr[midpoint]:
        return True
    elif len(aStr) == 1:
        return False
    if char > aStr[midpoint]:
        return isIn(char, aStr[midpoint+1:])
    else:
        return isIn(char, aStr[:midpoint])

print(isIn('l', "abcdefghijl"))
