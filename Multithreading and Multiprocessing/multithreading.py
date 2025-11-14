'''
When to use Multithreading in Python?
Multithreading in Python is useful in the following scenarios:
1. I/O-Bound Tasks: Multithreading is particularly effective for I/O-bound tasks, such as file operations, network requests, and database queries. Since these tasks often involve waiting for external resources, threads can be used to perform other operations while waiting.
2. GUI Applications: In graphical user interface (GUI) applications, multithreading can help keep the interface responsive by offloading long-running tasks to separate threads, preventing the main thread from being blocked.
3. Concurrent Operations: When you need to perform multiple operations concurrently, such as downloading multiple files or processing multiple user requests, multithreading can help improve efficiency and responsiveness.
4. Background Tasks: Multithreading is useful for running background tasks, such as periodic data updates or monitoring tasks, without interrupting the main application flow.
5. Lightweight Tasks: For tasks that are lightweight and do not require significant CPU resources, multithreading can help improve performance by allowing multiple threads to run simultaneously
'''

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(2)
        print(f"Letter: {letter}")
##Creating 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t = time.time()
#Start the threads
t1.start()
t2.start()

##Wait for both threads to complete
t1.join()
t2.join()

finished_time = time.time()-t
print(f"Finished in: {finished_time} seconds")