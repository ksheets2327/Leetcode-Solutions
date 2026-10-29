class MinStack:
    def __init__(self):
        self.s, self.st = [], []


    def push(self, val):
        self.s.append(val)
        if not self.st or val <= self.st[-1]:
            self.st.append(val)


    def pop(self):
        if self.s.pop() == self.st[-1]: 
            self.st.pop()

    def top(self):
        return self.s[-1]


    def getMin(self):
        return self.st[-1]
