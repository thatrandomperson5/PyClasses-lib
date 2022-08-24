import inspect


class ClassCallable:
    """Subclass this to be aprroved for checks."""

    pass


def is_cc(object):
    """Checks if an object is a function, method or ClassCallable."""
    return inspect.isfunction(object) or inspect.ismethod(object) or isinstance(object, ClassCallable)
