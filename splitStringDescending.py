class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def back(index, prev):
            if (index == len(s)):
                return True
            for j in range(index, len(s)):
                val = int(s[index:j+1])
                
                if (val == prev - 1 and back(j + 1, val)):
                    return True
            return False

        
        for i in range(len(s) - 1):
            val = s[:i + 1]
            if back(i+1, int(val)):
                return True
        return False   
