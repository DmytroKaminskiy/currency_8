from time import time


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # if not request.path.startswith('/admin/'):
        #     print('Admin site')

        start = time()
        response = self.get_response(request)
        end = time()
        # print(f'Took Time: {end - start}')
        return response
