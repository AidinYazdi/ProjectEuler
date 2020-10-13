# this program finds all the prime factors of a given number
# the number we want to find the prime factors of
num = 1024
primes = []
prime_factors = []
i = 2
while i <= num:
    prime = True
    for j in primes:
        if (i % j) == 0:
            prime = False
            break
    if (prime):
        primes.append(i)
        while (num % i) == 0:
            prime_factors.append(i)
            num /= i
    i += 1


# IMPORTANT: at this point in the code, prime_factors[] is a list of all the prime
# factors of num
print(prime_factors)
