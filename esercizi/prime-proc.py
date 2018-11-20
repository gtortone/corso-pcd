#!/usr/bin/python3

import concurrent.futures as cf

def worker(n):
  print("Thread " + str(n) + " started")

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

  print("Thread " + str(n) + " finished")

executor = cf.ProcessPoolExecutor(max_workers=2)

t1 = executor.submit(worker, (1))
t2 = executor.submit(worker, (2))
