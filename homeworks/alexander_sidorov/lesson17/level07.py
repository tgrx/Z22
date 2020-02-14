from typing import NoReturn


def typecheck(func):
    def typechecked(*args, **kw):
        verify_args(func, args, kw)

        exc = None
        try:
            result = func(*args, **kw)
        except Exception as _e:
            result = None
            exc = _e

        verify_result(func, result, exc)

        if exc:
            raise exc

        return result

    return typechecked


def verify_args(func, args, kwargs):
    args_map = build_args_map(func, args, kwargs)

    for name, value in args_map.items():
        verify_arg(func, name, value)


def verify_result(func, result, exc):
    declared_return_type = func.__annotations__.get("return")
    if not declared_return_type:
        return

    must_raise = declared_return_type is NoReturn
    raised = bool(exc)

    if must_raise != raised:
        must_do = "raise an exception" if must_raise else "must return a value"
        did = "raised an exception" if raised else "returned a value"
        raise TypeError(f"function must {must_do}, but it {did} instead")

    if raised:
        return

    if not isinstance(result, declared_return_type):
        raise TypeError(
            f"invalid return type:"
            f" expected {declared_return_type},"
            f" got {type(result)}({result})"
        )


def build_args_map(func, args, kwargs):
    args_map = dict(zip(func.__code__.co_varnames, args))
    args_map.update(kwargs)

    return args_map


def verify_arg(func, arg_name, arg_value):
    declared_arg_type = func.__annotations__.get(arg_name)

    if not declared_arg_type:
        return

    if not isinstance(arg_value, declared_arg_type):
        raise TypeError(
            f"invalid type for arg {arg_name}:"
            f" expected {declared_arg_type},"
            f" got {type(arg_value)}({arg_value})"
        )
