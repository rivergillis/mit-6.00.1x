animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}

def biggest(aDict):
    biggestLen = 0
    biggestKey = '\0'
    for key in aDict.keys():
        if len(aDict[key]) > biggestLen:
            biggestLen = len(aDict[key])
            biggestKey = key
    return biggestKey

print(biggest(animals))
