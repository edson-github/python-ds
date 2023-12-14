class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_spiral(root):

    s2 = []

    s1 = [root]
    while s1 or s2:

        while s1:
            temp = s1.pop()
            print(temp.data, end=' ')

            if temp.right:
                s2.append(temp.right)
            if temp.left:
                s2.append(temp.left)

        while s2:
            temp = s2.pop()
            print(temp.data, end=' ')

            if temp.left:
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)
