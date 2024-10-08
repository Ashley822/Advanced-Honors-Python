class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height is initially 1 when the node is inserted


class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, z):
        # Implement Right Rotation logic
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def left_rotate(self, z):
        # Implement Left Rotation logic
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, root, key):
        # Implement AVL Insert logic with balancing

        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def pre_order(self, root):
        # Implement AVL Delete logic with balancing
        if root:
            print(f"{root.key} ", end="")
            self.pre_order(root.left)
            self.pre_order(root.right)


# Test
if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None

    nodes = [10, 20, 30, 40, 50, 60, 70]
    for node in nodes:
        root = avl_tree.insert(root, node)

    print("Pre-order traversal after inserting nodes:")
    avl_tree.pre_order(root)

    print("\nHeight of the AVL tree:", avl_tree.get_height(root))
