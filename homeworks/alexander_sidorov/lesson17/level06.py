from datetime import datetime


def benchmark(func):
    def decorated(*args, **kw):
        ts_start = datetime.now()
        try:
            return func(*args, **kw)
        finally:
            delta = datetime.now() - ts_start
            total = int(delta.total_seconds())
            print(f"{total}")

    return decorated
