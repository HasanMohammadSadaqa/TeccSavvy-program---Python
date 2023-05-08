"""
this snippet of code aims to Create multiple threads that print out a message.
"""
import threading
import time


def print_message(message):
    print(message)

if __name__ == "__main__":

    threads = []
    for _ in range(10):
        thread = threading.Thread(target=print_message, args=["Hello World!"])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
