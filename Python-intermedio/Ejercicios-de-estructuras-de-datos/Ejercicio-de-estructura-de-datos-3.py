class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)
    def _insert_recursive(self, current, new_node):
        if new_node.value < current.value:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)
    def print_tree(self):
        self._in_order(self.root)
    def _in_order(self, node):
        if node is not None:
            self._in_order(node.left)
            print(node.value)
            self._in_order(node.right)
