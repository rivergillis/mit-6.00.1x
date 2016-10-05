def f(a, b):
    return a+b

def dict_interdiff(d1, d2):

    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above

    If f(a, b) returns a + b
    d1 = {1:30, 2:20, 3:30, 5:80}
    d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
    then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})

    '''
    inter_dict = {}
    diff_dict = {}

    for x in d1.keys():
        if x in d2:
            inter_dict[x] = f(d1[x], d2[x])
        else:
            diff_dict[x] = d1[x]
    for x in d2.keys():
        if x not in d1:
            diff_dict[x] = d2[x]
    return (inter_dict, diff_dict)

print(dict_interdiff({1:30, 2:20, 3:30, 5:80}, {1:40, 2:50, 3:60, 4:70, 6:90}))
