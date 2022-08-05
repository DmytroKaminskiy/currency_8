from time import time


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if not request.path.startswith('/admin/'):
            print('Admin site')

        start = time()
        response = self.get_response(request)
        end = time()
        print(f'Took Time: {end - start}')
        return response


'''
1. Создать модель ResponseLog с полями
    response_time = float
    request_method = string (GET, POST, ...) request.method
    query_params = string (?key=value) request.GET
    ip = string()
    path = string()  request.path
    ...

2. Создавать обьект ResponseLog (ResponseLog.objects.create()) с указанными полями.
3. Отправить имейл через вью класс ContactUsCreate
'''

# class SimpleMiddleware2:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         One-time configuration and initialization.
    #
    # def __call__(self, request):
    #     print('BEFORE VIEW')
    #     response = self.get_response(request)
    #     print('AFTER VIEW')
    #     return response