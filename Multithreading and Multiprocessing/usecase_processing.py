'''
Real World Example: Multiprocessing for CPU-Bound Tasks
Scenario: Factorial Calculation
Description: Calculating the factorial of large numbers is a CPU-intensive task. 
Using multiprocessing allows us to distribute these calculations across multiple CPU cores, 
significantly speeding up the overall processing time.
'''

import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(100000)

def compute_factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000, 6000, 7000, 8000, 9000]

    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()

    print(f'Results: {results}')
    print(f"Time taken: {end_time - start_time} seconds")