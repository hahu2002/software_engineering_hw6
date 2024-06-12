class Visitor:
    def visit_container(self, container, prefix="", flag=0):
        raise NotImplementedError

    def visit_leaf(self, leaf, prefix="", flag=0):
        raise NotImplementedError

class TreeVisitor(Visitor):
    def visit_container(self, container, prefix="", flag=0):
        connector = ""
        print(f"{prefix}{connector}{container.icon} Tree Container: {container.name} at level {container.level}")
        new_prefix = prefix + ("   " if prefix else "")
        flag += 1
        for i, child in enumerate(container.children):
            if i == len(container.children) - 1:
                child.accept(self, max(0, (flag - 1)) * "│  " + max(0, len(new_prefix) // 3 - flag + 1) * "   " + "└──", flag - 1)
                flag -= 1
            else:
                child.accept(self, max(0, (flag - 1)) * "│  " + max(0, len(new_prefix) // 3 - flag + 1) * "   " + "├──", flag)

    def visit_leaf(self, leaf, prefix="", flag=0):
        print(f"{prefix}{leaf.icon} Tree Leaf: {leaf.name}")

class RectangleVisitor(Visitor):
    MAXLEN = 100

    def visit_container(self, container, prefix="", flag=0):
        connector = ""
        if container.level == 0:
            print(f"{container.icon} " + "┌" + "─" * (self.MAXLEN - 2) + "┐")
        length = len(f"│ {prefix}{connector} Rectangle Container: {container.name} at level {container.level} ")
        print(f"{container.icon} │ {prefix}{connector} Rectangle Container: {container.name} at level {container.level} " + (self.MAXLEN - length - 1) * "─" + "┤")
        new_prefix = prefix + ("   " if prefix else "")
        flag += 1
        for i, child in enumerate(container.children):
            if i == len(container.children) - 1:
                child.accept(self, max(0, (flag)) * "│  " + max(0, len(new_prefix) // 3 - flag) * "│  " + "├──", flag - 1)
                flag -= 1
            else:
                child.accept(self, max(0, (flag)) * "│  " + max(0, len(new_prefix) // 3 - flag) * "│  " + "├──", flag)
        if container.level == 0:
            print(f"{container.icon} " "└" + "─" * (self.MAXLEN - 2) + "┘")

    def visit_leaf(self, leaf, prefix="", flag=0):
        length = len(f"│ {prefix} Rectangle Leaf: {leaf.name} ")
        print(f"{leaf.icon} │ {prefix} Rectangle Leaf: {leaf.name} " + (self.MAXLEN - length - 1) * "─" + "┤")
