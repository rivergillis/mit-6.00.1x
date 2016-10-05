def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]
    '''
    if aList == []:
        return []

    print(aList)
    for index,elem in enumerate(aList):
        print(elem)
        if type(elem) == list:
            print("Is a list")
            return flatten(elem) + flatten(aList[index+1:])
        else:
            print("Is not a list")
            return [elem] + flatten(aList[index+1:])

print(flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))
