num = 10001
primes = [2]
i = 3
while len(primes) < num:
    prime = True
    for element in primes:
        if (i % element) == 0:
            prime = False
            break
    if (prime):
        primes.append(i)
    i += 1

print(primes[-1])