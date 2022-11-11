'''
Threading - IO
Multiprocessing - CPU
Async - IO (!one thread!)
'''

from time import sleep, time

# def foo():
#     print('START FOO')
#     sleep(1)  # poshel za yablokami
#     print('END FOO')

# start = time()

# foo()
# foo()
# foo()

# end = time()
# print(f'Time: {end - start}')

import asyncio
# import requests
import httpx

# async def foo():
#     print('Foo Start')
#     # sleep(1)
#     await asyncio.sleep(1)
#     # await sleep(1)
#     print('Foo End')
#
# async def main():
#     await asyncio.gather(foo(), foo(), foo())
#
# start = time()
# # # event loop
# asyncio.run(main())
# print(f'Took time: {time() - start}')


async def fetch_url(url: str) -> int:
    # response = httpx.get(url)
    # print(response.status_code)
    # Rate.objects.all().order_by().filter()
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        print(response.status_code)
        return response.status_code
    #     print(url)

async def main():
    urls = [
               'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
               'https://uk.wikipedia.org/wiki/%D0%92%D1%96%D0%BA%D1%96%D0%BF%D0%B5%D0%B4%D1%96%D1%8F:%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BB_%D1%81%D0%BF%D1%96%D0%BB%D1%8C%D0%BD%D0%BE%D1%82%D0%B8',
               'https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D1%96_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B8',
               'https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:LintErrors',
           ] * 40
    await asyncio.gather(*[fetch_url(url) for url in urls])
    # await asyncio.gather(fetch_url(url), fetch_url(url), fetch_url(url), ...)

    # def foo_args(*args):
    #     print(args)
    # foo_args([1, 2, 3])
    # foo_args(*[1, 2, 3])



start = time()
# event loop
asyncio.run(main())
print(f'Took time: {time() - start}')

'''
django - 10_000  - 2 server == 50_000 = 10
fastapi - 10_000 - 1 server == 50_000 = 5

'''