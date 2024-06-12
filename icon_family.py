# icon_family.py
class IconFamily:
    def get_icon(self, component_type):
        raise NotImplementedError

class ChessIconFamily(IconFamily):
    def __init__(self):
        self.name = 'chess'
    def get_icon(self, component_type): 
        icons = {
            'container': '♔',
            'leaf': '♙'
        }
        return icons.get(component_type, '')

class SmileIconFamily(IconFamily):
    def __init__(self):
        self.name = 'smile'
    def get_icon(self, component_type):
        icons = {
            'container': '😉',
            'leaf': '😎'
        }
        return icons.get(component_type, '')
