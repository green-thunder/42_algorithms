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


    def printNodes(self):
        curr = self.head
        listNodes = []
        while curr:
            listNodes.append(curr.val)
            curr = curr.next

        print(listNodes)
        