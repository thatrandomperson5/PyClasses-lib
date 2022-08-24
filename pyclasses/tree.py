class Branch:
    """A Branch of a Tree"""
    def __init__(self, **kwargs):
        self.set(**kwargs)
    def setitems(self, **kwargs):
        for name, item in kwargs.items():
            if name == "extend" or name == "setitems":
                error = f"Name: {name} is reserved."
                raise ValueError(error)
            setattr(self, name, item)
    def extend(self, name, **kwargs):
        setattr(self, name, Branch(**kwargs))
           

class Tree:
    pass
    