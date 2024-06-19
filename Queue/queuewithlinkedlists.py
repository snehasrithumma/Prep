class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def is_empty(self):
        return self.front is None
    
    def enque(self, item):
        new_node = Node(item)
        if self.back:
            self.back.next = new_node

        self.back = new_node
        if self.front is None:
            self.front = new_node

        self.size+=1