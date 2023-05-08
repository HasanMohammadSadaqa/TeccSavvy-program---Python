import threading
import queue

# Shared queue
shared_queue = queue.Queue()


# Producer function
def producer():
    for i in range(5):
        item = f"Produced Item {i}"
        shared_queue.put(item)
        print(item)


# Consumer function
def consumer():
    while True:
        item = shared_queue.get()
        if item is None:
            break
        print(f"Consumed {item}")


# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Signal consumer to finish
shared_queue.put(None)

producer_thread.join()
# Wait for the consumer to finish
consumer_thread.join()
