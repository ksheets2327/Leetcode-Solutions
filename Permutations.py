class Solution(object):
    def permute(self, nums):
        result = []
        current_permutation = []
        used = set()

        def backtrack():
            if len(current_permutation) == len(nums):
                result.append(current_permutation[:])
                return
            
            for num in nums:
                if num not in used:
                    used.add(num)
                    current_permutation.append(num)

                    backtrack()

                    current_permutation.pop()
                    used.remove(num)

        backtrack()

        return result
            

        
