
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

    def sum_left_leaves(self):
        return self._sum_left_leaves_recursive(self.root, False)

    def _sum_left_leaves_recursive(self, node, is_left):
        if node is None:
            return 0

        if node.left is None and node.right is None and is_left:
            return node.data

        left_sum = self._sum_left_leaves_recursive(node.left, True)
        right_sum = self._sum_left_leaves_recursive(node.right, False)

        return left_sum + right_sum


tree = BinaryTree()

tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)

sum_left = tree.sum_left_leaves()
print("Sum of left leaves:", sum_left)