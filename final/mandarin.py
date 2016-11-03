def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # FILL IN YOUR CODE HERE
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
            '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    num = int(us_num)
    if num <= 10:
        return trans[us_num]
    elif num < 20:
        return trans['10'] + " " + trans[str(num-10)]
    else:
        out = trans[us_num[0]] + " " + trans['10']
        if us_num[1] != '0':
            out += " " + trans[us_num[1]]
        return out

for i in range(99):
    print(i, convert_to_mandarin(str(i)))
