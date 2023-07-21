class Hashtable:
    """
    Paramaters: Key, Value
    Returns: Nothing
    """

    def __init__(self, size=1024):
        self.size = size
        self.buckets = size * [None]



    def hash(self, key):
        """
        hash
        Arguments: key
        Returns: Index in the collection for that key
        :return:
        """
        # super
        #     ^
        # jump
        # 106 + 117 + 109 + 112 = 446
        # total = 0 + 115 + 117 + 112 + 101 + 114 = 560 * 11 = 10640
        # ['super: 100', None, None, None, None, None, 'jump: 734', None, None, None]
        total = 0
        for ch in key:
            total += ord(ch)
        primed = total * 19
        index = primed % self.size
        return index


if __name__ == '__main__':

    hash1 =  Hashtable()
    print(hash1.size)
    print(hash1.hash('super'))


