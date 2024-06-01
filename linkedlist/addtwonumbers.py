class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


def print_linked_list(head: ListNode) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next

def add(l1, l2):
    head = ListNode(0)
    tail = head
    carry = 0
    while l1 and l2 or carry != 0:
        digit1 = l1.val if l1 else 0
        digit2 = l2.val if l2 else 0 
        sum = digit1+ digit2 + carry

        carry = sum // 10
        digit = sum % 10

        newNode = ListNode(digit)
        tail.next = newNode
        tail = tail.next

        l1 = l1.next if l1 else 0
        l2 = l2.next if l2 else 0

    result = head.next
    head.next = None
    return result


# example
l1 = ListNode(2)
a = ListNode(4)
b = ListNode(3)
l1.next = a
a.next = b

l2 = ListNode(5)
d= ListNode(6)
e = ListNode(4)
l2.next = d
d.next = e
print(print_linked_list(add(l1, l2)))



