# Assessment 3.6: DFS Method in Tree
# Last Name: SUERTE
# Traversal: Depth-First Search (DFS), Preorder, Left to Right

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs_preorder(root):
    if root is None:
        return

    print(root.value, end=" ")
    dfs_preorder(root.left)
    dfs_preorder(root.right)


# Create the SUERTE binary tree from Assessment 3.5.
root = Node("S")
root.left = Node("U")
root.right = Node("E1")
root.left.left = Node("R")
root.left.right = Node("T")
root.right.left = Node("E2")

print("DFS Traversal of SUERTE Binary Tree:")
dfs_preorder(root)
print()
