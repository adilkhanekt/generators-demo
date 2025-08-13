print("--------- Generator and list comparison ---------")

import tracemalloc


tracemalloc.start()


# x = (i for i in range(100))
x = [i for i in range(100)]

current, peak = tracemalloc.get_traced_memory()

print(f"Current memory usage: {current / 1024:.2f} KB")  # Memory currently used
print(f"Peak memory usage: {peak / 1024:.2f} KB")  # Peak memory usage during runtime

tracemalloc.stop()



print("--------- Generators experiments ---------")

from typing import List

# Regular list with while loop example
def get_pow(start_num: int, end_num: int) -> List:
    result = []
    while start_num <= end_num:
        result.append(start_num**2)
        start_num +=1
    return result

# print(get_pow(1, 10000000))



# Generator with while loop example
def get_pow_yield(start_num: int, end_num: int):
    result = []
    while start_num <= end_num:
        yield start_num**2
        start_num +=1

# creates generator object
pow_gen = get_pow_yield(1, 10)
print(pow_gen)

# Iterating over first 3 elements of generator object
pow1 = next(pow_gen)
pow2 = next(pow_gen)
pow3 = next(pow_gen)

print(f"First: {pow1}, second: {pow2}, third: {pow3}")

# Iterating over entire generator object, but it actually starts from 4th element.
# The reason is that generator function keeps current state, and simply continues with the next element.
for i in pow_gen:
    print(i)
