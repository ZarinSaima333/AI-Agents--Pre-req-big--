# one single core doing all  the tasks, multi threads
import threading
import time

def take_order():
    for i in range(1,4):
        print(f'taking order for #{i}')
        time.sleep(2)

def brew_chai():
    for i in range(1,4):
        print(f'Brewing cha for #{i}')
        time.sleep(3)

#create threads
order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start() 

#wait for the both to finish
order_thread.join()
brew_thread.join()

print("All orders taken and cha brewed.")

# taking order for #1
# Brewing cha for #1
# taking order for #2
# Brewing cha for #2
# taking order for #3
# Brewing cha for #3
# All orders taken and cha brewed.