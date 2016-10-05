def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    total = 0
    for i in range(len(listA)):
        total += listA[i]*listB[i]
    return total

print(dotProduct([1,2,3],[4,5,6]))
print(dotProduct([],[]))
