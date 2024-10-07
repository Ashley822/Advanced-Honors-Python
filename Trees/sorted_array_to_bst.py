class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: list) -> TreeNode:
    """
    Parameters:
    - nums (list): A sorted list of integers.

    Returns:
    - TreeNode: The root of the resulting BST.
    """
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])

    return root


def inorderTraversal(root: TreeNode) -> list:
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
    traverse(root)
    return result

if __name__ == "__main__":
    nums = [-15, -10, -3, 0, 5, 9, 12, 20]
    bst_root = sortedArrayToBST(nums)

    result = inorderTraversal(bst_root)
    print("BST from Sorted Array In-order Traversal:", result)
    

