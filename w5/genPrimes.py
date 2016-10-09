#Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
import time
start=time.time()
#0.44 worst
def genPrimes():
    x = 2
    while True:
        isPrime = True
        for i in range(2,int(x**0.5)+1):
            if x % i == 0:
                isPrime = False
                break
        if isPrime:
            yield x
        x += 1

for x,i in enumerate(genPrimes()):
    if x==5500:
        break
end = time.time()
print(end-start)
