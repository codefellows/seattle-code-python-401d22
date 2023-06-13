def factorial(n):
    """
    :param n: Number to facorialize
    :return: n * n -1 (etc)
    """

    if n <= 1:
        return 1

    return n * factorial(n - 1)


factorial(3)

# return 1
# return 2 * 1
# return 2 * factorial(1) = 2 * 1
# return 3 * 2
# return 3 * factorial(2) - 3 * 2
# return 6

