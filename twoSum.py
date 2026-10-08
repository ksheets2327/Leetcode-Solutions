class Solution(object):
    # Brute Force
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        
        for i in range(n):
            for j in range(n):
                if (i == j):
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]

# Hash Map
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index
                
        
