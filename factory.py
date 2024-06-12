# factory.py
from container import RectangleContainer, TreeContainer
from leaf import RectangleLeaf, TreeLeaf
from abstract_factory import AbstractFactory
from visitor import TreeVisitor, RectangleVisitor

class RectangleFactory(AbstractFactory):
    def __init__(self, icon_family):
        self.icon_family = icon_family
        self.name = 'rectangle'

    def create_container(self, name, level):
        return RectangleContainer(self.icon_family.get_icon('container'), name, level)

    def create_leaf(self, name):
        return RectangleLeaf(self.icon_family.get_icon('leaf'), name)

    def create_visitor(self):
        return RectangleVisitor()

class TreeFactory(AbstractFactory):
    def __init__(self, icon_family):
        self.icon_family = icon_family
        self.name = 'tree'

    def create_container(self, name, level):
        return TreeContainer(self.icon_family.get_icon('container'), name, level)

    def create_leaf(self, name):
        return TreeLeaf(self.icon_family.get_icon('leaf'), name)

    def create_visitor(self):
        return TreeVisitor()







'''
from container import RectangleContainer
from leaf import RectangleLeaf
from container import TreeContainer
from leaf import TreeLeaf
from abstract_factory import AbstractFactory

class RectangleFactory(AbstractFactory):
    def __init__(self, icon_family):
        self.icon_family = icon_family
        self.name = 'rectangle'

    def create_container(self, name, level):
        return RectangleContainer(self.icon_family.get_icon('container'), name, level)

    def create_leaf(self, name):
        return RectangleLeaf(self.icon_family.get_icon('leaf'), name)

class TreeFactory(AbstractFactory):
    def __init__(self, icon_family):
        self.icon_family = icon_family
        self.name = 'tree'

    def create_container(self, name, level):
        return TreeContainer(self.icon_family.get_icon('container'), name, level)

    def create_leaf(self, name):
        return TreeLeaf(self.icon_family.get_icon('leaf'), name)
'''