def chocolate_maker(small, big, x):
    """
    Determine if it is possible to reach the exact length x using small and big chocolate bars.

    :param small: Number of small bars available (each length 1).
    :type small: int
    :param big: Number of big bars available (each length 5).
    :type big: int
    :param x: Target length to achieve.
    :type x: int
    :return: True if exact length x can be formed using the bars, False otherwise.
    :rtype: bool
    """
    small_length = 1
    big_length = 5

    max_big_needed = min(big, x // big_length)
    remainder = x - max_big_needed * big_length

    return (small * small_length) >= remainder and remainder % small_length == 0


if __name__ == "__main__":
    print(chocolate_maker(3, 1, 8))  # True
    print(chocolate_maker(3, 1, 9))  # False
    print(chocolate_maker(3, 2, 10)) # True
