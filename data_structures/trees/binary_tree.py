class Node:

    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        def insert(node, parent=None):
            if node is None:
                node = Node(value, parent)
            else:
                if value < node.data:
                    node.left = insert(node.left, node)
                elif value > node.data:
                    node.right = insert(node.right, node)
                else:
                    raise Exception(f'Node with value {value} already exists')
            return node

        self.root = insert(self.root)

    def remove(self, value):
        pass

    def preorder(self):
        def preorder(node):
            if node:
                yield node.data
                yield from preorder(node.left)
                yield from preorder(node.right)

        return preorder(self.root)

    def inorder(self):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.data
                yield from inorder(node.right)

        return inorder(self.root)

    def postorder(self):
        def postorder(node):
            if node:
                yield from postorder(node.left)
                yield from postorder(node.right)
                yield node.data

        return postorder(self.root)

    def min(self):
        if self.root is None:
            raise ValueError

        node = self.root
        while node.left is not None:
            node = node.left

        return node.data

    def max(self):
        if self.root is None:
            raise ValueError

        node = self.root
        while node.right is not None:
            node = node.right

        return node.data

    def __contains__(self, item):
        def search(node):
            if node is None:
                return False
            if item < node.data:
                return search(node.left)
            elif item > node.data:
                return search(node.right)
            return True

        return search(self.root)

    def __bool__(self):
        return self.root is not None


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(13)
    tree.insert(54)
    tree.insert(1)
    tree.insert(7)
    for e in tree.preorder():
        print(e)
    print(12 in tree)
    print(13 in tree)
