class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop() if self.s1 else None
        

    def peek(self):
        return (self.s1[-1]) if self.s1 else None
        

    def empty(self):
        return len(self.s1) == 0
    
q = MyQueue()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()