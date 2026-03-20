class Solution(object):
    def letterCombinations(self, digits):
        digit_to_letters = [
            "abc",   # 2
            "def",   # 3
            "ghi",   # 4
            "jkl",   # 5
            "mno",   # 6
            "pqrs",  # 7
            "tuv",   # 8
            "wxyz"   # 9
        ]
        result = [""]

        for digit in digits:
            letters = digit_to_letters[int(digit) - 2]
            result = [existing + letter for existing in result for letter in letters]
        return result

         


        
