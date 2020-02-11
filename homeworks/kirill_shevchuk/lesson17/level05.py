def trivial_decorator(function):
    def decorator(*ar, **kw):
        return function(*ar, **kw)
    return decorator