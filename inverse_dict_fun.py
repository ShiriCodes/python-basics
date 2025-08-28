def inverse_dict(my_dict: dict) -> dict:
    """Returns a new dictionary with original values as keys and lists of original keys as values."""
    new_dict = {}
    if not isinstance(my_dict, dict):
        raise TypeError(f"Expected dict, got {type(my_dict).__name__}.")
    for key, value in my_dict.items():
        if value in new_dict:
            new_dict[value].append(key)
        else:
            new_dict[value] = [key]
    return dict(sorted(new_dict.items()))

def main():
    print(inverse_dict({1:'hey'}))
    print(inverse_dict({}))
    print(inverse_dict({'I': 3, 'love': 3, 'self.py!': 2}))
    try:
        print(inverse_dict('heyyy 1'))
    except TypeError as e:
        print(f"Input must be a dictionary. {e}")


if __name__ == '__main__':
    main()