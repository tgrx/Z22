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


def verify_typecheck_untyped(decorator):
    @decorator
    def untyped(arg1, arg2):
        return arg1 / arg2

    try:
        untyped(1, 1)
    except Exception as err:
        raise AssertionError(f"type check failed") from err

    with pytest.raises(ZeroDivisionError):
        untyped(1, 0)


def verify_typecheck_args(decorator):
    @decorator
    def typed_args(arg1: int, arg2: int):
        return arg1 / arg2

    try:
        typed_args(1, 1)
    except Exception as err:
        raise AssertionError(f"type check failed") from err

    with pytest.raises(ZeroDivisionError):
        typed_args(1, 0)

    with pytest.raises(TypeError):
        typed_args(1j, 0)

    with pytest.raises(TypeError):
        typed_args(1, 0j)


def verify_typecheck_return(decorator):
    @decorator
    def typed_return(arg1, arg2) -> float:
        return arg1 / arg2

    try:
        typed_return(1, 1)
    except Exception as err:
        raise AssertionError("decorator failed") from err

    with pytest.raises(TypeError):

        class _C:
            def __truediv__(self, other):
                raise KeyError

        typed_return(_C(), 0)

    with pytest.raises(TypeError):
        typed_return(1, 0)

    with pytest.raises(TypeError):
        typed_return(1j, 2j)


def verify_typecheck_raise(decorator):
    @decorator
    def typed_noreturn(arg1, arg2) -> NoReturn:
        return arg1 / arg2

    with pytest.raises(ZeroDivisionError):
        typed_noreturn(1, 0)

    with pytest.raises(TypeError):
        typed_noreturn(1, 2)


def verify(module):
    verify_module(module)

    typecheck = getattr(module, _FUNC_NAME)
    verify_function(typecheck)

    verify_typecheck_untyped(typecheck)
    verify_typecheck_args(typecheck)
    verify_typecheck_return(typecheck)
    verify_typecheck_raise(typecheck)


def test(modules_level07):
    for module in modules_level07.values():
        verify(module)
