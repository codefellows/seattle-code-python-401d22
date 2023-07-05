def encrypt(plain_text, potato):
    # Expected Input: 101, 11
    #                 ^
    # Expected Output: 212
    # Ideas?
    # Need a dictionary or list with stored plain text?
    # Maybe a string instead?
    # loop through and move by the shift
    # 1 or 11 or 21
    # shifted_key = potato % 10
    # print(shifted_key)
    encrypted_string = ''
    for char in plain_text:
        # num = int(char)
        new_num = (int(char) + potato) % 10
        # new_num = new_num % 10
        # 0 1 2 3 4 5 6 7 8 9
        #   ^
        # Num is 8
        # shift is 3
        encrypted_string += str(new_num)
    return encrypted_string


def decrypt(encoded, shift):
    return encrypt(encoded, -shift)


if __name__ == '__main__':
    print(encrypt('8473', 33))  # 1706
    print(decrypt('1706', 3))  # 8473
