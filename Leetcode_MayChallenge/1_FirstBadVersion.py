# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def isBadVersion(self,number):
        check=[False]
        return check[number]
    def findBad(self,l,h):
        if(l>h):
            return l
        else:
            # if(self.isBadVersion(h)==False):
            #     return h + 1
            middle=int((l+h)//2)
            isBad=self.isBadVersion(middle)
            if(isBad==True):
                return self.findBad(l,middle-1)
            elif(isBad==False):
                return self.findBad(middle+1,h)
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        badVersionIndex=self.findBad(0,n-1)
        if(badVersionIndex>n):
            return -1
        else:
            return badVersionIndex

s=Solution();
print(s.firstBadVersion(1))
