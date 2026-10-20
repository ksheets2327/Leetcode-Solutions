class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        current_permutation = []
        occurences = {}
        for num in nums:
            occurences[num] = nums.count(num)


        def backtrack():
            if (len(current_permutation) == len(nums) and current_permutation not in result):
                result.append(current_permutation[:])
                return
            for num in occurences:
                if (occurences[num] > 0):
                    occurences[num] -= 1
                    current_permutation.append(num)

                    backtrack()

                    current_permutation.pop()
                    occurences[num] += 1
                
        
        backtrack()

        return result
