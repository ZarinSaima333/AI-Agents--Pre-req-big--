import threading

chai_stock = 0

def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1

threads = [ threading.Thread(target=restock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print("Chai stock: ", chai_stock)

#This is a race condition because two threads are changing the same variable at the same time; 
# chai_stock += 1 is not done in one single step, so one thread can read the value while another thread changes it, 
# and then the first thread writes back an old value, causing some increases to be lost; 
# the GIL does not stop this because it only protects Python itself, not your variable, 
# so without a lock, the final number becomes wrong and changes every run.

#Chai stock:  200000

#Chai stock:  199104
#bank 
#solve: deadlock