class Branch:
    """A Branch of a Tree"""
    def __init__(self, **kwargs):
        self.setitems(**kwargs)
    def setitems(self, **kwargs):
        for name, item in kwargs.items():
            if name in ["setitems", "extend"]:
                error = f"Name: {name} is reserved."
                raise ValueError(error)
            setattr(self, name, item)
    def extend(self, name, **kwargs):
        setattr(self, name, Branch(**kwargs))
           
def extend(cls, name, **kwargs):
    setattr(cls, name, Branch(**kwargs))

class Tree:
    def extend(self, name, **kwargs):
        extend(self, name, **kwargs)



    