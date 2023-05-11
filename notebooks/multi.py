import requests
import time
import threading
import multiprocessing
import math

# List of URLs to fetch data from
urls = [
    'https://www.python.org/',
    'https://www.openai.com/',
    'https://www.wikipedia.org/',
    # Add more URLs as needed
]

# List of numbers to calculate factorial
numbers = [50000, 100000, 150000, 200000]

# Define fetch_data as an independent function
def fetch_data(url):
    response = requests.get(url)
    return response.text

# Define calculate_factorial as an independent function
def calculate_factorial(n):
    return math.factorial(n)

def fetch_data_multithreaded(urls):
    start_time = time.time()

    # Create a list of threads
    threads = []

    # TODO: Create and start a thread for each URL in the urls list
    # Hint: You can use threading.Thread(target=function, args=(arg1,)) to create a thread
    # (https: // docs.python.org / 3 / library / threading.html  # threading.Thread)
    # Don't forget to start the thread with thread.start()
    for url in urls:
        pass

    # TODO: Wait for all threads to finish
    # Hint: You can use thread.join() to wait for a thread to finish
    for thread in threads:
        pass

    end_time = time.time()
    print(f"Time taken with multithreading: {end_time - start_time} seconds")

def fetch_data_multiprocessing(urls):
    start_time = time.time()

    # TODO: Create a multiprocessing pool and map the fetch_data function to the urls list
    # Hint: You can use multiprocessing.Pool() as pool: and then pool.map(function, iterable)
    # to create a multiprocessing pool and apply a function to an iterable
    # (https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool)
    with multiprocessing.Pool() as pool:
        pass

    end_time = time.time()
    print(f"Time taken with multiprocessing: {end_time - start_time} seconds")

def calculate_factorial_multithreaded(numbers):
    start_time = time.time()

    threads = []

    # TODO: Start the threads

    # TODO: Wait for all threads to finish

    end_time = time.time()
    print(f"Time taken to calculate factorials with multithreading: {end_time - start_time} seconds")

def calculate_factorial_multiprocessing(numbers):
    start_time = time.time()

    # TODO: Create a multiprocessing pool

    end_time = time.time()
    print(f"Time taken to calculate factorials with multiprocessing: {end_time - start_time} seconds")

if __name__ == '__main__':
    fetch_data_multithreaded(urls)
    fetch_data_multiprocessing(urls)
    calculate_factorial_multithreaded(numbers)
    calculate_factorial_multiprocessing(numbers)
