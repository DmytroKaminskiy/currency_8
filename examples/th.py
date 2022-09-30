from concurrent import futures
from time import sleep, time

import requests
from threading import Thread, current_thread

print(f'Main Thread: {current_thread()}')

def foo(num, num2=10):
    print(f'START FOO: {current_thread()}')
    sleep(num)
    print('END FOO')


# foo(3)
# foo(2)
# foo(4)

#################################
start = time()

####

# N + 1
# th1 = Thread(target=foo, args=[3])  # foo(3)
# th2 = Thread(target=foo, kwargs={'num': 5})  # foo(num=5)
# th3 = Thread(target=foo, args=[3], kwargs={'num2': 5})  # foo(3, num2=5)
# th4 = Thread(target=foo, args=[3], kwargs={'num2': 5})  # foo(3, num2=5)
#
# print('START THREADS')
# th1.start()
# th2.start()
# th3.start()
# th4.start()
#
# th1.join()
# th2.join()
# th3.join()
# th4.join()


########################

# threads = []
# for i in range(1, 11):
#     th = Thread(target=foo, args=[i])
#     threads.append(th)
#     th.start()
#
# for thread in  threads:
#     thread.join()

# import concurrent.futures
#
# def requests_get(url):
#     response = requests.get(url)
#     print(response.status_code)
#
#
# URLS = [
#     'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
#     'https://uk.wikipedia.org/wiki/%D0%92%D1%96%D0%BA%D1%96%D0%BF%D0%B5%D0%B4%D1%96%D1%8F:%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BB_%D1%81%D0%BF%D1%96%D0%BB%D1%8C%D0%BD%D0%BE%D1%82%D0%B8',
#     'https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D1%96_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B8',
#     'https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:LintErrors',
# ] * 40
#
# # 60.27
# # for url in URLS:
# #     requests_get(url)
#
# # 5 - 12, 10 - 6, 20 - 3.6, 40 - 3.2, 80 - 3.1, 160 - 3.2
# with concurrent.futures.ThreadPoolExecutor(160) as executor:
#     threads = []
#     for url in URLS:
#         threads.append(executor.submit(requests_get, url=url))
#
#     for th in threads:
#         th.result()

def countdown(n):
    while n != 0:
        n -= 1

N = 500_000_000_0

from multiprocessing import Process

# 13-14
# countdown(N)

# 13.8, 13.3
th1 = Process(target=countdown, args=[N // 2])
th2 = Process(target=countdown, args=[N // 2])

th1.start()
th2.start()

th1.join()
th2.join()
####

end = time()

print(f'Took time: {end - start} seconds.')

'''
IO - Thread !!!  GIL - global interpreter lock
CPU - Multiprocessing
'''
