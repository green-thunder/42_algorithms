class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None, nodes=[0]):
        if not head:
            head = Node(nodes[0])
            curr = head
            for i in range(1, len(nodes)):
                node = Node(nodes[i])
                curr.next = node
                curr = curr.next
        
        self.head = head


    def __repr__(self):
        curr = self.head
        listNodes = []
        while curr:
            listNodes.append(curr.val)
            curr = curr.next

        return listNodes.__repr__()


    def middleNode(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return LinkedList(slow)
        