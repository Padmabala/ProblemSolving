class Solution:
    # Python program for maximum contiguous circular sum problem

    # Standard Kadane's algorithm to find maximum subarray sum
    def kadane(self,a):
        n = len(a)
        max_so_far = float('-inf')
        max_ending_here = float('-inf')
        for i in range(0, n):
            max_ending_here = max_ending_here + a[i]
            if (max_ending_here < a[i]):
                max_ending_here = a[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
        return max_so_far

        # The function returns maximum circular contiguous sum in

    # a[]
    def maxSubarraySumCircular(self, A):

        n = len(A)
        hash={}
        if(n==1):
            return A[0]
        # Case 1: get the maximum sum using standard kadane's
        # algorithm
        max_kadane = self.kadane(A)

        # Case 2: Now find the maximum sum that includes corner
        # elements.
        max_wrap = 0
        for i in range(0, n):
            max_wrap += A[i]
            if(A[i] not in hash):
                hash[A[i]]=1
            else:
                hash[A[i]]+=1
            A[i] = -A[i]


            # Max sum with corner elements will be:
        # array-sum - (-max subarray sum of inverted array)
        max_wrap = max_wrap + self.kadane(A)

        # The maximum circular sum will be maximum of two sums
        if(len(hash)==1 and 0 in hash):
            return 0
        if max_wrap == 0:
            max_wrap=float('-inf')
        if max_kadane == 0:
            max_kadane=float('-inf')
        if(max_wrap==float('-inf') and max_kadane==float('-inf')):
            return -1
        if max_wrap > max_kadane:
            return max_wrap
        else:
            return max_kadane
s=Solution()
print(s.maxSubarraySumCircular([0,0,0,0,0]))


     # works but takes a lot of time
        # for i in range(len(A)):
        #     count=0
        #     j=i
        #     if(j in hash):
        #         continue
        #     maxEndingHere=0
        #     while(count!=len(A)):
        #         sum=maxEndingHere+A[j]
        #         if(sum>=A[j]):
        #             maxEndingHere=sum
        #         else:
        #             maxEndingHere=A[j]
        #             if j not in hash:
        #                 hash[j]=1
        #         if (maxEndingHere > maxAcross):
        #             maxAcross = maxEndingHere
        #         count+=1
        #         j+=1
        #         j=j%len(A)
        # return maxAcross

        # while(i<len(A)):
        #     if i not in hash:
        #         hash[i]=1
        #     elif hash[i]==2:
        #         break
        #     else:
        #         hash[i] += 1
        #     sum=maxEndingHere+A[i]
        #     if(sum>A[i]):
        #         maxEndingHere=sum
        #     else:
        #         maxEndingHere=A[i]
        #     if(maxEndingHere>maxAcross):
        #         maxAcross=maxEndingHere
        #     if((i+1)==len(A)):
        #         maxEndingHere=A[i]
        #         hash[i] += 1
        #         i=(i+1)%len(A)
        #
        #     else:
        #         i+=1
        # return maxAcross
# s=Solution()
# print(s.maxSubarraySumCircular([7,9,-8,3,-5]))

