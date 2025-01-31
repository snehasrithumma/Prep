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
