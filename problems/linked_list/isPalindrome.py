from LinkedLIst import LinkedList, Node

def isPalindrome(head: Node) -> bool:
    linked_list = LinkedList(head)
    middle: LinkedList = linked_list.middleNode()
    middle.reverse()

    curr1, curr2 = linked_list.head, middle.head
    while curr2:
        if curr1.val != curr2.val:
            return False
        
        curr1 = curr1.next
        curr2 = curr2.next


    return True

nodes = [1,2,3,4,3,2,1]
linked_list = LinkedList(nodes=nodes)
result = isPalindrome(linked_list.head)
print(result)

