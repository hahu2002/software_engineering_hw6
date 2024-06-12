# leaf.py
class Leaf:
    def __init__(self, icon, name):
        self.icon = icon
        self.name = name

    def accept(self, visitor, prefix="", flag=0):
        visitor.visit_leaf(self, prefix, flag)

class TreeLeaf(Leaf):
    def __init__(self, icon, name):
        super().__init__(icon, name)

class RectangleLeaf(Leaf):
    def __init__(self, icon, name):
        super().__init__(icon, name)



'''
class Leaf:
    def __init__(self, icon, name):
        self.icon = icon
        self.name = name

    def draw(self):
        raise NotImplementedError

class TreeLeaf(Leaf):
    def draw( self , prefix="" , flag = 0 ):
        print(f"{prefix}{self.icon} Tree Leaf: {self.name}")

class RectangleLeaf(Leaf):
    MAXLEN = 100
    def draw( self , prefix="" , flag = 0 ):
        length = len( f"│ {prefix} Rectangle Leaf: {self.name} " )
        print(f"{self.icon} │ {prefix} Rectangle Leaf: {self.name} " + ( self.MAXLEN - length - 1 ) * "─" + "┤" )
        # print(f"{prefix}{self.icon} Rectangle Leaf: {self.name}")
'''