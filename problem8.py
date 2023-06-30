
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

    def count_subtrees_with_sum(self, target_sum):
        count = self._count_subtrees_with_sum_recursive(self.root, target_sum)
        return count

    def _count_subtrees_with_sum_recursive(self, node, target_sum):
        if node is None:
            return 0

        count = 0

        left_sum = self._calculate_subtree_sum(node.left)
        right_sum = self._calculate_subtree_sum(node.right)

        if node.data + left_sum + right_sum == target_sum:
            count += 1

        count += self._count_subtrees_with_sum_recursive(node.left, target_sum)
        count += self._count_subtrees_with_sum_recursive(node.right, target_sum)

        return count

    def _calculate_subtree_sum(self, node):
        if node is None:
            return 0

        return (
            node.data
            + self._calculate_subtree_sum(node.left)
            + self._calculate_subtree_sum(node.right)
        )


tree = BinaryTree()

tree.insert(5)
tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(8)
tree.insert(7)
tree.insert(9)

target_sum = 7
count = tree.count_subtrees_with_sum(target_sum)
print("Number of subtrees with sum", target_sum, ":", count)