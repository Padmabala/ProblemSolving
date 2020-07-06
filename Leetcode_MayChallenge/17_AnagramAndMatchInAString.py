class Solution:
    def findAnagrams(self, s: str, p: str):
        indices = []
        flag = 0
        l = list(p)
        psum = 0
        for i in p:
            psum += ord(i)
        q = list(s)
        i = 0
        j = 0
        k = 0
        startIndex = 0
        sum = 0
        count=0
        windowSize=0
        while (q):
            if(len(q)<len(p)):
                break
            if (j < len(q) and q[j] in p):
                sum += ord(q[j])
                if (flag == 0):
                    startIndex = k
                    flag = 1
                windowSize+=1
            else:
                if q[j] not in p:
                    sum = 0
                    q = q[j+1:]
                    k = i+1
                    j = -1
                    flag=0
                    windowSize=0


            if (sum == psum):
                indices.append(startIndex)
                sum-=ord(q[0])
                q.pop(0)
                flag = 0
                if(count==0):
                    count=1
                k+=1
                windowSize-=1
            elif(windowSize==len(p)):
                sum -= ord(q[0])
                q.pop(0)
                flag = 0
                k += 1
                windowSize -= 1
            else:
                j+=1
            i+=1
        return indices


s = Solution()
print(s.findAnagrams("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaa"))

# class Solution:
#     def partition(self,s,low,high):
#         pivot=s[high]
#         i=low-1
#         for j in range(low,high):
#             if(s[j]<pivot):
#                 i+=1
#                 s[i],s[j]=s[j],s[i]
#         s[i + 1], s[high] = s[high], s[i + 1]
#         return i+1
#
#     def qsort(self,s,low,high):
#         if(low<high):
#             part=self.partition(s,low,high)
#             self.qsort(s,low,part-1)
#             self.qsort(s,part+1,high)
#
#     def findAnagrams(self, s: str, p: str):
#         print(s)
#         print(p)
#         count=0
#         indices=[]
#         flag=0
#         l=list(p)
#         self.qsort(l,0,len(l)-1)
#         sortedP=("").join(l)
#         q=list(s)
#         i=0
#         j=0
#         while(q):
#             if(j<len(q) and q[j] in p):
#                 count+=1
#                 if(flag==0):
#                     startIndex=i
#                     flag=1
#             else:
#                 count=0
#                 flag = 0
#                 j = 0
#                 i += 1
#                 q.pop(0)
#                 startIndex=-1
#                 continue
#             if(count==len(p) and startIndex!=-1):
#                 newS=s[startIndex:startIndex+len(p)]
#                 l = list(newS)
#                 self.qsort(l,0,len(l)-1)
#                 sortedS=("").join(l)
#                 if(sortedP==sortedS):
#                     indices.append(startIndex)
#                 count=0
#                 flag=0
#                 q.pop(0)
#                 j=0
#                 i+=1
#             else:
#                 j+=1
#         return indices