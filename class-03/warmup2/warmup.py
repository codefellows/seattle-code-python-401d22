# Given a string, write a function that will return a new string with only 1 of each char in the new string.
# commissioner
# comisner

def remove_char(strng):
    new_string = ''
    for char in strng:
        if char not in new_string:
            new_string += char
    return new_string

word = "commissioner"
# print(word[3])
print(remove_char(word))
print(remove_char('agressiveness'))
