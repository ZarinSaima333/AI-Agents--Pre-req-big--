import threading
import time
import asyncio

def background_worker():
    while True:
        time.sleep(1)
        print('logging system health👌')

async def fetch_orders():
    await asyncio.sleep(5)
    print('Order fetched')

threading.Thread(target=background_worker,daemon=True).start()

asyncio.run(fetch_orders()) #main_thread

# logging system health👌
# logging system health👌
# Order fetched