class CountMajor:
    def __init__(self):
        self.count=0
        self.element=-1
class Solution:
    def majorityElement(self, nums) -> int:
        major=int(len(nums)/2)
        ele=-1
        hash={}
        for i in range(len(nums)):
            if(nums[i] not in hash):
                hash[nums[i]]=1
            else:
                hash[nums[i]]+=1
            if(major<hash[nums[i]]):
                major=hash[nums[i]]
                ele=nums[i]
        return ele

s=Solution()
print(s.majorityElement([2]))