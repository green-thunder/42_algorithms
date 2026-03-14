from LinkedLIst import LinkedList, Node


def middleNode(head: Node) -> Node:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


nodes = [1,2,3,4,5,6]
linkedList = LinkedList(nodes=nodes)

middle_node = LinkedList(middleNode(linkedList.head))
print(middle_node)

# middle_node = linkedList.middleNode()
# print(middle_node)