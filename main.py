from pyclasses import Tree
class mytree(Tree):
    def __init__(self):
        self.x = 1
        print(self.x)
        self.extend("y", y=2, x=3)
        print(self.y.y)
        print(self.y.x)
mytree()