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