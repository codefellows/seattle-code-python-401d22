class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current._next

    # ll1 [4]->[1]->[10]->[8]->None
    #                            ^
    # 4 1 10 8


    # Insert Node of 5
    # ll1 [4]->[1]->[10]->[8]->None
    # New node with a value of 5 and next of none
    # New nodes next will be the ll.head
    # reassign the ll head to the new node of 5
    # ll1 [5]->[4]->[1]->[10]->[8]->None




if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2, node1)
    # [2] -> [1] -> None
    print(node1.value)
    node1.value = 4
    print(node1.value)
