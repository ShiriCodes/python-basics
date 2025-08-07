def extend_list_x(list_x, list_y):
    """
    This function extends a list at its beginning with the contents of another list, yielding a new list.
    Example:
    [4, 5, 6], [1, 2, 3] → [1, 2, 3, 4, 5, 6]

    :param list_x: A list to be extended.
    :type list_x: list
    :param list_y: A list to inserted at the beginning.
    :type list_y: list
    :return: An extended list.
    :rtype: list
    """
    if not isinstance(list_x, list) or not isinstance(list_y, list):
        raise TypeError("Both inputs must be a lists")

    return [*list_y,*list_x]

def main():
    print(extend_list_x([1,2,3],[7,1]))
    print(extend_list_x(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"],[1]))

    try:
        print(extend_list_x(1,"q"))
    except TypeError as e:
        print("Caught error:", e)







if __name__ == '__main__':
    main()
