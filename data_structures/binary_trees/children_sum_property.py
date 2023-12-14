# Check whether a tree statisfies children sum property
# Children sum property is such that every partent = left + right child

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum_prop(root):
    l = r = 0

    if not root or not root.left and not root.right:
        return True

    if root.left:
        l = root.left.val

    if root.right:
        r = root.right.val

    return bool(
        (root.val == l + r) and sum_prop(root.left) and sum_prop(root.right)
    )
