class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        """
        Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
        Arguments: none
        Returns: Sting representation of LinkedList
        """

        # ll: [1] -> [2] -> None
        #                    ^
        # output: { 1 } -> { 2 } -> None
        current = self.head
        output = ''
        while current:
            output += f'{{ {current.value} }} -> '
            current = current.next
        output += 'None'
        return output

    def traverse(self):
        """
        Sample method to show how to traverse a linkedlist
        Arguments: none
        Return: thing done in loop
        """
        # ll: [1] -> [2] -> None
        #                    ^
        current = self.head
        while current:
            # Do the thing you want to do
            current = current.next

    def insert(self, value):
        """
        Adds a new node with that value to the head of the list with an O(1) Time performance.
        Arguments: value
        Returns: nothing
        """
        # Insert 3
        # ll: [3] -> [1] -> [2] -> None
        # ll:  # [1] -> [2] -> None
        #      ^
        node = Node(value)
        if self.head:
            node.next = self.head
        self.head = node

    def includes(self, value):
        """
        Indicates whether that value exists as a Node’s value somewhere within the list.
        Arguments: value
        Returns: Boolean
        """
        # Value 2
        # ll: [1] -> [2] -> None
        #             ^
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False


if __name__ == '__main__':
    # ll: [1] -> [2] -> None
    node1 = Node(1)
    node2 = Node(2)
    ll = LinkedList(node1)
    node1.next = node2
    print(ll)
    print(ll.includes(1)) # True
    print(ll.includes(3)) # False
    ll.insert(3)
    print(ll)
    print(ll.includes(3)) # True
