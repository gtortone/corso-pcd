#!/usr/bin/python3

print("Program started")

# initialize a list
primes = []
for possiblePrime in range(2, 20000):
    
  # assume number is prime until shown it is not. 
  isPrime = True
  for num in range(2, possiblePrime):
      if possiblePrime % num == 0:
          isPrime = False
      
  if isPrime:
      primes.append(possiblePrime)

print("Program finished")
