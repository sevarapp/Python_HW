import threading

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_primes(start, end, result):
    for number in range(start, end):
        if is_prime(number):
            result.append(number)

def threaded_prime_checker(start, end, num_threads=4):
    threads = []
    results = [[] for _ in range(num_threads)]
    chunk_size = (end - start) // num_threads

    for i in range(num_threads):
        chunk_start = start + i * chunk_size
        chunk_end = end if i == num_threads - 1 else chunk_start + chunk_size
        t = threading.Thread(target=check_primes, args=(chunk_start, chunk_end, results[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    primes = []
    for res in results:
        primes.extend(res)
    primes.sort()
    print(f"Prime numbers between {start} and {end}:")
    print(primes)

import threading
from collections import Counter
import os

def process_lines(lines, counter):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)
    counter.append(local_counter)

def threaded_word_count(file_path, num_threads=4):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    threads = []
    results = []
    chunk_size = len(lines) // num_threads

    for i in range(num_threads):
        start = i * chunk_size
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        chunk = lines[start:end]
        counter = []
        t = threading.Thread(target=process_lines, args=(chunk, counter))
        threads.append((t, counter))
        t.start()

    total_counter = Counter()
    for t, counter in threads:
        t.join()
        total_counter.update(counter[0])

    print("Word Frequencies:")
    for word, count in total_counter.most_common():
        print(f"{word}: {count}")



