class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert_recursive(node, key):
            if node is None:
                return Node(key)
            if key < node.key:
                node.left = _insert_recursive(node.left, key)
            elif key > node.key:
                node.right = _insert_recursive(node.right, key)
            return node
        
        if self.root is None:
            self.root = Node(key)
        else:
            self.root = _insert_recursive(self.root, key)

    def delete(self, key):
        def _min_value_node(node):
            current = node
            while current.left is not None:
                current = current.left
            return current
        
        def _delete_recursive(node, key):
            if node is None:
                return node
            if key < node.key:
                node.left = _delete_recursive(node.left, key)
            elif key > node.key:
                node.right = _delete_recursive(node.right, key)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                
                temp = _min_value_node(node.right)
                node.key = temp.key
                node.right = _delete_recursive(node.right, temp.key)
            return node
        
        self.root = _delete_recursive(self.root, key)
    
    def find_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key if current else None

    def find_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key if current else None

    def search(self, key):
        def _search_recursive(node, key):
            if node is None or node.key == key:
                return node
            if key < node.key:
                return _search_recursive(node.left, key)
            return _search_recursive(node.right, key)
        
        return _search_recursive(self.root, key)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("Max value:", bst.find_max())  
    print("Min value:", bst.find_min())  
    search_node = bst.search(40)
    print("Search for 40:", search_node.key if search_node else "Not found")


