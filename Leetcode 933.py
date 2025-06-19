class RecentCounter(object):

    def __init__(self):
        self.counter = []
        

    def ping(self, t):
        self.counter.append(t)

        while self.counter and self.counter[0] < t - 3000:
            self.counter.pop(0)

        return len(self.counter)

#Optimizing it with Queue

from collections import deque

class RecentCounter(object):

        def __init__(self):
            self.counter = deque()
            

        def ping(self, t):
            self.counter.append(t)

            while self.counter and self.counter[0] < t - 3000:
                self.counter.popleft()

            return len(self.counter)
