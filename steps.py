"""How many different ways can you climb a staircase of `n` steps?

You can climb 1, 2, or 3 steps at a time.

For one step, we could do this one way: 1

    >>> steps(1)
    1

For two: 11 2

    >>> steps(2)
    2

For three: 111 12 21 3

    >>> steps(3)
    4

For four: 1111 121 211 112 22 13 31

    >>> steps(4)
    7

For five: 11111 2111 1211 1121 1112 122 121 221 113 131 311 23 32

    >>> steps(5)
    13

For six steps: 111111 21111 12111 11211 11121 11112 2211 2121 2112
    1212 1122 1221 3111 1311 1131 1113 321 312 213 231 132 123 222 33

    >>> steps(6)
    24
"""


def steps(stairs):
    """How many different ways can you climb a staircase of `n` steps?

    You can climb 1, 2, or 3 steps at a time.
    """

    def get_combos(stairs):
        """Get all combos of strides you could use to climb given stairs."""

        combos = set()

        for stride in [1, 2, 3]:

            if stairs % stride == 0:
                combos.add(str(stride) * int(stairs / stride))

            if stairs > stride:
                combos.update(str(stride) + combo
                    for combo in get_combos(stairs - stride))

        return combos

    return len(get_combos(stairs))





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED! YOU'RE A STAIRMASTER!\n")
