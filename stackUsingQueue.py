class MyStack(object):

    def __init__(self):
        self.q = deque()
        self.topIndex = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        self.topIndex = len(self.q) - 1
        

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return 0
        q2 = deque()
        index = 0
        while index != self.topIndex:
            q2.append(self.q.popleft())
            index = index + 1

        val = self.q.popleft()
        self.q = q2

        self.topIndex = len(self.q) - 1       
        return val
        

    def top(self):
        """
        :rtype: int
        """
        if self.empty():
            return 0
        q2 = deque()
        index = 0
        while index != self.topIndex:
            q2.append(self.q.popleft())
            index = index + 1

        val = self.q.popleft()
        q2.append(val)
        self.q = q2

        self.topIndex = len(self.q) - 1       
                
        return val
        

    def empty(self):
        """
        :rtype: bool
        """
        return False if self.q else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
