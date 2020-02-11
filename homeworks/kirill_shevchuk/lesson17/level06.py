import time


def benchmark(function, *ar, **kw):
    def decorator(*ar, **kw):
        try:
            start_time = time.time()
            function(*ar, **kw)
            print(int(time.time() - start_time))
        except Exception:
            print(0)
        return function(*ar, **kw)
    return decorator
