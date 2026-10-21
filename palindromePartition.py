class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        results = []
        part = []
        def validPal(strin):
            rev = strin[::-1]
            if strin == rev:
                return True
            return False

        
        def dfs(index):
            if index >= len(s):
                results.append(part[:])
                return
            for i in range(index, len(s)):
                if validPal(s[index:i+1]):
                    part.append(s[index:i+1])
                    dfs(i+1)
                    part.pop()
        
        dfs(0)
        return results
