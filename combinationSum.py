class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        path = []

        def back():
            if sum(path) == target and sorted(path) not in result:
                result.append(sorted(path))
                return
            for num in candidates:
                if sum(path) + num <= target:
                    path.append(num)
                    back()
                    path.pop()

        back()
        return result
