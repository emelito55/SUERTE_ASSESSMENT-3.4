from collections import deque

# =========================================================
# Assessment 3.3: Non-Linear Data Structure
# Last Name: SUERTE
# =========================================================


# ---------------------------------------------------------
# PART 1: BINARY TREE
# ---------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Build the binary tree for SUERTE
#          S
#        /   \
#       U     E
#      / \   /
#     R   T E
root = Node("S")
root.left = Node("U")
root.right = Node("E")
root.left.left = Node("R")
root.left.right = Node("T")
root.right.left = Node("E")


def bfs_tree(root):
    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


def dfs_tree(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.data)       # visit the node first (preorder)
    dfs_tree(node.left, result)    # then the whole left side
    dfs_tree(node.right, result)   # then the right side
    return result


# ---------------------------------------------------------
# PART 2: GRAPH
# ---------------------------------------------------------
# Adjacency list for SUERTE (the second E is written as E')
graph = {
    "S":  ["U", "E", "R"],
    "U":  ["S", "T"],
    "E":  ["S", "E'"],
    "R":  ["S", "E'"],
    "T":  ["U"],
    "E'": ["E", "R"],
}


def bfs_graph(graph, start):
    visited = {start}
    queue = deque([start])
    result = []
    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


def dfs_graph(graph, vertex, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    visited.add(vertex)
    result.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_graph(graph, neighbor, visited, result)
    return result


# ---------------------------------------------------------
# OUTPUT
# ---------------------------------------------------------
print("=== BINARY TREE ===")
print("BFS:", " - ".join(bfs_tree(root)))
print("DFS:", " - ".join(dfs_tree(root)))

print()
print("=== GRAPH ===")
print("BFS:", " - ".join(bfs_graph(graph, "S")))
print("DFS:", " - ".join(dfs_graph(graph, "S")))
