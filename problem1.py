class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)

    def inorder_traversal(self):
        if self.left is not None:
            self.left.inorder_traversal()
        print(self.value)
        if self.right is not None:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.value)
        if self.left is not None:
            self.left.preorder_traversal()
        if self.right is not None:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left is not None:
            self.left.postorder_traversal()
        if self.right is not None:
            self.right.postorder_traversal()
        print(self.value)


def main():
    root = BinaryTree(10)
    root.insert(5)
    root.insert(15)
    root.insert(2)
    root.insert(7)
    root.insert(12)
    root.insert(17)

    print("Inorder traversal:")
    root.inorder_traversal()

    print("Preorder traversal:")
    root.preorder_traversal()

    print("Postorder traversal:")
    root.postorder_traversal()


if __name__ == "__main__":
    main()