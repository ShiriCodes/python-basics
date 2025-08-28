def count_chars(my_str: str) -> dict[str, int]:
    """Returns dictionary with characters (no spaces) as keys and number of repeats in my_str as values."""
    seen = set()
    unique_chars = []
    for char in my_str:
        if char not in seen and char != ' ':
            unique_chars.append(char)
            seen.add(char)
    str_dict = {}
    for char in unique_chars:
        count = my_str.count(char)
        str_dict[char] = count
    return str_dict

def main():
    print(count_chars('ap ple'))
    print(count_chars(''))
    print(count_chars(str('a'*1000)))
    try:
        print(count_chars(1))
    except TypeError as e:
        print(f"Input must be a string. {e}.")


if __name__ == '__main__':
    main()