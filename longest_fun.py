def longest(my_list):
    """
    This function returns the longest string out of a list of strings.
    Example:
    ["111", "234", "2000", "goru", "birthday", "09"] → birthday

    :param my_list: A list of str elements.
    :type my_list: list
    :return: The longest str element in the list
    :rtype: str
    """
    if not (
        isinstance(my_list, list)
        and all(isinstance(x, (str)) for x in my_list)
    ):
        raise TypeError("my_list must be a list that contains str elements")

    if not my_list:
        raise ValueError("my_list is empty")

    return  max(my_list, key = len)


def main():
    print(longest(["hello", "hi", "Welcome"]))
    print(longest(["This", "is", "working"]))
    print(longest(["great", "to", "see", "that"]))
    print(longest(["111", "234", "2000", "goru", "birthday", "09"]))


    try:
        print(longest([[0.6, 1, 2, 3], [9, [4, 3], 5, 10.5]]))
    except TypeError as e:
        print("Caught error:", e)

    try:
        print(longest([]))
    except ValueError as e:
        print("Caught error:", e)






if __name__ == '__main__':
    main()
