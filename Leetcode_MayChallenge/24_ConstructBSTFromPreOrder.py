# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.root = None

    def bstFromPreorder(self, preorder):
        for i in preorder:
            newNode = TreeNode(i)
            if self.root is None:
                self.root = newNode
            else:
                temp = self.root
                while (temp != None):
                    prev = temp
                    if (i < temp.val):
                        temp = temp.left
                    else:
                        temp = temp.right
                if (i < prev.val):
                    prev.left = newNode
                else:
                    prev.right = newNode
        return self.root
s=Solution()
print(s.bstFromPreorder([8,5,1,7,10,12]))

