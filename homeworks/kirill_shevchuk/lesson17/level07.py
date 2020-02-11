def typecheck(function, *ar, **kw):
    def decorator(*ar, **kw):
        type_hints = function.__annotations__
        for key, value in type_hints:
            if key == "return":
                if not isinstance(function(*ar, **kw), value):
                    raise TypeError
            elif not isinstance(key, value):
                raise TypeError
        return function(*ar, **kw)
    return decorator