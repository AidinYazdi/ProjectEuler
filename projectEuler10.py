num = 2000000
primes = [2]
i = 3
while i < num:
    if i % 100001 == 0:
        print(i)
    prime = True
    for j in primes:
        if (i % j) == 0:
            prime = False
            break
    if prime:
        primes.append(i)
    i += 2

print(sum(primes))
