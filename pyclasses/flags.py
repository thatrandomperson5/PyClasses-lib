from dataclasses import dataclass
from typing import Callable, Any


@dataclass
class FlaggedMethod:
    method: Callable
    type: str

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.method(*args, **kwargs)

    def __str__(self):
        return str(self.method)

    def __repr__(self):
        return repr(self.cls)


def flag(type):
    def Inner(func):
        return FlaggedMethod(func, type)

    return Inner
