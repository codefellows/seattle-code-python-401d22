class Node:
    """
    Docstring
    """

    def __int__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    """
    Docstring
    """

    def pre_order(self, values=[]):
        # root >> left >> right
        # tree.root = 4
        #                       4
        #                     /   \
        #                   7      18
        #                 /   \   /   \
        #                3     1 5     11

        # expected   [4, 7, 3, 1, 18, 5, 11]
        # value_list = walk_through [[4, 7, 3, 1, 18, 5, 11]]
        def walk(input_node, value_list):
            if not input_node:
                return
            # handle root
            value_list.append(input_node.value)

            # handle left
            walk(input_node.left, value_list)

            # handle right
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def in_order(self):
        # left >> root >> right
        pass

    def post_order(self):
        # left >> right >> root
        pass




class BinarySearchTree(BinaryTree):
    """
    Docstring
    """

    def add(self):
        pass

    def contains(self):
        pass
