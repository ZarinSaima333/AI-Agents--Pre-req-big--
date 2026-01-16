from multiprocessing import Process
import time

def crunch_number():
    print('Started the count process')
    count=0
    for _ in range(100_000_000):
        count+=1
    print('Ended the count process')

if __name__ == '__main__':
    start=time.time()

    p1= Process(target=crunch_number)
    p2= Process(target=crunch_number)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end=time.time()

    print(f"total time required in multiprocessing {end-start:.2f} seconds")

#spawn error thake dendur dite hobe
#idk the entry point of  your program,multiprocessing doesnt know a lot but threading does.
#We need if __name__ == "__main__": in multiprocessing so that child processes do not re-execute the entire script again, which would cause infinite process creation.

# Started the count process
# Started the count process
# Ended the count process
# Ended the count process
# total time required in multiprocessing 11.54 seconds