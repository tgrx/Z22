def typecheck(function, *ar, **kw):
    def decorator(*ar, **kw):
        type_hints = function.__annotations__
        for key, value in type_hints:
            if key == "return":
                result = function(*ar, **kw)
                if not isinstance(result, value):
                    raise TypeError
            elif not isinstance(key, value):
                raise TypeError
        return result
    return decorator