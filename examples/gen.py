# lst = [1, 2, 3, 4]  # 123 ns ± 1.21 ns per loop
#
# def gen():  # 305 ns ± 1.85
#     for i in range(1, 5):
#         yield i
#
#
# it = lst.__iter__()
# print(id(lst))
# print(id(it))
#
# g = gen()
# print(id(g))
# print(id(g.__iter__()))
#
# for i in g:
#     print(i)
#
# for i in g:
#     print(i)

# for i in lst:
#     i + i
#
# for i in gen():
#     i + i

# import requests
#
#
# url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/640px-Python-logo-notext.svg.png'
# response = requests.get(url)
# print(response.status_code)
#
# with open('./python.png', 'wb') as file:
#     file.write(response.content)

# import requests
# import uuid
# import io
#
#
# def send_to_server(content):
#     print(len(content))  # send here
#
#
# url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/640px-Python-logo-notext.svg.png'
# response = requests.get(url)
#
# # filepath = f'./{uuid.uuid4()}python.png'
# # with open(filepath, 'wb') as file:
# #     file.write(response.content)
#
# send_to_server(response.content)


# import csv
# import io
#
# def send_to_server(content: bytes):
#     if not isinstance(content, bytes):
#         raise TypeError('Invalid type for content')
#
#     print(len(content))  # send here
#
# fileobj = io.StringIO()
# spamwriter = csv.writer(fileobj)
# spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
# spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
#
# fileobj.seek(0)
# send_to_server(fileobj.read().encode())

# with open(filepath, 'rb') as file:
#     send_to_server(file.read())
