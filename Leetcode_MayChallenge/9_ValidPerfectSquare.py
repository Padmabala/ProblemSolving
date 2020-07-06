class Solution:
    def checkPerfectSqaure(self,start,num,order):
        sq=start*start
        while (sq>=num):
            if (sq == num):
                print(start)
                return True
            else:
                if(order==1):
                    start+=1
                else:
                    start-=1
                sq = start * start
        return False
    def isPerfectSquare(self, num: int) -> bool:
        div=int(num/2)
        sq = div * div
        while(sq>=num):
            div=int(div/2)
            sq=div*div
        v1=num-(div*div)
        v2=num-((div*2)*div)
        if(v1<v2):
            return self.checkPerfectSqaure(div,num,1)
        else:
            return self.checkPerfectSqaure(div*2,num,0)


# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         i = 1
#         sq = 1
#         while (sq <= num):
#             if (sq == num):
#                 print(i)
#                 return True
#             else:
#                 i += 1
#                 sq = i * i
#         return False
s=Solution()
print(s.isPerfectSquare(64))
