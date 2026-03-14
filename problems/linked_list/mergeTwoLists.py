from LinkedLIst import LinkedList, Node

def mergeTwoLists(head1: Node, head2: Node) -> Node:
    curr1, curr2 = head1, head2
    head = new_list = Node()
    while curr1 or curr2:
        val1 = curr1.val if curr1 else float('inf')
        val2 = curr2.val if curr2 else float('inf')
        if val1 < val2:
            new_list.next = Node(val1)
            curr1 = curr1.next
        else:
            new_list.next = Node(val2)
            curr2 = curr2.next

        new_list = new_list.next

    return LinkedList(head.next)

def mergedTwoLists42(head1: Node, head2: Node) -> Node:
    curr1, curr2 = head1, head2
    head = curr = Node()

    while curr1 and curr2:
        if curr1.val < curr2.val:
            curr.next = curr1
            curr1 = curr1.next
        else:
            curr.next = curr2
            curr2 = curr2.next

        curr = curr.next

    curr.next = curr1 or curr2
    return LinkedList(head.next)

list1 = LinkedList(nodes=[1,2,4])
list2 = LinkedList(nodes=[1,3,5])

merged_list = mergedTwoLists42(list1.head, list2.head)

print(merged_list)

