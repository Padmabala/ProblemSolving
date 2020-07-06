# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.root=None
    def insert(self,element):
        newNode=TreeNode(element)
        if(self.root==None):
            self.root=newNode
        else:
            temp=self.root
            while(temp!=None):
                prev=temp
                if(element<temp.val):
                    temp=temp.left
                else:
                    temp=temp.right
            if(element<prev.val):
                prev.left=newNode
            else:
                prev.right=newNode
    def traverse(self,root):

        if(root==None):
            return
        self.traverse(root.left)
        if(self.k>0):
            self.k-=1
        if(self.k==0 and not(self.found)):
            self.ele=root.val
            self.found=True
        self.traverse(root.right)

    def kthSmallest(self, k: int) -> int:
        self.k = k
        self.ele=0
        self.found=False
        self.traverse(self.root)
        return self.ele


s=Solution()
s.insert(8)
s.insert(4)
s.insert(2)
s.insert(0)
s.insert(1)
s.insert(3)
s.insert(9)
print(s.kthSmallest(1))
