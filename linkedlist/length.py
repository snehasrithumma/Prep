class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> None
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

def length(head):
    count = 0
    current = head
    while current:
        count+=1
        current = current.next
    return count

print((length(node1)))
