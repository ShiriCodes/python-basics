def format_list(my_list):
    """
    This function formats a list into a string consisting of the items at even indices (0, 2, 4, ...)
    and the last item in the list, separated by 'and'.
    Example:
    [1, 2, 3] → "1 and 3"
    ["a", "b", "c", "d", "e"] → "a, c and e"

    :param my_list: A list to be formatted.
    :type my_list: list
    :return: A string containing my_list items in even places and both "and" and the last my_list item .
    :rtype: str
    """
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list")

    if 0 < len(my_list) < 2:
        return str(my_list[-1])

    if len(my_list) == 0:
        raise ValueError("Input must contain at least one item")

    even_placed_items = my_list[0:-1:2]
    even_placed_items_str = ", ".join(map(str, even_placed_items))
    last_item = str(my_list[-1])
    return even_placed_items_str + " and " + last_item

def main():
    print(format_list([1,2,3]))
    print(format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))

    try:
        print(format_list(1))
    except TypeError as e:
        print("Caught error:", e)

    try:
        print(format_list([]))
    except ValueError as e:
        print("Caught error:", e)

    print(format_list([1]))






if __name__ == '__main__':
    main()
