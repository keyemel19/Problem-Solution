
'''Solution for Problem 1'''

class Node:
    def __init__(self, data):
        """Initialize a node in the binary tree."""
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        """Initialize an empty binary tree."""
        self.root = None

    def insert(self, data):
        """Inserts a new node into the binary tree."""
        if not self.root:
            # If the tree is empty, set the new node as the root.
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        """
        Helper function to recursively insert a node into the binary tree.
        """
        if data < current.data:
            # If data is less than current node's data, go left.
            if current.left is None:
                # If the left child is empty, insert the new node here.
                current.left = Node(data)
            else:
                # Recursively traverse to the left subtree.
                self._insert_recursive(current.left, data)
        elif data > current.data:
            # If data is greater than current node's data, go right.
            if current.right is None:
                # If the right child is empty, insert the new node here.
                current.right = Node(data)
            else:
                # Recursively traverse to the right subtree.
                self._insert_recursive(current.right, data)

    def find_max_element(self):
        """Finds the maximum element in the binary tree."""
        if self.root is None:
            return float('-inf')

        return self._find_max_recursive(self.root)

    def _find_max_recursive(self, node):
        """Helper function to find the maximum element recursively."""
        if node is None:
            return float('-inf')

        max_val = node.data
        left_max = self._find_max_recursive(node.left)
        right_max = self._find_max_recursive(node.right)

        return max(max_val, left_max, right_max)

# Usage
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(1)
tree.insert(4)
tree.insert(7)
tree.insert(9)

max_element = tree.find_max_element()
print("Maximum element in the tree:", max_element)  # Output: Maximum element in the tree: 9



'''Solution for Problem 2'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def calculate_height(root):
    if root is None:
        return -1  # Height of an empty tree is considered as -1

    left_height = calculate_height(root.left)
    right_height = calculate_height(root.right)

    return max(left_height, right_height) + 1

# Example usage:

# Constructing a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Calculating the height of the tree
height = calculate_height(root)
print("Height of the binary tree:", height)  # Output: Height of the binary tree: 2