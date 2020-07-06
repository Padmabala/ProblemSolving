class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        d1 = {}
        for l in s1:
            if l in d1:
                d1[l] += 1
            else:
                d1[l] = 1

        d2 = {}
        for l in s2[:len(s1)]:
            if l in d2:
                d2[l] += 1
            else:
                d2[l] = 1

        if d1 == d2:
            return True
        print(len(s2) - len(s1))
        for i in range(len(s2) - len(s1)):
            v_out = s2[i]
            if d2[v_out] == 1:
                del d2[v_out]
            else:
                d2[v_out] -= 1

            v_in = s2[i + len(s1)]
            if v_in in d2:
                d2[v_in] += 1
            else:
                d2[v_in] = 1
            if d1 == d2:
                return True

        return False

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         psum=0
#         so=sorted(s1)
#         for i in s1:
#             psum += ord(i)
#         q = list(s2)
#         j = 0
#         sum = 0
#         windowSize = 0
#         while (q):
#             if (len(q) < len(s1)):
#                 break
#             if (q[j] in s1):
#                 sum += ord(q[j])
#                 windowSize += 1
#             else:
#                 sum = 0
#                 q = q[j + 1:]
#                 j = -1
#                 windowSize = 0
#
#             if (sum == psum and windowSize==len(s1)):
#                 if((sorted(q[0:j+1]))==so):
#                     return True
#             if (windowSize == len(s1)):
#                 sum -= ord(q[0])
#                 q.pop(0)
#                 windowSize -= 1
#             else:
#                 j += 1
#         return False
s = Solution()
print(s.checkInclusion("abc", "cccbbbaaa"))