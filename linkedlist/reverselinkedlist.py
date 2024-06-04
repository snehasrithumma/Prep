class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


def print_linked_list(head: ListNode) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next

def reverse(head):
    if not head and not head.next:
        return head
    
    print(print_linked_list((l1)))
    prev , current = None, head
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
        print(print_linked_list((prev)))

    return prev

    
# example
l1 = ListNode(2)
a = ListNode(4)
b = ListNode(3)
l1.next = a
a.next = b
print(print_linked_list(reverse(l1)))
