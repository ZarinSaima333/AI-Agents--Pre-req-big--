import threading

lock_a = threading.Lock()
lock_b = threading.Lock()


def task1():
    with lock_a:
        print("Task 1 acquired lock a")
        with lock_b:
            print("Task 1 acquired lock b")

def task2():
    with lock_b:
        print("Task 2 acquired lock b")
        with lock_a:
            print("Task 2 acquired lock a")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

# Task 1 acquired lock a
# Task 2 acquired lock b

# Here’s what happens:

# Thread 1 locks A and waits for B

# Thread 2 locks B and waits for A

# Neither thread can continue because each one is holding the lock the other needs

# So both threads get stuck, and the program never finishes.



# eadlock and race conditions are different problems, though both involve threads and shared resources.

# Race condition: Happens when threads access or modify shared data at the same time without proper coordination, causing unpredictable results (like your chai_stock example).

# Deadlock: Happens when threads wait forever for each other’s locks, so the program gets stuck (like your lock_a + lock_b example).

# Using locks can solve race conditions by protecting shared data, but if you’re not careful, locks can cause deadlocks, which is a new problem