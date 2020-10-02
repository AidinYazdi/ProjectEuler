# 600851475143
num = 600851475143
prime_num = 600851475143
highest = 0
primes = [2]
i = 3
while i <= num:
  prime = True
  for ele in primes:
    if (i % ele) == 0:
      prime = False
      break
  if (prime):
    primes.append(i)
    if (num % i) == 0:
        num /= i
  i += 1

for element in primes[::-1]:
  if prime_num % element == 0:
    highest = element
    break
print(highest)
