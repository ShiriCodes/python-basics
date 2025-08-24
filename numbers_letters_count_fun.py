def numbers_letters_count(my_str: str) -> list[int]:

    """
    Returns number of digits and non-digit characters in my_str.

    Example:
    print(numbers_letters_count("Python 3.6.3"))
    [3, 9]

    :param my_str: A string possibly containing different types of characters.
    :return: List of 2 number values - number of digits and non-digit characters in my_str.
    :raises TypeError: If 'my_str' is not a string.
    """

    if not isinstance(my_str, str):
        raise TypeError("'my_str' must be a string")

    digit_count = 0
    non_digit_count = 0
    for char in my_str:
        if char.isdigit():
            digit_count += 1
        else:
            non_digit_count +=1

    return [digit_count, non_digit_count]

def main():
    print(numbers_letters_count("Hell0"))
    print(numbers_letters_count("Python 3.6.3"))
    print(numbers_letters_count("89 9"))


    try:
        print(numbers_letters_count(8))
    except TypeError as e:
        print("Caught error:", e)



if __name__ == '__main__':
    main()
