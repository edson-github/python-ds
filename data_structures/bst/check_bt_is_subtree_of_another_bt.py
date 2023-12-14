class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check(root1, root2):
    if root1 is None:
        return True
    if root2 is None:
        return False
    if are_identical(root1, root2):
        return True
    return (check(root1.left, root2) or check(root1.right, root2))


def are_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (root1.val == root2.val and are_identical(root1.left, root2.left) and are_identical(root1.right, root2.right))


