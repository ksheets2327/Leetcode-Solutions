class Solution(object):
    def isAdditiveNumber(self, num):
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                s1 = num[:i]
                s2 = num[i:j]
                
                if ((len(s1) > 1 and s1[0] == '0') or 
                   (len(s2) > 1 and s2[0] == '0')):
                   continue
                
                num1, num2 = int(s1), int(s2)

                if self.isValid(num[j:], num1, num2):
                    return True
        return False

    
    def isValid(self, remaining, n1, n2):
        if not remaining:
            return True
        
        target = n1 + n2
        target_str = str(target)

        if not remaining.startswith(target_str):
            return False

        return self.isValid(remaining[len(target_str):], n2, target)
        
