#!/usr/bin/python3

import threading
import time

def worker():
  while(True):
    print("working...")
    #time.sleep(1)  

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
