class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic={}
        for i in nums:
            if i in dic:
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        lis=sorted(dic.items(), key=lambda x: x[1])
        print(lis)
        return [i[0] for i in lis[-k:]]
