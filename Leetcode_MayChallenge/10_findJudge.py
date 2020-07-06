class Solution:
    def findJudge(self, N: int, trust) -> int:
        hash={}
        maxSupport={}
        max=-1
        element=-1
        for i in range(len(trust)):
            if(trust[i][0]>N or trust[i][1]>N):
                return -1
            hash[trust[i][0]]=1
            if(trust[i][1] not in maxSupport):
                maxSupport[trust[i][1]]=1
            else:
                maxSupport[trust[i][1]]=maxSupport[trust[i][1]]+1
            if(maxSupport[trust[i][1]]>=max):
                max=maxSupport[trust[i][1]]
                element=trust[i][1]
                # hash[trust[i][1]] = 0
        if (len(trust) == 0):
            return 1
        elif (element in hash):
            return -1
        else:
            if(maxSupport[element]==N-1):
                return element
            else:
                return -1
s=Solution()
print(s.findJudge(11,[[1, 8], [1, 3], [2, 8], [2, 3], [4, 8], [4, 3], [5, 8], [5, 3], [6, 8], [6, 3], [7, 8], [7, 3], [9, 8], [9, 3], [11, 8], [11, 3],[10,3],[8,3]]))