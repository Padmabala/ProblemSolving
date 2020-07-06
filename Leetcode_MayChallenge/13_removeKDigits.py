
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack =[]
        for n in num:
            while k and stack and stack[-1 ] >n:
                stack.pop()
                k-=1
            stack.append(n)
        stack = stack[:-k] if k else stack
        return "".join(stack).lstrip('0') or "0"





# class Solution:
#     def removeKdigits(self, num, k):
#         l = list(num)
#         count = 0
#         flag = 0
#         s=''
#         if(len(num)==k or (num=="0")):
#             return '0'
#         i=0
#         while(i<len(l)):
#             if (count == k):
#                 for j in range(0,len(l)):
#                     if (l[j] == '0' and flag == 0):
#                         j += 1
#                     elif (l[j] != '0' and flag == 0):
#                         flag = 1
#                     if(flag==1):
#                         s = s+l[j]
#                 if(flag==0):
#                     return '0'
#                 else:
#                     return s
#             elif (i == len(l) - 1 and count != k):
#                 while (count != k and i>=0):
#                     if(l[i-1]>l[i]):
#                         i-=1
#                         l.pop(i)
#                     else:
#                         l.pop(i)
#                         i -= 1
#                     count+=1
#             elif(l[i]>l[i+1]):
#                 count+=1
#                 l.pop(i)
#                 i=0
#             else:
#                 i+=1
s=Solution()
print(s.removeKdigits('0',0))