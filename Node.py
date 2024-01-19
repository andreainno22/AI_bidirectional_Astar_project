class Node:

    def __init__(self, state, parent=None, parent2=None, action=None, path_cost=0, effective_path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        """ state = [row, column] """
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.effective_path_cost = effective_path_cost
        self.parent2 = parent2
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def set_path_cost(self, path_cost):
        self.path_cost = path_cost

    def set_effective_path_cost(self, effective_path_cost):
        self.effective_path_cost = effective_path_cost

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node.state)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)
