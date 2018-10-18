class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers)-1
        while i<j:
            temp=numbers[i]+numbers[j]
            if temp==target:
                return [i+1, j+1]
            else:
                if temp>target:
                    j=j-1
                else:
                    i=i+1
