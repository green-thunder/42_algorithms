from LinkedLIst import LinkedList, Node

def reverse(head: Node) -> Node:
    curr = head
    prev = None

    while curr:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_

    return LinkedList(prev)


nodes = [1,2,3,4,5]
linked_list = LinkedList(nodes=nodes)

#1
# reversed_list = reversed(linked_list)

#2
# linked_list.reverse()

#3
# reversed_list = linked_list.reverse(inplace=False)

reversed_list = reverse(linked_list.head)
print(reversed_list)