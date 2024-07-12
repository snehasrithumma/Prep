class CircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1
        return True

    def dequeue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size



# Circular Queue
# Definition: A circular queue is a linear data structure that uses a single, fixed-size buffer in a circular fashion. The end of the queue wraps around to the beginning when it reaches the end of the buffer.

# Key Characteristics:

# Single-ended operations: Elements can only be added (enqueued) at the rear and removed (dequeued) from the front.
# Fixed size: The size of the queue is fixed. When the queue is full, no more elements can be added until space is freed by removing elements.
# Circular behavior: The rear and front pointers wrap around to the beginning of the buffer when they reach the end.
# Operations:

# Enqueue: Add an element to the rear.
# Dequeue: Remove an element from the front.
# Peek: Get the element at the front without removing it.
# isEmpty: Check if the queue is empty.
# isFull: Check if the queue is full.
# Use Cases:

# Buffer management (e.g., circular buffers for data streams).
# Task scheduling.
# Round-robin scheduling.