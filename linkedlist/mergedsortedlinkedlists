class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

def print_linked_list(head: ListNode) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next


def mergeTwoLists(list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # for remaining linked list elements after the traversal
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next


# example
l1 = ListNode(2)
a = ListNode(3)
b = ListNode(4)
l1.next = a
a.next = b

l2 = ListNode(1)
d= ListNode(5)
e = ListNode(8)
l2.next = d
d.next = e
print(print_linked_list(mergeTwoLists(l1, l2)))