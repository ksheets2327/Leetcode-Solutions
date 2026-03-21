class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        
        if s[0] == '-':
            sign = -1
        else:
            sign = 1
        if s[0] in {'-', '+'}:
            s = s[1:]
        
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        for c in s:
            if not c.isdigit():
                break
            digit = int(c)

            if (result > INT_MAX // 10) or (result == INT_MAX  // 10 and digit > 7):
                if sign == -1:
                    return INT_MIN
                else:
                    return INT_MAX

            result = result * 10 + digit
        
        return sign * result


        
