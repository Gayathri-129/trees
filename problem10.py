class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def print_nodes_at_odd_levels(self):
        self._print_odd_levels_recursive(self.root, 1)

    def _print_odd_levels_recursive(self, node, level):
        if node is None:
            return

        if level % 2 != 0:
            print(node.data, end=" ")

        self._print_odd_levels_recursive(node.left, level + 1)
        self._print_odd_levels_recursive(node.right, level + 1)


tree = BinaryTree()

tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(9)
tree.insert(5)
tree.insert(10)
tree.insert(6)

print("Nodes at odd levels:")
tree.print_nodes_at_odd_levels()