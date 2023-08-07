# Given a linked list of objects, with an age property, and a target
# age, find the age that is closest in age to the target age

# [{age: 23}] -> [{age: 10}] -> [{age: 45}] -> None
#    ^^^
# age is 19
# closest_age: 4

class Node:
    def __init__(self, value=None, next=None):
        if value is None:
            value = {}
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head


def closest_age(ll, age):
    closest_age = 100
    current = ll.head
    while current:
        if abs(age - current.value['age']) < closest_age:
            closest_age = current.value['age']
        # temp_age = current.value['age'] % age
        # if temp_age < closest_age:
        #     closest_age = current.value['age']
        current = current.next
    return closest_age


if __name__ == '__main__':
    ll = LinkedList()
    node1 = Node({'age': 45})
    node2 = Node({'age': 10}, node1)
    node3 = Node({'age': 23}, node2)
    ll.head = node3

    print(closest_age(ll, 19))

