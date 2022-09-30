def hello():
    return "Hello"


def world():
    return "World"


urls = {
    "/world/": world,
    "/hello/": hello,
}

def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
