class MyCircularDeque:
    def __init__(self, k: int):
        self.size = k
        self.deque = [None] * k
        self.front = 0
        self.rear = 0
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.size) % self.size
        self.deque[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deque[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.size) % self.size
        self.deque[self.rear] = None
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1 + self.size) % self.size]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.front == self.rear

# Example usage:
deque = MyCircularDeque(3)
print(deque.deque)
# print(deque.insertLast(1))  # True
# print(deque.deque)
# print(deque.insertLast(2))  # True
# print(deque.deque)
# print(deque.insertFront(3))  # True
# print(deque.insertFront(4))  # False, the deque is full
# print(deque.getRear())  # 2
# print(deque.isFull())  # True
# print(deque.deleteLast())  # True
print(deque.insertFront(4))  # True
print(deque.getFront())  # 4
print(deque.insertFront(5))  # True
# print(deque.deque)
# print(deque.deleteFront())  # 4
# print(deque.deque)
print(deque.insertLast(2))  # True
print(deque.deque, deque.front, deque.rear, deque.size, deque.count)



# Circular Deque
# Definition: A circular deque is a double-ended queue that uses a circular buffer to allow insertion and deletion of elements from both the front and rear.

# Key Characteristics:

# Double-ended operations: Elements can be added or removed from both the front and the rear.
# Fixed size: The size of the deque is fixed. When the deque is full, no more elements can be added until space is freed by removing elements.
# Circular behavior: Both front and rear pointers wrap around to the beginning of the buffer when they reach the end.
# Operations:

# EnqueueFront: Add an element to the front.
# EnqueueRear: Add an element to the rear.
# DequeueFront: Remove an element from the front.
# DequeueRear: Remove an element from the rear.
# PeekFront: Get the element at the front without removing it.
# PeekRear: Get the element at the rear without removing it.
# isEmpty: Check if the deque is empty.
# isFull: Check if the deque is full.
# Use Cases:

# Complex buffering systems.
# Real-time data processing.
# Palindrome checking.