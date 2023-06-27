# Given nested lists of integers, write some code that will add 2 to each one.
#
# Input:
#    |
# [ [1, 2, 3] , [4, 5, 6] ]
#
# Output:
#
# [[3, 4, 5], [6, 7, 8]]

def add_2(lst):
    for items in lst:
        for i, num in enumerate(items):
            num += 2
            items[i] = num
    return lst

def print_months(lst):
    for i, month in enumerate(lst):
        print(f'{month} : {i + 1}')



if __name__ == '__main__':
    # list1 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
    #          'November', 'December']
    lst = [ [1, 2, 3] , [4, 5, 6] ]
    # print(add_2(lst))

    print_months(list1)
