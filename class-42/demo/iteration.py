class LinkedList:
# [1, 2, 3, 4]
# [1] -> [2] -> [3] -> [4] -> None
#                              ^
    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_generator()

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

if __name__ == '__main__':
    # def gen():
    #     for num in range(11):
    #         yield num
    #
    # num_generator = gen()
    # try:
    #     print(next(num_generator))
    #     print(next(num_generator))
    #     print(next(num_generator))
    #     print(next(num_generator))
    #     print(next(num_generator))
    #     print(next(num_generator))
    #     print(next(num_generator))
    #     print(next(num_generator))
    #     print(next(num_generator))
    #     print(next(num_generator))
    #     print(next(num_generator))
    #     print(next(num_generator))
    # except StopIteration:
    #     print('We are all done')
    lst = [1, 2, 3, 4]
    ll1 = LinkedList(lst)
    # [1] -> [2] -> [3] -> [4] -> None

    iterator = iter(ll1)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

    # print(next(ll1))
