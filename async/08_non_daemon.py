import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temp)
t.start()

print("Main program done")


#non daemon thread does not overs when the main thread is done executing.
# Monitoring tea temperature...
# Main program done

# Monitoring tea temperature...
# Main program done
# Monitoring tea temperature...
# Monitoring tea temperature...
# Monitoring tea temperature...
# Monitoring tea temperature...
# Monitoring tea temperature...