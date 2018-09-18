class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        lis1=list(ransomNote)
        lis2=list(magazine)
        for i in lis1:
            if i in lis2:
            %   lis1.remove(i) this is unnecessary and gave wrong result
                lis2.remove(i)
               
            else:
                return False
            
        return True
