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

    def bfs_traversal(self):
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs_traversal(self):
        if self.root is None:
            return

        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.data, end=" ")

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


tree = BinaryTree()

tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)

print("BFS traversal:")
tree.bfs_traversal()

print("\nDFS traversal:")
tree.dfs_traversal()