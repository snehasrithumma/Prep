class Queue:
    def __init__(self, size):
        self.items = []
        self.max_size = size

    def is_empty(self):
        return len(self.items) == 0
    
    def is_full(self):
        return len(self.items) == self.max_size

    def peek(self):
        if self.is_empty():
            return IndexError('Empty Queue')
        else:
            return self.items[0]
        
    def enque(self, item):
        if self.is_full():
            print('Queue is full')
        else:
            self.items.append(item)
            print('added new element')

    def deque(self):
        if not self.is_empty():
           return  self.items.pop(0)
        else:
           print('Empty Queue')
        

    def size(self):
        return len(self.items)
    
    def print_q(self):
        for item in self.items:
            print(item, end='\n')
        print('done')

    
q = Queue(3)
q.enque(9)
q.enque(19)
q.enque(29)
q.print_q()
q.enque(39)
q.print_q()
q.peek()
q.deque()
q.peek()
q.size()
q.print_q()