def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    longest_start_index_inc = None
    longest_start_index_dec = None
    longest_inc = 0
    longest_dec = 0
    reset = True
    current_index = None
    inc_len = 1
    dec_len = 1
    print(L)
    for i in range(len(L)-1):
        if reset:
            current_index = i
            inc_len = 1
            reset = False
            print("resetting... current_index=", i)
            print('test')
        if (L[i] > L[i+1]) or (i == len(L)-2):
            if i == len(L)-2:
                inc_len += 1
            print("L[",i,"]=",L[i]," L[",i+1,"]=",L[i+1])
            reset = True
            print("reset requested")
            print(inc_len, longest_inc)
            if inc_len > longest_inc:
                print("new longest, ci=", current_index, "i+1=",i+1,"inc_len=",inc_len)
                print("about to make longest_sub_inc")
                longest_sub_inc = L[current_index:i+1]
                longest_inc = inc_len
                longest_start_index_inc = current_index
                if i == len(L)-2 and L[i] <= L[i+1]:
                    longest_sub_inc.append(L[i+1])
                    longest_inc += 1
        else:
            print("Increasing with no reset, i=",i)
            inc_len += 1
    print(longest_sub_inc)

    reset = True
    current_index = None

    for i in range(len(L)-1):
        if reset:
            current_index = i
            dec_len = 1
            reset = False
            print("resetting... current_index=", i)
        if (L[i] < L[i+1]) or (i == len(L)-2):
            if i == len(L)-2:
                dec_len += 1
            print("L[",i,"]=",L[i]," L[",i+1,"]=",L[i+1])
            reset = True
            print("reset requested")
            if dec_len > longest_dec:
                print("new longest, ci=", current_index, "i+1=",i+1,"dec_len=",dec_len)
                longest_sub_dec = L[current_index:i+1]
                longest_dec = dec_len
                longest_start_index_dec = current_index
                if i == len(L)-2 and L[i] >= L[i+1]:
                    longest_sub_dec.append(L[i+1])
                    longest_dec += 1
        else:
            print("Decreasing with no reset,i=",i)
            dec_len += 1
    print(longest_sub_dec)

    if len(longest_sub_inc) == len(longest_sub_dec):
        if longest_start_index_inc <= longest_start_index_dec:
            return sum(longest_sub_inc)
        else:
            return sum(longest_sub_dec)
    elif len(longest_sub_inc) > len(longest_sub_dec):
        return sum(longest_sub_inc)
    else:
        return sum(longest_sub_dec)

print(longest_run([5,4,10]))
