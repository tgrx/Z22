from project.utils import verify_names

_FUNC_NAME = "trivial_decorator"


def verify_module(module):
    assert hasattr(
        module, _FUNC_NAME
    ), f"module {module.__name__} has no attribute {_FUNC_NAME}"

    verify_names(module, "print")


def verify_function(func):
    assert callable(func), f"entity {func} is not a function"


def verify(module):
    verify_module(module)

    trivial_decorator = getattr(module, _FUNC_NAME)
    verify_function(trivial_decorator)

    dataset = (
        "yxz",
        [1, 2, 3, 4, 5],
        range(0, 100, 3),
        {1, 2, 3, 4, 5},
        {1: 5, 2: 4, 3: 3, 4: 2, 5: 1},
    )

    functions = (
        bool,
        callable,
        id,
        lambda _i: _i is None,
        lambda _i: _i is not None,
        str,
    )

    for func in functions:
        decorated = trivial_decorator(func)
        for data in dataset:
            expected = func(data)
            got = decorated(data)

            assert expected == got, f"mismatch at `{data}` with decorated `{func}`"

    dec_filter = trivial_decorator(filter)
    assert list(dec_filter(bool, [0, 1])) == list(filter(bool, [0, 1]))


def test(modules_level05):
    for module in modules_level05.values():
        verify(module)
