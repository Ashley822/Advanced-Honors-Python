from autocomplete_system import AVLTree

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
