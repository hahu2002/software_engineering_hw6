# funny_json_explorer.py
class FunnyJsonExplorer:
    def __init__(self, factory):
        self.factory = factory

    def show(self, json_data):
        container = self.factory.create_container('Main Container', 0)
        self._parse_json(json_data, container)
        visitor = self.factory.create_visitor()
        container.accept(visitor)

    def _parse_json(self, data, parent_container):
        for key, value in data.items():
            if isinstance(value, dict):
                child_container = self.factory.create_container(key, parent_container.level + 1)
                parent_container.add(child_container)
                self._parse_json(value, child_container)
            else:
                if value is not None:
                    key = f"{key} : {value}"
                leaf = self.factory.create_leaf(key)
                parent_container.add(leaf)



'''
class FunnyJsonExplorer:
    def __init__(self, factory):
        self.factory = factory

    def show(self, json_data):
        container = self.factory.create_container( 'Main Container' , 0 )
        self._parse_json( json_data , container )
        container.draw()

    def _parse_json( self , data , parent_container ):
        for key , value in data.items():
            if isinstance( value , dict ):
                child_container = self.factory.create_container( key , parent_container.level + 1)
                parent_container.add(child_container)
                self._parse_json( value , child_container )
            else:
                if value is not None:
                    key = f"{key} : {value}"
                leaf = self.factory.create_leaf( key )
                parent_container.add(leaf)
'''