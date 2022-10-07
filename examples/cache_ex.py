from time import sleep, time

import hashlib


CACHE = {}


def slow_func(num, power):
    global CACHE  #  LEGB

    cache_key = hashlib.sha1(f'slow_func::{num}::{power}'.encode()).hexdigest()

    print(num, power, CACHE)

    if cache_key in CACHE:
        return CACHE[cache_key]
    else:
        sleep(num)
        result = num ** power
        CACHE[cache_key] = result
        return result



def slow_func2(num, power):
    global CACHE

    cache_key = hashlib.sha1(f'slow_func2::{num}::{power}'.encode()).hexdigest()

    # hash('ab') -> 'abc'
    # hash('ba') -> 'abc'

    print(num, power, CACHE)

    if cache_key in CACHE:
        return CACHE[cache_key]
    else:
        sleep(num)
        result = num - power
        CACHE[cache_key] = result
        return result


start = time()

print(slow_func(3, 6))
print(slow_func(3, 6))
print(slow_func2(3, 6))
print(slow_func2(3, 6))

end = time()
print(f'time: {end - start}')  # 7
