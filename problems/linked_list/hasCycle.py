
from LinkedLIst import LinkedList, Node

def hasCycle(head: Node) -> bool:
  hasSeen = []
  curr = head
  while curr:
    if curr in hasSeen:
      return True
    hasSeen.append(curr) 
    curr = curr.next

  return False

linked_list = LinkedList(nodes=[1,2,3,4,5])

linked_list.makeLoop(1, inplace=True)

linked_list.visualize()
is_cycle = hasCycle(linked_list.head)
print(is_cycle)