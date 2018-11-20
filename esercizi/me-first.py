#!/usr/bin/python3

import random
import time 
import multiprocessing
import concurrent.futures as cf

buffer = []
buffer_size = 10

counter = 0
inp = 0
out = 0

for i in range(1,11):
  buffer.append(0)

def producer():
  global counter, inp, out

  while (True):
    while ( counter == buffer_size ):
      0  # do nothing

    item = random.randint(1,100)
    buffer[inp] = item

    inp = (inp + 1) % buffer_size 
    
    print("{P")
    counter = counter + 1		# critical section
    print("P}")

def consumer():
  global counter, inp, out

  while (True):
    while ( counter == 0 ):
      0   # do nothing

    item = buffer[out]

    out = (out + 1) % buffer_size
    
    print("{C")
    counter = counter - 1		# critical section
    print("C}")
    
executor = cf.ThreadPoolExecutor(max_workers=2)

t1 = executor.submit(producer)
t2 = executor.submit(consumer)
