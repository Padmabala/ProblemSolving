class Solution:
    def bSearch(self,nums,low,high,target):
        if(low>high):
            return low
        if(low>=high):
            if(low>len(nums)-1):
                return low
            elif(high<0):
                return 0
            elif():
                return low
        mid=(low+high)//2
        if(nums[mid]==target):
            return mid
        elif(nums[mid]>target):
            index=mid-1
            return self.bSearch(nums,low,mid-1,target)
        else:
            return self.bSearch(nums,mid+1,high,target)
    def searchInsert(self, nums,target):
        return self.bSearch(nums,0,len(nums)-1,target)
s=Solution()
print(s.searchInsert([1],0))