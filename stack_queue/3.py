class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        maxsub=[]
        temp=[]
       
        temp.append(s[0])
        n=len(s)
        if n == 1:
            return 1
        for j in range(1, n):
            if s[j] not in temp:
                temp.append(s[j])

            else:

                while s[j] in temp:
                    temp.pop(0)
                temp.append(s[j])
            if len(maxsub)<len(temp):
                maxsub=temp[:]
        return len(maxsub)
                
            
        
