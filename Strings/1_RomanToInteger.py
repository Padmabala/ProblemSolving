class Solution:
    def romanToInt(self, s):
        romanHash={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l=list(s)
        sum=0
        for i in range(len(l)):
            if(l[i] in romanHash):
                ex = romanHash[l[i]]
                if (i > 0):
                    if (romanHash[l[i - 1]] < romanHash[l[i]]):
                        ex = romanHash[l[i]] - romanHash[l[i - 1]]
                        sum = sum - romanHash[l[i - 1]]
                sum += ex
            else:
                return 'Invalid input'
        return sum
s=Solution()
print(s.romanToInt("CM"))
