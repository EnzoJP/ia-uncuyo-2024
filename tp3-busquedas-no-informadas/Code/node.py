
class Node:
    def __init__(self, state=None, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action  # Acción que llevó a este nodo desde su padre
        self.children = []

    def add_child(self, child):
        self.children.append(child)