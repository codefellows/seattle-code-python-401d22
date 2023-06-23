from node import Node

class Stack:
    """
    Create a Stack class that has a top property. It creates an empty Stack when instantiated.
    This object should be aware of a default empty value assigned to top when the stack is created.
    """
    def __int__(self):
        self.top = None

    def push(self, value):
        node =Node(value)

        """
        ALOGORITHM push(value)
        // INPUT <-- value to add, wrapped in Node internally
        // OUTPUT <-- none
           node = new Node(value)
           node.next <-- Top
           top <-- Node
        """
    # push
    # Arguments: value
    # adds a new node with that value to the top of the stack with an O(1) Time performance.


    def pop(self):
        pass
    # pop
    # Arguments: none
    # Returns: the value from node from the top of the stack
    # Removes the node from the top of the stack
    # Should raise exception when called on empty stack


    def peek(self):
        pass
    # peek
    # Arguments: none
    # Returns: Value of the node located at the top of the stack
    # Should raise exception when called on empty stack


    def is_empty(self):
        pass
    # is empty
    # Arguments: none
    # Returns: Boolean indicating whether or not the stack is empty.