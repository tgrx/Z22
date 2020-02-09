from project.utils import verify_names

_FUNC_NAME = "my_filter"


def verify_module(module):
    assert hasattr(
        module, _FUNC_NAME
    ), f"module {module.__name__} has no attribute {_FUNC_NAME}"

    verify_names(module, "filter", "print")


def verify_function(func):
    assert callable(func), f"entity {func} is not a function"


def verify(module):
    verify_module(module)

    my_filter = getattr(module, _FUNC_NAME)
    verify_function(my_filter)

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
        hash,
        id,
        lambda _i: _i is None,
        lambda _i: _i is not None,
        str,
    )

    for func in functions:
        for data in dataset:
            expected = list(filter(func, data))
            got = my_filter(func, data)

            assert (
                expected == got
            ), f"mismatch when filtered `{data}` using `{func.__name__}`"


def test(modules_level04):
    for module in modules_level04.values():
        verify(module)
