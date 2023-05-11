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

    # Start the threads
    for url in urls:
        thread = threading.Thread(target=fetch_data, args=(url,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Time taken to fetch data with multithreading: {end_time - start_time} seconds")

def fetch_data_multiprocessing(urls):
    start_time = time.time()

    # Create a multiprocessing pool
    with multiprocessing.Pool() as pool:
        results = pool.map(fetch_data, urls)

    end_time = time.time()
    print(f"Time taken to fetch data with multiprocessing: {end_time - start_time} seconds")

def calculate_factorial_multithreaded(numbers):
    start_time = time.time()

    # Create a list of threads
    threads = []

    # Start the threads
    for number in numbers:
        thread = threading.Thread(target=calculate_factorial, args=(number,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Time taken to calculate factorials with multithreading: {end_time - start_time} seconds")

def calculate_factorial_multiprocessing(numbers):
    start_time = time.time()

    # Create a multiprocessing pool
    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_factorial, numbers)

    end_time = time.time()
    print(f"Time taken to calculate factorials with multiprocessing: {end_time - start_time} seconds")

if __name__ == '__main__':
    fetch_data_multithreaded(urls)
    fetch_data_multiprocessing(urls)
    calculate_factorial_multithreaded(numbers)
    calculate_factorial_multiprocessing(numbers)
