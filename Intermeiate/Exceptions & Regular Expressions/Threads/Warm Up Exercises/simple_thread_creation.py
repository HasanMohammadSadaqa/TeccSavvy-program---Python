"""
This code aims to create a simple thread that prints out a message.
"""
import threading


def print_message(message):
    print(message)


if __name__ == "__main__":
    thread1 = threading.Thread(target=print_message, args=["Hello World!"])
    thread1.start()
    thread1.join()
