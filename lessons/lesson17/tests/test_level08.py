from project.utils import verify_names

_CLASS_NAME = "Functor"


def verify_module(module):
    assert hasattr(
        module, _CLASS_NAME
    ), f"module {module.__name__} has no attribute {_CLASS_NAME}"

    verify_names(module, "print")


def verify_class(klass):
    assert isinstance(klass, type), f"entity {klass} is not a class"


def verify(module):
    verify_module(module)

    functor_class = getattr(module, _CLASS_NAME)
    verify_class(functor_class)

    def func(arg1, arg2):
        return arg1 ** arg2

    functor = functor_class(func, (4,), {"arg2": 7})
    result = functor()

    assert result == 16384


def test(modules_level08):
    for module in modules_level08.values():
        verify(module)
