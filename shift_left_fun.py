def shift_left(my_list):
    """
    This function is meant for shifting a list of any length one step to the left. For example: [1, 2, 3] → [2, 3, 1]

    :param my_list: A list to be shifted.
    :type my_list: list
    :return: A list based on the original list, shifted.
    :rtype: list
    """
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list")

    if len(my_list) < 2:
        return my_list.copy()
    
    first_to_last_item = my_list[0]
    rest_of_my_list = my_list [1:]
    return rest_of_my_list + [first_to_last_item]

def main():
    print(shift_left([1,2,3]))
    print(shift_left(["wc","wgr","wfc","evee","erqqqqqqecf"]))
    print(shift_left([1]))
    print(shift_left([]))
    try:
        print(shift_left(1))
    except TypeError as e:
        print("Caught error:", e)





if __name__ == '__main__':
    main()
