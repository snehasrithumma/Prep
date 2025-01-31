class Stack:
    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        if self.is_empty():
            print('No data')
        else:
            return self.arr.pop()
    
    def peek(self):
        if self.is_empty():
            print('No data')
        else:
            return self.arr[-1]
    
    def is_empty(self):
        return len(self.arr) == 0
    
s = Stack()
s.push(1)
s.push(2)
print(s.peek())  # Output: 2
print(s.pop())  # Output: 2
print(s.is_empty())  # Output: False
print(s.pop())  # Output: 1
print(s.is_empty()) 