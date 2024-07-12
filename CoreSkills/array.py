class Array:
    def __init__(self, capacity):
        self.length = 0
        self.capacity = capacity
        self.arr = [0] * capacity

    def get(self, i: int):
        return self.arr[i]
    
    def set(self, i: int, n: int):
        self.arr[i] = n
    
    def pushback(self, n: int):
        self.capacity = self.capacity+1
        self.arr[self.length] = n
        self.length +=1

    def popback(self):
        if self.length > 0:
            self.length -= 1
        return self.arr[self.length]
    
    def resize(self):
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity

        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self):
        return self.length
    
    def getCapacity(self):
        return self.capacity
     



a = Array(3)
print(a.get(0))
a.set(0, 9)
print(a.get(0))
a.pushback(10)
print('-----')
for i in range(a.getSize()):
    print(i, a.get(i))
print(a.arr)
print('*****')
a.resize()
a.pushback(20)
for i in range(a.getSize()):
    print(i, a.get(i))
print(a.length)
print(a.capacity)
print(a.arr)