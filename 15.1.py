import multiprocessing
import os

def right_now(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print ('Wait', seconds, 'seconds, the time is', datetime.now())

if __name__ == '__main__':
    import random 
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=right_now, args=(seconds,))
        proc.start()

