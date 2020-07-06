class Solution:
    def countBits(self, num):
        count={}
        arr=[]
        count[0]=0
        j=0
        arr.append(0)
        for i in range(1,num+1):
            pos=2**j
            nextPos=2**(j+1)
            if ((i+1)==nextPos):
                j += 1
            if(i==pos):
                count[i]=1
            else:
                count[i]=count[pos]+count[i-pos]
            arr.append(count[i])
        return arr




s=Solution()
print(s.countBits(0))