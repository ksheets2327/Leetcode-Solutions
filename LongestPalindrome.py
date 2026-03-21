class Solution(object):
    def longestPalindrome(self, s):
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        longest = 0
        hasOdd = False

        for count in counts.values():
            longest += count // 2 * 2
            if count % 2 == 1:
                hasOdd = True
        
        if hasOdd:
            longest += 1

        return longest
        
