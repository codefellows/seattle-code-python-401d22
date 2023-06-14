# file = open('assets/spam.txt')
# print(file)
#
# contents = file.read()
# print(contents)
#
# print('Is the file closed: ', file.closed)

# with open('assets/spam.txt') as file:
#     print(file.read())
#
# print('Is the file closed: ', file.closed)

# print(help(file))

with open('assets/brain.jpg', 'rb') as file:
    contents = file.read()

with open('assets/brain.copy.jpg', 'wb') as file2:
    file2.write(contents)
