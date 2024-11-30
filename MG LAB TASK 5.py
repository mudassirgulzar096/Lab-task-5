
class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __hash__(self):  
        return hash(self.value)

    def __eq__(self, other):  
        return self.value == other.value

def dfs_stack_graph(start_node):
    visited = set()
    stack = [start_node]
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            print(current_node.value, end=' ')
            visited.add(current_node)
            
            for neighbor in reversed(current_node.neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=' ')

print("DFS Traversal (Graph):")
node_a = GraphNode('A')
node_b = GraphNode('B')
node_c = GraphNode('C')
node_d = GraphNode('D')
node_e = GraphNode('E')

node_a.add_neighbor(node_b)
node_a.add_neighbor(node_c)
node_b.add_neighbor(node_d)
node_c.add_neighbor(node_e)
node_d.add_neighbor(node_a)
node_e.add_neighbor(node_b)

dfs_stack_graph(node_a)  
print("\n")


print("Tree Traversals:")
tree_root = TreeNode(1)
tree_root.left = TreeNode(2)
tree_root.right = TreeNode(3)
tree_root.left.left = TreeNode(4)
tree_root.left.right = TreeNode(5)

print("Inorder Traversal:")
inorder_traversal(tree_root)
print("\nPreorder Traversal:")
preorder_traversal(tree_root)
print("\nPostorder Traversal:")
postorder_traversal(tree_root)
print()
