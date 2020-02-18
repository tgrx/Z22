from typing import NoReturn


def typecheck(function):
    def typechecked(*ar, **kw):
        verify_args(function, ar, kw)

        exc = None
        try:
            result = function(*ar, *kw)
        except Exception as _e:
            result = None
            exc = _e
        verify_result(function, result, exc)

        if exc:
            raise exc

        return result

    return typechecked


def verify_args(fun, arg, kwarg):
    args_map = build_args_map(fun, arg, kwarg)

    for name, value in args_map.items():
        verify_arg(fun, name, value)


def verify_result(fun, result, exc):

    declared_return_type = fun.__annotations__.get("return")

    if not declared_return_type:
        return None

    must_raise = declared_return_type is NoReturn
    raised = bool(exc)

    if must_raise != raised:
        raise TypeError

    if raised:
        return None

    if not isinstance(result, declared_return_type):
        raise TypeError

    return None


def build_args_map(fun, arg, kwarg):
    args_map = dict(zip(fun.__code__.co_varnames, arg))
    args_map.update(kwarg)
    return args_map


def verify_arg(fun, arg_name, arg_value):
    declared_arg_type = fun.__annotations__.get(arg_name)

    if not declared_arg_type:
        return None

    if not isinstance(arg_value, declared_arg_type):
        raise TypeError

    return None
