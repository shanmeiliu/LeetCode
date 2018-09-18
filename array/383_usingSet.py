class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        s=ransomNote
        t=magazine
        for i in set(s):
            if s.count(i) > t.count(i):
                return False
        return True
