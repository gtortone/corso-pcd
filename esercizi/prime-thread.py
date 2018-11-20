#!/usr/bin/python3

import threading

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

t1 = threading.Thread(target=worker,args=[1])
t2 = threading.Thread(target=worker,args=[2])

t1.start()
t2.start()

t1.join()
t2.join()
