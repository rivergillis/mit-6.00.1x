animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}
def how_many(aDict):
    lentotal = 0
    for val in aDict.values():
        lentotal += len(val)
    return lentotal

print(how_many(animals))
