def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test = 1
    if (a > b):
        test = b
    else:
        test = a

    while test > 1:
        if (a % test == 0 and b % test == 0):
            break
        test -= 1
    return test

def gcdRecur(a, b):
    if b == 0:
        return a
    return gcdRecur(b, a % b)
