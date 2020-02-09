from project.utils import verify_names

_FUNC_NAME = "my_map"


def verify_module(module):
    assert hasattr(
        module, _FUNC_NAME
    ), f"module {module.__name__} has no attribute {_FUNC_NAME}"

    verify_names(module, "map", "print")


def verify_function(func):
    assert callable(func), f"entity {func} is not a function"


def verify(module):
    verify_module(module)

    my_map = getattr(module, _FUNC_NAME)
    verify_function(my_map)

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
        str,
    )

    for func in functions:
        for data in dataset:
            expected = list(map(func, data))
            got = my_map(func, data)

            assert (
                expected == got
            ), f"mismatch when applied `{func.__name__}` to `{data}`"


def test(modules_level03):
    for module in modules_level03.values():
        verify(module)
