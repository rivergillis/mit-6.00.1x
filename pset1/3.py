# print the longest substring of s in alphabetical order
s = "12345safjhxvbsfubu23br84028bfasd80fybxzcv8cx7v"
current = ""
best_spot = 0
longest_len = 0

prev = ''
count = 0
while count < len(s):
    if s[count] >= prev:
        current += s[count]
    else:
        # save the biggest length and the spot at which it begins
        if len(current) > longest_len:
            longest_len = len(current)
            best_spot = count - longest_len
        current = s[count]
    prev = s[count]
    count += 1

if len(current) > longest_len:
    print("Longest substring in alphabetical order is: " + current)
else:
    # rebuild the longest string
    count = 0
    current = ""
    while count < longest_len:
        current += s[best_spot + count]
        count += 1
    print("Longest substring in alphabetical order is: " + current)
