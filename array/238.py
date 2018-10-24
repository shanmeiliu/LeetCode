class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[1]*len(nums)
        prod=1
        for i in range(len(nums)):
            output[i]=output[i]*prod
            prod=prod*nums[i]
        prod=1   
        for i in range(len(nums)-1, -1, -1):
            output[i]=output[i]*prod
            prod=prod*nums[i]
        return output
