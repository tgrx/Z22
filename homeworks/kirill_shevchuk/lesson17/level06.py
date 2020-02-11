import time


def benchmark(function, *ar, **kw):
    def decorator(*ar, **kw):
        start_time = time.time()
        function(*ar, **kw)
        print(int(time.time() - start_time))
        return function(*ar, **kw)
    return decorator
