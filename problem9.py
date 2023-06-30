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

    def max_level_sum(self):
        max_sum = float("-inf")
        max_level = 0
        current_level = 1

        while True:
            level_sum = self._calculate_level_sum(self.root, current_level)

            if level_sum == 0:
                break

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

            current_level += 1

        return max_sum, max_level

    def _calculate_level_sum(self, node, level):
        if node is None:
            return 0

        if level == 1:
            return node.data

        left_sum = self._calculate_level_sum(node.left, level - 1)
        right_sum = self._calculate_level_sum(node.right, level - 1)

        return left_sum + right_sum

tree = BinaryTree()

tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(9)
tree.insert(7)

max_sum, max_level = tree.max_level_sum()
print("Maximum level sum:", max_sum)
print("Level with maximum sum:", max_level)