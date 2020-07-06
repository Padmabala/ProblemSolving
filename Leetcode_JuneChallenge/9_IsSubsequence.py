class Solution:
    def isSubsequence(self, s, t):
        h = {}
        for index, i in enumerate(list(t)):
            if i not in h:
                h[i] = [index]
            else:
                h[i].append((index))
        prev =-1
        flag=True
        ls=list(s)
        for i in range(len(ls)):
            if ls[i] in h:
                print(h[ls[i]],len(h[ls[i]]))
                if(h[ls[i]]):
                    for j in range(len(h[ls[i]])):
                        ele = h[ls[i]][j]
                        if (ele <= prev):
                            flag = False
                        else:
                            flag = True
                            break
                    if (flag == False):
                        break;
                    else:
                        prev = h[ls[i]][j]
                        h[ls[i]].pop(0)
                else:
                    flag=False
                    break
            else:
                flag=False
                break
        return flag
s=Solution()
print(s.isSubsequence("aaaaaa","bbaaaa"))


# class Solution:
#     def isSubsequence(self, s, t):
#         h = {}
#         for index, i in enumerate(list(t)):
#             if i not in h:
#                 h[i] = index
#         prev = -1
#         k=[]
#
#         for i in range(len(s)):
#             prev=-1
#             flag = True
#             ls=list(s[i])
#             for i in range(len(ls)):
#                 if ls[i] in h:
#                     if (h[ls[i]] <= prev):
#                         flag=False
#                         break
#                     else:
#                         prev = h[ls[i]]
#                 else:
#                     return False
#             k.append(flag)
#         return k
# s=Solution()
# print(s.isSubsequence("axc","ahbgdc"))
