class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class PerfectBinaryTree:
    def __init__(self):
        self.root = None

    def construct_tree(self, height):
        self.root = self._construct_recursive(height, 1)

    def _construct_recursive(self, height, level):
        if level > height:
            return None

        node = Node(level)
        node.left = self._construct_recursive(height, level + 1)
        node.right = self._construct_recursive(height, level + 1)

        return node

    def sum_of_all_nodes(self):
        return self._sum_recursive(self.root)

    def _sum_recursive(self, node):
        if node is None:
            return 0

        return (
            node.data + self._sum_recursive(node.left) + self._sum_recursive(node.right)
        )


tree = PerfectBinaryTree()
tree_height = 3  # Height of the perfect binary tree

tree.construct_tree(tree_height)

total_sum = tree.sum_of_all_nodes()
print("Sum of all nodes:", total_sum)