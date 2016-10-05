def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.

    closest_power(3,12) returns 2
    closest_power(4,12) returns 2
    closest_power(4,1) returns 0
    '''
    smallest_gap = num
    closest = 0
    for i in range(int(num)):
        powered = base**i
        if abs(powered-num) < smallest_gap:
            smallest_gap = abs(powered-num)
            closest = i
        elif abs(powered-num) > smallest_gap:
            return closest
    return closest

