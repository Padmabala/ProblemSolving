# Python program to check if two nodes in a binary
# tree are cousins

# A Binary Tree Node
class Node:

    # Constructor to create a new Binary Tree
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isSibling(root, a, b):
    # Base Case
    if root is None:
        return 0

    return ((root.left == a and root.right == b) or
            (root.left == b and root.right == a) or
            isSibling(root.left, a, b) or
            isSibling(root.right, a, b))


# Recursive function to find level of Node 'ptr' in
# a binary tree
def level(root, ptr, lev):
    # Base Case
    if root is None:
        return 0
    if root.val == ptr:
        return lev

        # Return level if Node is present in left subtree
    l = level(root.left, ptr, lev + 1)
    if l != 0:
        return l

        # Else search in right subtree
    return level(root.right, ptr, lev + 1)


# Returns 1 if a and b are cousins, otherwise 0
def isCousin(root, a, b):
    # 1. The two nodes should be on the same level in
    # the binary tree
    # The two nodes should not be siblings(means that
    # they should not have the smae parent node

    if ((level(root, a, 1) == level(root, b, 1)) and
            not (isSibling(root, a, b))):
        return 1
    else:
        return 0

    # Driver program to test above function


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(None)
# root.left.right.right = Node(15)
# root.right.left = Node(6)
# root.right.right = Node(7)
# root.right.left.right = Node(8)

node1 = root.left.left
node2 = root.right

print("Yes" if isCousin(root, node1, node2) == 1 else "No")


# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self):
#         self.val =0
#         self.left = None
#         self.right = None
#
# class Solution:
#     def __init__(self):
#         self.sameLevelElements={}
#         self.parent={}
#         self.count=0
#         self.depth=1
#         self.tree = None
#         self.minus=1
#         self.emptyNode=0
#
#     def insert(self,element):
#         newNode=TreeNode()
#         newNode.val=element
#         if(self.tree==None):
#             self.tree = newNode
#         else:
#             currentNode=self.tree
#             while(currentNode!=None):
#                 prevNode = currentNode
#                 if(element<currentNode.val):
#                     currentNode=currentNode.left
#                 elif(element>currentNode.val):
#                     currentNode=currentNode.right
#             if(prevNode.val>element):
#                 prevNode.left=newNode
#             else:
#                 prevNode.right=newNode
#         return self.tree
#     def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
#         self.levelOrderTraverse(root)
#         for i in range(1,len(self.sameLevelElements)):
#             if(x in self.sameLevelElements[i] and y in self.sameLevelElements[i]):
#                 if(self.parent[x]!=self.parent[y]):
#                     return True
#         return False
#     def levelOrderTraverse(self,node):
#         l=[]
#         l.append(node)
#         self.sameLevelElements[self.depth] = []
#         while(len(l)>0):
#             currentNode=l[0]
#             if(currentNode is not None):
#                 self.count += 1
#                 l.append(currentNode.left)
#                 if (currentNode.left is not None):
#                     self.sameLevelElements[self.depth].append(currentNode.left.val)
#                     self.parent[currentNode.left] = currentNode
#                 self.count += 1
#                 l.append(currentNode.right)
#                 if (currentNode.right is not None):
#                     self.sameLevelElements[self.depth].append(currentNode.right.val)
#                     self.parent[currentNode.right] = currentNode
#                 if (self.count == (2 ** self.depth) or self.count+self.minus == (2 ** self.depth)):
#                     self.depth += 1
#                     self.sameLevelElements[self.depth] = []
#                     if(self.emptyNodes==True):
#                         self.minus=self.minus*2
#
#                     self.count =0
#             else:
#                 self.emptyNodes==True
#
#
#             l.pop(0)
#     def inOrder(self):
#         self.inOrderTraverse(self.tree)
#     def inOrderTraverse(self,node):
#         if(node==None):
#             return
#         self.inOrderTraverse(node.left)
#         print(node.val)
#         self.inOrderTraverse(node.right)
# s=Solution()
# ch=input("Do u wanna add element to tree? y/n")
# t=None
# while(ch=='y'):
#     t=s.insert(int(input("Enter the element to add")))
#     ch = input("Do u wanna add element to tree? y/n")
# s.inOrder()
# print(s.isCousins(t,3,4))