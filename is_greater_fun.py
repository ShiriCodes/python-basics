def is_greater(my_list: list[int | float], n: int | float) -> list[int | float]:

    """
    Returns a list of numbers larger than 'n'.

    Example:
    result = is_greater([1, 30, 25, 60, 27, 28], 28)
    print(result)
    [30, 60]

    :param my_list: List of numbers.
    :param n: Number.
    :return: List of numbers larger than 'n' out of 'my_list'.
    :raises TypeError: If 'n' is not a number, or 'my_list' is not a list of numbers.
    """

    if not isinstance(n, (int, float)):
        raise TypeError("'n' must be a number")
    if not isinstance(my_list, list):
        raise TypeError("'my_list' must be a list")
    if not all(isinstance(item, (int, float)) for item in my_list):
        raise TypeError("'my_list' must be a list of numbers")

    result = []
    for number in my_list:
        if number > n:
            result.append(number)

    return result



def main():
    print(is_greater([1, 30, 25, 60, 27, 28], 28))
    print(is_greater([-1, 30, -25, 60, -27, 28], 3))
    print(is_greater([1, 30, 25, -60, 27, -28], -11))


    try:
        print(is_greater(3.9, 8))
    except TypeError as e:
        print("Caught error:", e)



if __name__ == '__main__':
    main()
