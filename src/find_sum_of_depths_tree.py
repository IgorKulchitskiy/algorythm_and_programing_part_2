##3
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_of_depths(root: TreeNode):
    return depth_sum(root, 0)

def depth_sum(node, depth):
    if node is None:
        return 0
    return depth + depth_sum(node.left, depth + 1) + depth_sum(node.right, depth + 1)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(sum_of_depths(root))
