class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1 or n == 0:
            return 
        i,j =0,0
        k = n-1
        while j <= k :
            if nums[j] == 1:
                j+=1
                            
            else:
                if nums[j] == 2:
                    temp=nums[j]
                    nums[j]=nums[k]
                    nums[k]=temp
                    k-=1
                else:
                    if nums[j] == 0:
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
                        i+=1
                        j+=1

