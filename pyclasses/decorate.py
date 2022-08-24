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

    def __init_subclass__(cls, **kwargs) -> None:
        for name, method in inspect.getmembers(cls):

            if not name.startswith("__"):
                if inspect.isfunction(method):
                    setattr(cls, name, DecoratableClassMethod(method, cls))


def decoratable(cls):
    """Set the decorated class to be decoratable."""
    for name, method in inspect.getmembers(cls):

        if not name.startswith("__"):
            if inspect.isfunction(method):
                setattr(cls, name, DecoratableClassMethod(method, cls))
    return cls


def class_decorator(func):
    def inner(func):
        a = False
        try:
            return func(func.cls, func.method)
        except:
            a = True
        if a:
            error = "Method is not a DecoratableClassMethod, make sure your decorator is inside a decoratable class."
            raise TypeError(error)

    return inner
