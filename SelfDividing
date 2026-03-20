class Solution(object):
    def selfDividingNumbers(self, left, right):
        def isSelfDividing(n):
            temp = n
            while temp > 0:
                digit = temp % 10
                if digit == 0 or n % digit != 0:
                    return False
                temp = temp // 10
            return True
        
        return [i for i in range(left, right+1, 1) if isSelfDividing(i)]
                    
        
