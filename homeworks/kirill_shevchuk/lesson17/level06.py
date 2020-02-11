import time


def benchmark(function, *ar, **kw):
    def decorator(*ar, **kw):
        try:
            start_time = time.time()
            result = function(*ar, **kw)
        finally:
            print(int(time.time() - start_time))
        return result
    return decorator
