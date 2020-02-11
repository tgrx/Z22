def typecheck(function):
    def decorator():
        print(get_type_hints())
    return decorator