import time


def benchmark(function):
    def decorator(*ar, **kw):
        start_time = time.time()
        try:
            return function(*ar, **kw)
        finally:
            print(int(time.time() - start_time))

    return decorator
