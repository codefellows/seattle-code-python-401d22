POINTS = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
    'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
    'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4,
    'z': 10
}

def score_word(word):
    # EXTRA:  check if word empty
    if not word:
        return 0
    # DONE: set initial total
    score = 0
    # DONE: loop through word
    for letter in word:
    # EXTRA:  check if it is alpha for additional check
        if letter.isalpha():
    # DONE: add POINTS value to total
            score += POINTS[letter]
    # DONE: return total
    return score



if __name__ == '__main__':
    print(score_word('cabbage')) #14
    print(score_word('za')) #11
    print(score_word('qi')) #11
    print(score_word('qi za')) #22
    print(score_word('lsdjfglkjndfuh4ijnp9=743+5n9-un9 7v84'))
    print(score_word('')) #0
