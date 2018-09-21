class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num=nums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if j-i<0:
            return None
        return sum(self.num[i:j+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
