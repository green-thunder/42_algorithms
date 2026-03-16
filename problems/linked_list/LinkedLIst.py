class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None, nodes=[0]):
        self.len = None
        if not head:
            self.len = len(nodes)
            head = Node(nodes[0])
            curr = head
            for i in range(1, len(nodes)):
                node = Node(nodes[i])
                curr.next = node
                curr = curr.next
        
        self.head = head
        if not self.len:
            self.__len__()


    def __len__(self):
        if not self.len:
            length = 0
            curr = self.head
            while curr:
                length += 1
                curr = curr.next

            self.len = length

        return self.len

    def __repr__(self):
        curr = self.head
        listNodes = []
        while curr:
            listNodes.append(curr.val)
            curr = curr.next

        return listNodes.__repr__()
    
    def __reversed__(self):
        curr = self.head
        prev = None

        while curr:
            new_node = Node(curr.val)
            new_node.next = prev
            prev = new_node
            curr = curr.next

        return LinkedList(prev)
    
    def __eq__(self, other):
        curr1 = self.head
        curr2 = other.head

        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False
            
            curr1 = curr1.next
            curr2 = curr2.next

        return not(curr1 or curr2)

    def middleNode(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return LinkedList(slow)
    
    def reverse(self, inplace=True):
        curr = self.head
        prev = None

        while curr:
            new_node = Node(curr.val)
            new_node.next = prev
            prev = new_node
            curr = curr.next

        if inplace:
            self.head = prev
            return

        return LinkedList(prev)
    
    def pop(self, index=-1):
        if not isinstance(index, int):
            raise TypeError("index must be int")

        if self.head is None:
            raise IndexError("pop from empty list")

        length = self.len
      
        if index < -length or index >= length:
            raise IndexError("pop index out of range")

        if index < 0:
            index += length

        dummy = Node(0, self.head)
        prev = dummy
        for _ in range(index):
            prev = prev.next

        target = prev.next.val
        prev.next = prev.next.next
        self.head = dummy.next
        return target
