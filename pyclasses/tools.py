from dataclasses import dataclass
from typing import Callable, Type, Any
import inspect


@dataclass
class DecoratableClassMethod:
    method: Callable
    cls: Type

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.method(self.cls, *args, **kwargs)

    def __str__(self):
        return str(self.method)

    def __repr__(self):
        return repr(self.cls)


class Decoratable:
    def __init_subclass__(cls, **kwargs) -> None:
        for name, method in inspect.getmembers(cls):

            if not name.startswith("__"):
                if inspect.isfunction(method):
                    setattr(cls, name, DecoratableClassMethod(method, cls))
