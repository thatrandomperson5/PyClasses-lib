from pyclasses import Tree


class mytree(Tree):
    def __init__(self):
        print(self.__init__)
        print(self.test)
        self.test()

    def test(self):
        self.x = 1
        print(self.x)
        self.extend("y", y=2, x=3)
        print(self.y.y)
        print(self.y.x)
        self.y.extend("z", a="hi", b="hello")
        print(self.y.z.a)
        print(self.y.z.b)


mytree()
