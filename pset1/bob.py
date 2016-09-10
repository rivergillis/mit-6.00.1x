s = "bobabcsdlfajsdbobsldfkjadsfbob"
bobs = 0
count = 0
while (count < (len(s)-2)):
    if s[count] == 'b' and s[count+1] == 'o' and s[count+2] == 'b':
        bobs += 1
    count += 1
print(bobs)
