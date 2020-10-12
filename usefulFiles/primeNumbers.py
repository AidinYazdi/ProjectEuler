# this programs finds all the prime numbers within a lower and upper bound
# it uses a prime sieve (the Sieve of Eratosthenes)

# the bounds:
# bounds must be on the interval [2, infinity]
# bounds must be integers
lower_bound = 2
upper_bound = 2000000

# the array to keep track of which values are primes or not
primes = []
# setting up the boolean list for which values are primes and which are not
for i in range(lower_bound, upper_bound + 1):
    primes.append(True)

# the list of primes
list_of_primes = []

# finding all the prime values and adding them to the list_of_primes[]
for i in range(lower_bound, upper_bound + 1):
    if primes[i - lower_bound]:
        list_of_primes.append(i)
        j = i + i
        while j in range(upper_bound + 1):
            primes[j - lower_bound] = False
            j += i


# IMPORTANT: at this point in the code, list_of_primes[] is a list with all the prime
# numbers on the interval [lower_bound, upper_bound] (including the endpoints)
# from here, you can do whatever you want with list_of_primes[]

# print the list of primes
print(sum(list_of_primes))
