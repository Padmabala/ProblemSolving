# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.l = 0

    def isSibling(self, root, x, y):
        if (root.left is None or root.right is None):
            return 0
        return ((root.left.val == x and root.right.val == y) or
                (root.left.val == y and root.right.val == x) or
                self.isSibling(root.left, x, y) or
                self.isSibling(root.right, x, y))

    def level(self, root, ptr, level):

        if root is None:
            return 0
        if root.val == ptr:
            return level
        if (root.left is not None):
            self.l = self.level(root.left, ptr, level + 1)
        if (self.l > 0):
            return self.l
        if (root.right is not None):
            return self.level(root.right, ptr, level + 1)

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        print(root)
        l1 = self.level(root, x, 0)
        l2 = self.level(root, y, 0)
        s1 = self.isSibling(root, x, y)
        print(l1, l2, s1)
        if ((l1 > 0) and (l2 > 0) and (l1 == l2) and not (s1)):
            return True
        else:
            return False
