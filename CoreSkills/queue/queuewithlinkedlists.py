class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, max_size):
        self.front = None
        self.back = None
        self.size = 0
        self.max_size = max_size

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, item):
        if self.size < self.max_size:
            new_node = Node(item)
            if self.back:
                self.back.next = new_node

            self.back = new_node
            if self.front is None:
                self.front = new_node

            self.size+=1
        else:
            print('full cant add: '+str(item))


    def dequeue(self):
        temp = self.front
        self.front = temp.next
        self.size-=1
        if self.front is None:
            self.rear = None
            self.size = 0
        return temp.data
    
    def peek(self):
        if not self.is_empty():
            return self.front.data
        
    def printQueue(self):
        result = []
        curr = self.front
        while curr:
            result.append(curr.data)
            curr = curr.next
        print('items : '+', '.join(map(str,result)))


    def getValue(self, index):
        cur = self.front
        i = 0
        while cur:
            if i == index:
                return cur.data
            cur = cur.next
            i+=1
        return -1

q = Queue(4)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.printQueue()
print(q.dequeue())  # Output: 10
q.printQueue()
q.enqueue(40)
q.printQueue()
print(q.peek())     # Output: 20
print('index:'+str(q.getValue(3)))