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
