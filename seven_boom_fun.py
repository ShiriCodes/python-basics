def seven_boom(end_number: int) -> list[str | int]:

    """
    Returns a list containing numbers from 0 to 'end-number',
    with each multiple of 7 or number containing the digit 7 replaced by the string 'BOOM'.

    Example:
    print(seven_boom(17))
    ['BOOM', 1, 2, 3, 4, 5, 6, 'BOOM', 8, 9, 10, 11, 12, 13, 'BOOM', 15, 16, 'BOOM']

    :param end_number: An integer equal or larger than 0.
    :return: List containing numbers from 0 to 'end-number', with each multiple of 7 or number containing the digit 7 replaced by the string 'BOOM'.
    :raises TypeError: If 'end_number' is not an integer.
    :raises ValueError: If 'end_number' is lower than 0.
    """

    if not isinstance(end_number, int):
        raise TypeError("'end_number' must be an integer.")

    if end_number < 0:
        raise ValueError("'end_number' must be an integer equal or larger than 0.")

    num_list = list(range(end_number + 1))
    for i, num in enumerate(num_list):
        if num % 7 == 0 or '7' in str(num):
            num_list[i] = 'BOOM'

    return num_list


def main():
    assert seven_boom(0) == ['BOOM']
    assert seven_boom(17) == ['BOOM', 1, 2, 3, 4, 5, 6, 'BOOM', 8, 9, 10, 11, 12, 13, 'BOOM', 15, 16, 'BOOM']
    assert seven_boom(28) == ['BOOM', 1, 2, 3, 4, 5, 6, 'BOOM', 8, 9, 10, 11, 12, 13, 'BOOM', 15, 16, 'BOOM', 18, 19, 20, 'BOOM', 22, 23, 24, 25, 26, 'BOOM', 'BOOM']


    try:
        print(seven_boom('girl'))
    except TypeError as e:
        print("Caught error:", e)

    try:
        print(seven_boom(-2))
    except ValueError as e:
        print("Caught error:", e)


if __name__ == '__main__':
    main()
