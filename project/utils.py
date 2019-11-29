import importlib.util
from pathlib import Path


def import_by_path(module_path: Path):
    package_name = ".".join(module_path.parts[-4:-1])
    module_name = module_path.name[:-3]

    spec = importlib.util.spec_from_file_location(
        f"{package_name}.{module_name}", module_path.as_posix()
    )
    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    return module
