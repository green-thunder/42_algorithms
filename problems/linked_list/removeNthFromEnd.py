from LinkedLIst import LinkedList, Node


def removeNthFromEnd(head: Node, n: int) -> Node:
    dummy = Node(0, head)
    slow = fast = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    return dummy.next

linked_list = LinkedList(nodes=[1,2,3,4,5,6])
n = 6

# linked_list.head = removeNthFromEnd(linked_list.head, n)

# print(linked_list)
