from LinkedLIst import LinkedList, Node

def addTwoNumbers(head1: Node, head2: Node) -> Node:
    curr1, curr2 = head1, head2
    odd = 0 
    head = curr = Node()

    while curr1 or curr2 or odd:
        total = sum([
            curr1.val if curr1 else 0, 
            curr2.val if curr2 else 0,
            odd
        ])
        odd, val = divmod(total, 10)
        curr.next = Node(val)
        if curr1: curr1 = curr1.next
        if curr2: curr2 = curr2.next

        curr = curr.next

    return LinkedList(head.next)


list1 = LinkedList(nodes=[1,9,1])
list2 = LinkedList(nodes=[9,1,9])

result = addTwoNumbers(list1.head, list2.head)

print(result)