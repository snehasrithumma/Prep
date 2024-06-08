class Queue:
    def __init__(self) -> None:
        self.items = []

    def is_empty(s):
        return len(s) == 0
    
    def peek(self):
        if self.is_empty:
            return IndexError('Empty Queue')
        else:
            return self.items[0]
        
    def enque(self, item):
        self.items.append(item)

    def deque(self):
        if not self.is_empty:
           return  self.items.pop(0)
        else:
            return IndexError('Empty Queue')
        

    def size(self):
        return len(self.items)
    
    def print_q(self):
        for item in self.items:
            print(item, end='->')
    
q = Queue()
q.items = [1,5,6]
q.print_q()
q.enque(9)
q.peek()
q.size()
q.deque()
q.peek()
q.size()