from logger import logging

def add(a,b):
    logging.debug(f"Addition of {a} and {b} is taking place")
    return a+b

logging.debug(f"Addition function is called")
add(2,3)