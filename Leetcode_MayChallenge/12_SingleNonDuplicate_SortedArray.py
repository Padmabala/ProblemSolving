class Solution:
    def singleNonDuplicate(self, nums) :
        high = len(nums) - 1
        low = 0
        while True:
            mid = int((low + high) / 2)
            if (mid % 2 == 1):
                mid -= 1
            if mid < high and nums[mid] == nums[mid + 1]:
                low = mid + 2
            elif mid > low and nums[mid] == nums[mid - 1]:
                high = mid - 2
            else:
                return nums[mid]
        # return self.findDuplicate(nums,0,n-1)
    # def findDuplicate(self,nums,start,end):
    #     mid = int((start + end) / 2)
    #     if(start==end):
    #         return nums[mid]
    #     # print(nums[mid])
    #     # c1=nums[mid-1]<nums[mid]
    #     # c2=((((mid-1)-start)+1)%2!=0)
    #     # c3=nums[mid]==nums[mid-1]
    #     # c4=((((mid-1)-start)+1)%2==0)
    #     # print(c1,c2,c3,c4)
    #     # c5=nums[mid+1]>nums[mid]
    #     # c6=(((end-(mid+1))+1)%2!=0)
    #     # c7=nums[mid]==nums[mid+1]
    #     # c8=(((end-(mid+1))+1)%2==0)
    #     # print(c5,c6,c7,c8)
    #
    #     if(nums[mid-1]<nums[mid] and ((((mid-1)-start)+1)%2!=0)):
    #         return self.findDuplicate(nums,start,mid-1)
    #     elif(nums[mid]==nums[mid-1] and ((((mid-1)-start)+1)%2==0)):
    #         return self.findDuplicate(nums, start, mid - 2)
    #     elif(nums[mid+1]>nums[mid] and (((end-(mid+1))+1)%2!=0)):
    #         return self.findDuplicate(nums,mid+1,end)
    #     elif(nums[mid]==nums[mid+1] and (((end-(mid+1))+1)%2==0)):
    #         return self.findDuplicate(nums,mid+2,end)
    #     else:
    #         return self.findDuplicate(nums, mid , mid)

s=Solution()
print(s.singleNonDuplicate([1,1,2,2,3,3,4,8,8]))

# print(s.singleNonDuplicate([1,1,2,2,3,3,4,8,8,9,9,8,8,9,9,8,8,9,9,8,8,9,9,
#                             8,8,9,9,8,8,9,9,8,8,9,9,8,8,9,9,8,8,9,9,8,8,9,9,8,8,9,9,8,8,9,9,8,8,9,9,8,8,9,9,8,8,9,9,8,8,9,9,10,10]))
# class Solution:
#     def singleNonDuplicate(self, nums) :
#         b = 0
#         for i in range(len(nums)):
#             b=b^nums[i]
#         return b

