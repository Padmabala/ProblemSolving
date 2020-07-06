class Solution:
    def findMaxLength(self, nums):
        hash={0:-1}
        sum=0
        maxLen=0
        for i in range(len(nums)):
            if (nums[i] == 0):
                nums[i] = -1
            sum+=nums[i]
            if(sum in hash):
                if maxLen<i-hash[sum]:
                    maxLen=i-hash[sum]
            else:
                hash[sum]=i
        return maxLen
s=Solution()
print(s.findMaxLength([0,1,0]))