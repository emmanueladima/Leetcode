from queue import Queue

class MyStack(object):

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        

    def push(self, x):
        self.q2.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
            self.q1, self.q2 = self.q2, self.q1
        

    def pop(self):
        popped = self.q1.get()

        if not self.q1.empty():
            while self.q1.qsize() > 1:
                item = self.q1.get()
                self.q2.put(item)
                self.top_element = self.q1.get()

            last = self.q1.get()
            self.q2.put(last)
            self.q1, self.q2 = self.q2, self.q1
        else:
            self.top_element = None
        return popped

    def top(self):
       return self.top_element
        

    def empty(self):
        return self.q1.empty()
        


# Other code suggested by ChatGPT

from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0