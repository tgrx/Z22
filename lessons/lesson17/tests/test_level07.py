from typing import NoReturn

import pytest

from project.utils import verify_names

_FUNC_NAME = "typecheck"


def verify_module(module):
    assert hasattr(
        module, _FUNC_NAME
    ), f"module {module.__name__} has no attribute {_FUNC_NAME}"

    verify_names(module, "print")


def verify_function(func):
    assert callable(func), f"entity {func} is not a function"


def verify_typecheck_trivial(decorator):
    @decorator
    def decoratee(arg1, arg2):
        return arg1 + arg2

    try:
        decoratee("a", "b")
    except Exception:
        raise AssertionError("typecheck failed")


def verify_typecheck_args(decorator):
    @decorator
    def decoratee(arg1: str, arg2: int):
        if not arg1:
            return ""
        return arg1[:-1] + arg1[-1] * arg2

    try:
        decoratee("a", 1)
    except Exception:
        raise AssertionError("decorator failed")

    with pytest.raises(TypeError):
        decoratee([1], 1)

    with pytest.raises(TypeError):
        decoratee([1], "x")


def verify_typecheck_return(decorator):
    @decorator
    def decoratee(arg1, arg2) -> str:
        return arg1 + arg2

    try:
        decoratee("a", "b")
    except Exception:
        raise AssertionError("decorator failed")

    with pytest.raises(TypeError):
        decoratee(1, 2)

    with pytest.raises(TypeError):
        decoratee([1], [2])

    with pytest.raises(TypeError):
        decoratee([1], 2)


def verify_typecheck_raise(decorator):
    @decorator
    def decoratee(arg1, arg2) -> NoReturn:
        return arg1 / arg2

    try:
        decoratee(1, 0)
    except ZeroDivisionError:
        pass
    except Exception:
        raise AssertionError("decorator failed")

    with pytest.raises(TypeError):
        decoratee(1, 2)


def verify(module):
    verify_module(module)

    typecheck = getattr(module, _FUNC_NAME)
    verify_function(typecheck)

    verify_typecheck_trivial(typecheck)
    verify_typecheck_args(typecheck)
    verify_typecheck_return(typecheck)
    verify_typecheck_raise(typecheck)


def test(modules_level07):
    for module in modules_level07.values():
        verify(module)
