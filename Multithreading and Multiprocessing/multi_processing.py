'''
What is Multiprocessing in Python?
Multiprocessing is a package that supports the spawning of processes using an API similar to the threading module. 
It allows you to create multiple processes, each with its own Python interpreter and memory space, enabling true parallelism and better CPU utilization, especially for CPU-bound tasks.
Why Use Multiprocessing?
1. Bypass Global Interpreter Lock (GIL): Python's GIL can be a bottleneck for CPU-bound tasks. Multiprocessing allows you to bypass the GIL by using separate memory spaces for each process.
2. Improved Performance: By utilizing multiple CPU cores, multiprocessing can significantly speed up the execution of CPU-intensive tasks.
3. Isolation: Each process runs independently, which can enhance stability and security.
'''

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i * i}")

def cube_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Cube: {i * i * i}")

if __name__ == "__main__":
    ## Create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()
    ## Start the processes
    p1.start()
    p2.start()

    ## Wait for both processes to complete
    p1.join()
    p2.join()

    finished_time = time.time()-t
    print(f"Finished in: {finished_time} seconds")