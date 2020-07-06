class Solution:
    def intervalIntersection(self, A,B):
        i=0
        j=0
        ans=[]
        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
            # if
            # if(i>0):
            #     l=max(A[i-1][1],B[j-1][1])
            #     if(i==len(A)):
            #         r=B[j][0]
            #         if (l == r):
            #             ans.append([l, r])
            #         break
            #     elif(j==len(B)):
            #         r=A[i][0]
            #         if (l == r):
            #             ans.append([l, r])
            #         break
            #     else:
            #         r=min(A[i][0],B[j][0])
            #         if (l == r):
            #             ans.append([l, r])
            #
            # l=max(A[i][0],B[j][0])
            # r=min(A[i][1],B[j][1])
            # if l<=r:
            #     ans.append([l,r])
            # if (i == len(A) - 1 and j == len(B) - 1):
            #     i += 1
            #     j += 1
            #     break
            # if(i<len(A)-1):
            #     if(B[j][1] >= A[i][1] or j==len(B)-1):
            #         i+=1
            # if(j<len(B)-1):
            #     if (B[j][1]<A[i][1] or i == len(A) - 1):
            #         j+=1
        # return ans
s=Solution()
print(s.intervalIntersection([[0,2],[5,10],[13,23],[24,25]],
[[1,5],[8,12],[15,24],[25,26]]))