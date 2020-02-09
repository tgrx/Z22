import pytest

_FUNC_NAME = "benchmark"


def verify_module(module):
    assert hasattr(
        module, _FUNC_NAME
    ), f"module {module.__name__} has no attribute {_FUNC_NAME}"


def verify_function(func):
    assert callable(func), f"entity {func} is not a function"


def verify(module, capsys):
    verify_module(module)

    benchmark = getattr(module, _FUNC_NAME)
    verify_function(benchmark)

    dfilter = benchmark(filter)

    captured = capsys.readouterr()
    assert not captured.out, "no prints should occur when decorator is applied"

    assert list(dfilter(bool, [0, 1])) == list(filter(bool, [0, 1]))
    captured = capsys.readouterr()
    assert captured.out == "0\n"

    with pytest.raises(TypeError):
        dfilter(1, 2, 3)

    captured = capsys.readouterr()
    assert captured.out == "0\n"


def test(modules_level06, capsys):
    for module in modules_level06.values():
        verify(module, capsys)
