# Given 3 LL, sum the numbers represented by the ll
# ll1 1->2->3->None = 123
#               ^
# ll2 2->3->4->None = 234
#              ^
# ll3 3->4->5->None = 345
#               ^
# return 702

def sum_ll(ll1, ll2, ll3):
    current1 = ll1.head
    current2 = ll2.head
    current3 = ll3.head
    num1 = '1'
    num2 = '234'
    num3 = '345'
    while current1:
        num1 += str(current1.value)
        current1 = current1.next

    while current2:
        num2 += str(current2.value)
        current2 = current2.next

    while current3:
        num3 += str(current3.value)
        current3 = current3.next
    return int(num1) + int(num2) + int(num3)

# num1 = ''
# num2 = ''
# num3 = ''












# Given 3 LL, sum the numbers represented by the ll
# ll1 1->2->3->None = 123
#   ^
# ll2 2->3->4->None = 234
#   ^
# ll3 3->4->5->None = 345
#   ^
# return 702

# num =
# Total = 0
def sum_ll_streamlines(ll1, ll2, ll3):
    total = 0
    num_list = [ll1, ll2, ll3]

    for lst in num_list:
        current = lst.head
        num = ''
        while current:
            num += current.value
            current = current.next
        total += int(num)
    return total
