class queueWithStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enque(self, val):
        while self.s1:
            self.s2.append(self.s1.pop())

        self.s1.append(val)

        while self.s2:
            self.s1.append(self.s2.pop())


    def deque(self):
        if not self.s1:
            return "queue is empty"
        return self.s1.pop()

    def is_empty(self):
        return len(self.s1) == 0
    
    def peek(self):
        return self.s1[-1] if self.s1 else "queue is empty"

queue = queueWithStack()
queue.enque(1)
queue.enque(2)
queue.enque(3)
print(queue.peek())
print(queue.deque())
print(queue.deque())
print(queue.peek())