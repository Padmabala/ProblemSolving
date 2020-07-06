class CountIndex:
    def __init__(self):
        self.count=0;
        self.index=-1;
class Solution:
    def getCountIndexObj(self):
        countIndexObj=CountIndex()
        return countIndexObj
    def firstUniqChar(self, s: str) -> int:
        firstUniqueChar=float('inf')
        hash={}
        l=list(s)
        i=0
        for i in range(len(list(s))):
            if(l[i] not in hash):
                countIndexArray = self.getCountIndexObj()
                countIndexArray.count=1
                countIndexArray.index=i
                hash[l[i]]=countIndexArray
            else:
                hash[l[i]].count += 1
        uniqueChars=list(hash.keys())
        for i in range(len(uniqueChars)):
            if(hash[uniqueChars[i]].count==1):
                firstUniqueChar=min(firstUniqueChar,hash[uniqueChars[i]].index)
        if(firstUniqueChar==float('inf')):
            return -1
        return firstUniqueChar
s=Solution()
print(s.firstUniqChar("dddczcdbbaa"))

# above code 32ms
# Below code 56 ms

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         hash={[] for i in range(len(s))}
#         l=list(s)
#         i=0
#         for i in range(len(list(s))):
#             if(l[i] not in hash):
#                 hash[l[i]]=1
#             else:
#                 hash[l[i]]+=1
#
#         for i in range(len(l)):
#             if(hash[l[i]]==1):
#                 return l.index(l[i])
#         return -1
# s=Solution()
# print(s.firstUniqChar("dddccdbba"))