from dataclasses import dataclass
from typing import Callable, Type, Any
import inspect
from .tools import ClassCallable


@dataclass
class DecoratableClassMethod(ClassCallable):
    method: Callable
    cls: Type

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.method(self.cls, *args, **kwargs)

    def __str__(self):
        return str(self.method)

    def __repr__(self):
        return repr(self.cls)


class Decoratable:
    """Set the subclased class and all sublacces of that class to be decoratable."""

    def __new__(cls, *args, **kwargs) -> None:
        for name, method in inspect.getmembers(cls):

            if not name.startswith("_"):
                if inspect.isfunction(method):
                    setattr(cls, name, DecoratableClassMethod(method, cls))
        cls = super().__new__(cls, *args, **kwargs)
        return cls


def class_decorator(func):
    def inner(func):
        a = False
        try:
            out = func(func.cls, func.method)
        except Exception:
            a = True
        if a:
            error = "Method is not a DecoratableClassMethod, make sure your decorator is inside a decoratable class."
            raise TypeError(error)
        if out is None:
            return func
        else:
            return out

    return inner
