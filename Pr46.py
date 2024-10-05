import math
# Project Euler problem 46. What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

# Checking for primality

def is_prime(n):
    if n < 2: 
         return False;
    if n % 2 == 0:             
         return n == 2  
    # Sieve of Eratosthenes
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

# Making a list of all the primes under a certain border using the sieve of Eratosthenes
def primes(n):
    list = []
    primes = []
    list.append(2)
    i = 3
    while ( i <= n ):
      list.append(i)
      i += 2
    # Sieve of Eratosthenes
    h = 2
    k = 3
    while k*k <= n:
      i = 0
      for j in range(h, len(list), 1):
         if list[j] % k == 0:
            list[j] = 0
      h += 1
      k += 2
 
    for l in range(0, len(list), 1):
     if list[l] != 0:
      primes.append(list[l])

    return primes

# initial values
odd = 9
border = 6000
prime_list = primes(border)
counter = 0
list_odd = []
      
for a in range(0, len(prime_list), 1):
  for b in range(0, border, 1):
    d = (prime_list[a] + 2*math.pow(b,2))
    if math.floor(d/2) != d/2 and d < border:
      list_odd.append(d)

while( odd < border):
  odd += 2
  for i in range(0, len(list_odd), 1):
      if odd == list_odd[i]:
         break   
      if i == len(list_odd)-1 and is_prime(odd) == False:
         print("The right number!")
         print(odd) 
         odd = border + 1
    
 
# Answer: 5777
