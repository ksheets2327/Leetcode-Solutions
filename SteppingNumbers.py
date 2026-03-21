class Solution(object):
    def countSteppingNumbers(self, low, high):
        ans = []
        q =deque(range(10))
        
        while q:
            num = q.popleft()
            if low <= num <= high: 
                ans += [num]
            if num > high:
                return ans
            last_digit = num % 10
            if num == 0: 
                continue
            for new in [last_digit - 1, last_digit + 1]:
                if 0 <= new <= 9:
                    q.append(num * 10 + new)


        
