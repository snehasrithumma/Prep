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


# # example
# l1 = ListNode(0)
# a = ListNode(3)
# b = ListNode(5)
# l1.next = a
# a.next = b

# l2 = ListNode(1)
# d= ListNode(5)
# e = ListNode(8)
# l2.next = d
# d.next = e
# print(print_linked_list(mergeTwoLists(l1, l2)))

# print(print_linked_list(l1))
# # adding element at the end of linked list
# f = ListNode(2)
# head = l1
# while head.next:
#     head = head.next
# head.next = f
# head = f
# print(print_linked_list(l1))
# print(print_linked_list(head))


# # Deleting List Node
# current = l1
# l1 = l1.next
# current.next = None

# print(print_linked_list(l1))
# print(print_linked_list(current))
print('---------')
h1 = ListNode(2)
h2 = ListNode(4)
h3 = ListNode(6)
h4 = ListNode(8)
h1.next = h2
h2.next = h3
h3.next = h4
head = h1

current = head
i = 0
while current.next:
    pointer = current
    temp = current.next
    while current.next.next:
        current = current.next
    if current == pointer:
        break
    tail = current.next
    current.next = None
    pointer.next = tail
    tail.next = temp
    current = temp
print(print_linked_list(head))
    