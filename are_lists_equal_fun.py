def are_lists_equal(list1, list2):
    """
    This function checks whether two lists contain the same elements (order doesn't matter).
    Example:
    [0.6, 1, 2, 3], [3, 2, 0.6, 1] → True
    [0.6, 1, 2, 3], [9, 0, 5, 10.5] → False

    :param list1: A list of int or float elements.
    :type list1: list
    :param list2: A list of int or float elements.
    :type list2: list
    :return: True or False.
    :rtype: bool
    """
    if not (
        isinstance(list1, list) and isinstance(list2, list)
        and all(isinstance(x, (int, float)) for x in list1)
        and all(isinstance(x, (int, float)) for x in list2)
    ):
        raise TypeError("list1 and list2 must be lists that contain int or float elements")

    if not len(list1) == len(list2):
        return False

    return sorted(list1) == sorted(list2)


def main():
    print(are_lists_equal([0.6, 1, 2, 3], [3, 2, 0.6, 1]))
    print(are_lists_equal([0.6, 1, 2, 3], [9, 0, 5, 10.5]))
    print(are_lists_equal([0.6, 1, 2, 3], [0.6, 1, 3]))


    try:
        print(are_lists_equal([0.6, 1, 2, 3], [9, [4, 3], 5, 10.5]))
    except TypeError as e:
        print("Caught error:", e)







if __name__ == '__main__':
    main()
