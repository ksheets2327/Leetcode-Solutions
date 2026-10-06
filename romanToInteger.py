class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        num = 0
        dic = {"I":1, "V":5, "X":10, "L":50, "C": 100, "D":500, "M":1000}

        for i in range(len(s)):
            if i == len(s) - 1: # last letter
                num = num + dic[s[i]]
                break
           # if the letter has a smaller value than the next letter, its being subtracted
            if dic[s[i]] < dic[s[i + 1]]:
                num = num - dic[s[i]]
            else:
                num = num + dic[s[i]]

        return num

