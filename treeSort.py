# Import the binarytree library
from binarytree import build, Node

# Class containing left and right child of the current node and key value
class TreeNode:
    def __init__(self, item=0):
        self.key = item
        self.left, self.right = None, None

# Root of BST
root = None

# This method mainly calls insertRec()
def insert(key):
    global root
    root = insertRec(root, key)
    # Print the binary tree representation after each insertion
    print("Binary Tree Representation:")
    binary_tree = build_binary_tree(root)
    print(binary_tree)

# A recursive function to insert a new key in BST
def insertRec(root, key):
    # If the tree is empty, return a new node
    if root is None:
        root = TreeNode(key)
        return root

    # Otherwise, recur down the tree
    if key < root.key:
        root.left = insertRec(root.left, key)
    elif key > root.key:
        root.right = insertRec(root.right, key)

    return root

# A function to do inorder traversal of BST
def inorderRec(root):
    if root is not None:
        inorderRec(root.left)
        print(root.key, end=" ")
        inorderRec(root.right)

# Function to build a binary tree from a given root node
def build_binary_tree(root):
    if root is None:
        return None
    return Node(root.key, build_binary_tree(root.left), build_binary_tree(root.right))

def treeSortMain(arr):
    print("================ Tree Sort ==================\n")
    for num in arr:
        insert(num)

    print("Inorder traversal of the BST after insertion:")
    inorderRec(root)

if __name__ == '__main__':
    # Driver Code
    user_input = input("Enter numbers separated by spaces to insert into the BST (e.g., 5 4 7 2 11): ")
    arr = [int(num) for num in user_input.split()]
    for num in arr:
        insert(num)

    print("Inorder traversal of the BST after insertion:")
    inorderRec(root)
