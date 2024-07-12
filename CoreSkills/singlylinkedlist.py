class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, i : int):
        index = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next_node

        return -1
    
    def insertHead(self, val:int):
        self.head.next_node = ListNode(val, self.head.next_node)
        if not self.head.next_node.next_node:
            self.tail = self.head.next_node

    def insertTail(self, val:int):
        self.tail.next_node = ListNode(val)
        self.tail = self.tail.next_node

    def remove(self, i:int):
        index = 0
        curr = self.head
        while index < i and curr:
            curr = curr.next_node
            index+=1
        if curr and curr.next_node:
            if curr.next_node == self.tail:
                self.tail == curr.next_node

            curr.next_node = curr.next_node.next_node
            return True
        return False
    
    def getValues(self):
        result = []
        curr = self.head.next
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result


    