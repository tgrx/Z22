import importlib.util
import multiprocessing
import traceback
from pathlib import Path

import sys

PROJECT_DIR = Path(__file__).resolve().parent

HOMEWORKS_DIR = PROJECT_DIR / "homeworks"
LESSONS_DIR = PROJECT_DIR / "lessons"

ERROR_MSG = """
FAILED! test: `{test}`

# APP:
```
{app}
```

# ERROR:
```
{err}
```

# TRACEBACK:
```
{tb}
```
"""


def _import(module_path: Path, prefix=""):
    package_name = module_path.parent.name
    module_name = module_path.name[:-3]

    spec = importlib.util.spec_from_file_location(
        f"{prefix}.{package_name}.{module_name}", module_path.as_posix()
    )

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


class Runner(multiprocessing.Process):
    def __init__(self, results, mgr):
        super().__init__()
        self._results = results
        self._mgr = mgr

    def run(self) -> None:
        for test_path in LESSONS_DIR.glob("**/test_*.py"):
            print(f"\nrun test: {test_path.as_posix()}\n")

            self._results[test_path] = self._mgr.dict()

            test = _import(test_path, "tests")

            for homework_path in HOMEWORKS_DIR.glob("**/*.py"):
                print(f"\n\tcheck homework in {homework_path.as_posix()}")

                if not test.wants_path(homework_path):
                    print(f"\t\tskip: test does not want path")
                    continue

                homework_module = _import(homework_path, "homework_module")

                if not test.wants_module(homework_module):
                    print(f"\t\tskip: test does not want module")
                    continue

                try:
                    test.verify(homework_module)
                # pylint: disable=W0703
                except Exception as err:
                    print(
                        ERROR_MSG.format(
                            test=test_path,
                            app=homework_path,
                            err=err,
                            tb=traceback.format_exc(),
                        )
                    )

                    self._results[test_path][homework_path] = {
                        "result": "FAIL",
                        "error": err,
                        "traceback": traceback.format_exc(),
                    }
                else:
                    self._results[test_path][homework_path] = {
                        "result": "OK",
                        "error": None,
                        "traceback": None,
                    }

                    print("END test run\n\n")


def main():
    with multiprocessing.Manager() as mgr:
        results = mgr.dict()
        success = True

        runner = Runner(results=results, mgr=mgr)
        runner.start()
        runner.join(5)
        if runner.exitcode != 0:
            runner.terminate()
            print("TESTS FAILED")
            success = False

        print("\n\n[RESULTS]")

        for test_case, test_targets in results.items():
            print(f"\n[TEST] {test_case}")

            for homework, context in test_targets.items():
                status = context["result"]
                print(f"\t{homework}: {status}")
                if status != "OK":
                    print(f"\t\terror: {context['error']}")
                    print(
                        f"\n\t\t----- trace -----\n{context['traceback']}\t\t----- trace -----\n"
                    )
                    success = False

        return int(success is False)


if __name__ == "__main__":
    sys.exit(main())
