# container.py
class Container:
    def __init__(self, icon, name, level):
        self.icon = icon
        self.name = name
        self.level = level
        self.children = []

    def add(self, component):
        self.children.append(component)

    def accept(self, visitor, prefix="", flag=0):
        visitor.visit_container(self, prefix, flag)

class TreeContainer(Container):
    def __init__(self, icon, name, level):
        super().__init__(icon, name, level)

class RectangleContainer(Container):
    def __init__(self, icon, name, level):
        super().__init__(icon, name, level)






'''
class Container:
    def __init__(self, icon, name, level):
        self.icon = icon
        self.name = name
        self.level = level
        self.children = []

    def add(self, component):
        self.children.append(component)

    def draw(self):
        raise NotImplementedError

# Tree Container
class TreeContainer(Container):
    def draw( self , prefix="" , flag = 0 ):
        connector = "" #"───" if prefix else ""
        print(f"{prefix}{connector}{self.icon} Tree Container: {self.name} at level {self.level}")
        new_prefix = prefix + ("   " if prefix else "")
        flag += 1
        for i, child in enumerate(self.children):
            if i == len(self.children) - 1:
                child.draw( max( 0 , ( flag - 1 ) ) * "│  " + max( 0 , len(new_prefix) // 3 - flag + 1 ) * "   " + "└──" , flag - 1 )
                flag -= 1
            else:
                child.draw( max( 0 , ( flag - 1 ) ) * "│  " + max( 0 , len(new_prefix) // 3 - flag + 1 ) * "   " + "├──" , flag )

# Rectangle Container
class RectangleContainer(Container):
    MAXLEN = 100
    def draw( self , prefix="" , flag = 0 ):
        connector = "" #"───" if prefix else ""
        if ( self.level == 0 ):
            print( f"{self.icon} " + "┌" + "─" * ( self.MAXLEN - 2 ) + "┐")
        length = len( f"│ {prefix}{connector} Rectangle Container: {self.name} at level {self.level} " )
        print(f"{self.icon} │ {prefix}{connector} Rectangle Container: {self.name} at level {self.level} " + ( self.MAXLEN - length - 1 ) * "─" + "┤" )
        new_prefix = prefix + ("   " if prefix else "")
        flag += 1
        for i, child in enumerate(self.children):
            if i == len(self.children) - 1:
                child.draw( max( 0 , ( flag ) ) * "│  " + max( 0 , len(new_prefix) // 3 - flag ) * "│  " + "├──" , flag - 1 )
                flag -= 1
            else:
                child.draw( max( 0 , ( flag ) ) * "│  " + max( 0 , len(new_prefix) // 3 - flag ) * "│  " + "├──" , flag )
        if ( self.level == 0 ):
            print( f"{self.icon} " "└" + "─" * ( self.MAXLEN - 2 ) + "┘" )
'''