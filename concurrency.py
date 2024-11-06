# concurrency.py
# This file demonstrates multithreading and multiprocessing in Python.

# =====================
# 1. Multithreading with Threading Library
# =====================

import threading
import time

# Function to simulate a task
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)

# Creating and starting a thread
thread = threading.Thread(target=print_numbers)
thread.start()

# Main thread continues to run
for i in range(5):
    print("Main Thread is running")
    time.sleep(0.5)

# Wait for the thread to complete
thread.join()
print("Thread completed")

# =====================
# 2. Multithreading with Multiple Threads
# =====================

def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print(f"Letter: {letter}")
        time.sleep(0.7)

# Creating multiple threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting the threads
thread1.start()
thread2.start()

# Waiting for threads to finish
thread1.join()
thread2.join()
print("Both threads completed")

# =====================
# 3. Multiprocessing with Multiprocessing Library
# =====================

import multiprocessing

# Function to simulate a task in a separate process
def square_numbers():
    for i in range(1, 6):
        print(f"Square: {i ** 2}")
        time.sleep(1)

# Creating and starting a process
process = multiprocessing.Process(target=square_numbers)
process.start()

# Main process continues to run
for i in range(5):
    print("Main Process is running")
    time.sleep(0.5)

# Wait for the process to complete
process.join()
print("Process completed")

# =====================
# 4. Using Process Pool
# =====================

# Creating a pool of processes to execute a function
def cube_number(n):
    return n ** 3

# Pool of 4 processes
with multiprocessing.Pool(4) as pool:
    results = pool.map(cube_number, [1, 2, 3, 4, 5])
print("Cube results from Process Pool:", results)

# =====================
# 5. Sharing Data Between Processes with Queue
# =====================

def square_worker(numbers, queue):
    """Worker function to square numbers and put them in a queue."""
    for n in numbers:
        queue.put(n ** 2)

# Using Queue to share data between processes
numbers = [1, 2, 3, 4, 5]
queue = multiprocessing.Queue()

# Creating process
p = multiprocessing.Process(target=square_worker, args=(numbers, queue))
p.start()
p.join()

# Retrieve results from the queue
squared_numbers = []
while not queue.empty():
    squared_numbers.append(queue.get())
print("Squared numbers from queue:", squared_numbers)

# =====================
# 6. Thread Synchronization with Locks
# =====================

lock = threading.Lock()

def count_with_lock():
    """Function to demonstrate thread synchronization with lock."""
    global counter
    lock.acquire()
    for _ in range(5):
        counter += 1
        print(f"Counter with Lock: {counter}")
        time.sleep(0.1)
    lock.release()

# Shared variable
counter = 0

# Creating threads with a shared lock
thread1 = threading.Thread(target=count_with_lock)
thread2 = threading.Thread(target=count_with_lock)

# Starting and joining threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Final Counter Value:", counter)

# =====================
# End of concurrency.py
# =====================
