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

    def makeLoop(self, index, inplace=False, visualize=False):
        if not isinstance(index, int):
            raise TypeError("index must be int")

        if self.head is None:
            raise IndexError("makeLoop index out of range")

        length = self.len
       
        if index < -length or index >= length:
            raise IndexError("makeLoop index out of range")

        if index < 0:
            index += length

        if not inplace:
            values = []
            cur = self.head
            while cur:
                values.append(cur.val)
                cur = cur.next

            new_list = LinkedList(nodes=values)
            target_list = new_list
        else:
            target_list = self

        cur = target_list.head
        target = None
        last = None
        i = 0
        while cur:
            if i == index:
                target = cur
            last = cur
            cur = cur.next
            i += 1

        last.next = target
        if visualize:
            target_list.visualize()
            
        if not inplace:
            return target_list

    def visualize_dot(self, max_nodes=100):
        if not isinstance(max_nodes, int):
            raise TypeError("max_nodes must be int")
        if max_nodes <= 0:
            raise ValueError("max_nodes must be > 0")

        lines = ["digraph LinkedList {", "  rankdir=LR;", "  node [shape=circle];"]
        node_ids = {}
        nodes = []

        cur = self.head
        steps = 0
        while cur and steps < max_nodes:
            obj_id = id(cur)
            if obj_id in node_ids:
                break
            node_name = f"n{len(nodes)}"
            node_ids[obj_id] = node_name
            nodes.append(cur)
            cur = cur.next
            steps += 1

        for i, node in enumerate(nodes):
            label = str(node.val).replace('"', '\\"')
            lines.append(f'  n{i} [label="{label}"];')

        for i, node in enumerate(nodes):
            nxt = node.next
            if nxt is None:
                continue
            nxt_id = id(nxt)
            if nxt_id in node_ids:
                lines.append(f"  n{i} -> {node_ids[nxt_id]};")
            else:
                break

        lines.append("}")
        return "\n".join(lines)

    def visualize_text(self, max_nodes=100):
        if not isinstance(max_nodes, int):
            raise TypeError("max_nodes must be int")
        if max_nodes <= 0:
            raise ValueError("max_nodes must be > 0")

        parts = []
        node_ids = {}
        nodes = []

        cur = self.head
        steps = 0
        loop_at = None
        while cur and steps < max_nodes:
            obj_id = id(cur)
            if obj_id in node_ids:
                loop_at = node_ids[obj_id]
                break
            node_ids[obj_id] = len(nodes)
            nodes.append(cur)
            parts.append(str(cur.val))
            cur = cur.next
            steps += 1

        if not nodes:
            return "Empty"

        text = " -> ".join(parts)
        if loop_at is not None:
            text += f" -> (loops to list[{loop_at}] = {parts[loop_at]})"
        elif cur is not None:
            text += " -> (truncated)"

        return text

    def visualize_png(self, output_path=None, max_nodes=100):
        if output_path is not None and not isinstance(output_path, str):
            raise TypeError("output_path must be str or None")
        if not isinstance(max_nodes, int):
            raise TypeError("max_nodes must be int")
        if max_nodes <= 0:
            raise ValueError("max_nodes must be > 0")

        try:
            from graphviz import Source
        except ImportError as exc:
            raise ImportError(
                "graphviz package is required for visualize_png. "
                "Install with: pip install graphviz"
            ) from exc

        import os

        if output_path is None:
            base_dir = os.path.dirname(__file__)
            images_dir = os.path.join(base_dir, "images")
            os.makedirs(images_dir, exist_ok=True)
            output_path = os.path.join(images_dir, "linked_list")

        dot = self.visualize_dot(max_nodes=max_nodes)
        src = Source(dot)
        src.format = "png"
        src.render(filename=output_path, cleanup=True)
        return output_path + ".png"
    
    def visualize(self, output_path=None, max_nodes=100):
        self.visualize_png(output_path, max_nodes)
        vizual_text = self.visualize_text(max_nodes)
        print(vizual_text)
