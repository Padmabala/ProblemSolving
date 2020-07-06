class Node:
    def __init__(self,val):
        self.lNode=None
        self.rNode=None
        self.val=val
class Solution:
    def __init__(self):
        self.root=None
        self.s=[]
    def insert(self,l):
        newNode=Node(l)
        if self.root is None:
            self.root=newNode
        else:
            temp=self.root
            while(temp is not None):
                prev=temp
                if(l[1]<=temp.val[1]):
                    temp=temp.lNode
                else:
                    temp=temp.rNode
            if(l[1]<=prev.val[1]):
                prev.lNode=newNode
            else:
                prev.rNode=newNode
    def traverse(self,temp):
        if temp is None:
            return
        self.traverse(temp.rNode)
        for i in range(temp.val[1]):
            self.s.append((temp.val[0]))
            # print(temp.val[0],end='')
        self.traverse(temp.lNode)
    def frequencySort(self,s):
        hash={}
        for i in s:
            if(i not in hash):
                hash[i]=1
            else:
                hash[i]+=1
        for i in hash:
            self.insert([i,hash[i]])
        self.traverse(self.root)
        v=""
        return v.join(self.s)
s=Solution()
print(s.frequencySort("tree"))
