from time import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time()
        try:
            answer = func(*args, **kwargs)
        finally:
            end = time()
            print(int(end - start))
        return answer

    return wrapper
