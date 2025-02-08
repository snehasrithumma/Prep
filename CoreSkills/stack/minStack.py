class MinStack:

    def __init__(self):
        self.arr = []
        self.min = []

    def push(self, val: int) -> None:
        if len(self.min) == 0 or val <= self.min[-1]:
            self.min.append(val)
        self.arr.append(val)

    def pop(self) -> None:
        if self.arr[-1] == self.min[-1]:
            self.min.pop()
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
obj.push(2)
obj.push(5)
obj.push(2)
obj.pop()
print(obj.top())
print(obj.getMin())



class stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def add(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
    
    def remove(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None
    
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None
    
a = stack()
a.add(9)
a.add(6)
a.add(10)
a.add(2)
print(a.min_stack)
print(a.stack)
print(a.getMin())
print('----')
print(a.remove())
print(a.min_stack)
print(a.stack)
print('----')
print(a.remove())
print(a.min_stack)
print(a.stack)
print(a.getMin())