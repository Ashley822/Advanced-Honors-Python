class Node:
    def __init__(self, key):
        self.key = key.lower()  
        self.left = None
        self.right = None
        self.height = 1

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
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, root, key):
        if not root:
            return Node(key)

        if key.lower() < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        balance = self.get_balance(root)

        if balance > 1 and key.lower() < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key.lower() > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key.lower() > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key.lower() < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, key):
        key = key.lower()
        if not root or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def in_order(self, root):
        result = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.key)
            current = current.right
        return result

    def autocomplete(self, root, prefix):
        """
        Finds and returns all words in the AVL tree that start with the given prefix.
        """
        words = []
        self._autocomplete_check(root, prefix.lower(), words)
        words.sort()  # Sort words to ensure lexicographical order
        return words

    def _autocomplete_check(self, node, prefix, words):
        if not node:
            return

        if node.key.startswith(prefix):
            words.append(node.key)

        self._autocomplete_check(node.left, prefix, words)

        self._autocomplete_check(node.right, prefix, words)


def main():
    avl_tree = AVLTree()
    root = None

    print("Welcome to the Autocomplete System!")

    while True:
        print("\nChoose an option:")
        print("1. Insert a word")
        print("2. Search for a word")
        print("3. Autocomplete a word")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            word = input("Enter a word to insert: ")
            root = avl_tree.insert(root, word)
            print(f'Word "{word}" has been inserted.')

        elif choice == "2":
            word = input("Enter a word to search for: ")
            found = avl_tree.search(root, word)
            if found:
                print(f'Word "{word}" found in the AVL tree.')
            else:
                print(f'Word "{word}" not found.')

        elif choice == "3":
            prefix = input("Enter a prefix: ")
            suggestions = avl_tree.autocomplete(root, prefix)
            if suggestions:
                print(f'Suggestions: {suggestions}')
            else:
                print(f'No words found with prefix "{prefix}".')

        elif choice == "4":
            print("Exiting the system.")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
