# nobody asked about capital / lowercase

def is_panagram(word):
    ALPHA = "abcdefghijklmnopqrstuvwxyz"
    new_str = ''
    for char in word.lower():
        if char not in new_str and char in ALPHA:
            new_str += char

    if len(new_str) == 26:
        return True
    else:
        return False


def delete_over(lst, num):
    # Iterate through the list of LinkedLists one by one
    for ll in lst:
        # Set the 'current' variable to the head of the current LinkedList
        current = ll.head
        # Initialize a 'prev' variable to keep track of the previous node in the LinkedList
        prev = None
        # Traverse the current LinkedList
        while current:
            # Check if the value of the current node is greater than 'num'
            if current.vaue > num:
                # If the current node is the head of the LinkedList
                if current == ll.head:
                    # Update the head to the next node (remove the current node)
                    ll.head = current.next
                else:
                    prev.next = current.next

            else:
                # If the current node is not the head
                # Update the 'next' of the previous node to skip the current node
                # Move to the next node in the LinkedList
                prev = current
            current = current.next




# Walkthrough

# lst = (ll1, ll2)
#              ^
# Int : 9

# ll1 = [10] -> None
#                ^
# current:
# previous:

# ll2 = [3] -> [10] -> [5] -> None
#               ^
# current:
# previous:
