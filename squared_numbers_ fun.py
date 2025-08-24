def squared_numbers(start: int, stop: int) -> list[int]:

    """
    Return a list of squares from start to stop (inclusive).

    Example:
        squared_numbers(4, 8) -> [16, 25, 36, 49, 64]
        squared_numbers(-3, 3) -> [9, 4, 1, 0, 1, 4, 9]

    :param start: Start of the range (integer).
    :param stop: End of the range (integer, must be >= start).
    :return: List of squared numbers.
    :raises TypeError: If 'start' or 'stop' are not integers.
    :raises ValueError: If 'stop' is smaller than 'start'.
    """

    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("'start' and 'stop' must be integers")

    if stop  < start:
        raise ValueError ("'stop' must be equal or larger than 'start'")

    i = start
    squares_list = []
    while i <= stop:
        squares_list.append(i ** 2)
        i += 1
    return squares_list


def main():
    print(squared_numbers(4, 8))
    print(squared_numbers(-3, 3))
    print(squared_numbers(0, 0))


    try:
        print(squared_numbers(3.9, 8))
    except TypeError as e:
        print("Caught error:", e)

    try:
        print(squared_numbers(9, 8))
    except ValueError as e:
        print("Caught error:", e)



if __name__ == '__main__':
    main()
