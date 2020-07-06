class Solution:
    def mergeSort(self,arr):
        if len(arr)>1:
            mid=int(len(arr)//2)
            l=arr[:mid]
            h=arr[mid:]
            self.mergeSort(l)
            self.mergeSort(h)

            i=j=k=0;
            while i<len(l) and j<len(h):
                if(l[i]<h[j]):
                    arr[k]=l[i]
                    i+=1
                else:
                    arr[k]=h[j]
                    j+=1
                k+=1
            while(i<len(l)):
                arr[k]=l[i]
                i+=1
                k+=1
            while(j<len(h)):
                arr[k]=h[j]
                j+=1
                k+=1

    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        self.mergeSort(nums)
        return nums
s=Solution()
print(s.sortColors([2,0,2,1,1,0]))
