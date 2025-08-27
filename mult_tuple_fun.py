def mult_tuple(tuple1, tuple2):
    """Returns a list of all possible combinations of given values."""
    result = []
    for a in tuple1:
        for b in tuple2:
            result.append((a,b))
            result.append((b,a))
    return tuple(result)

def mult_tuple_length_predict(tuple1, tuple2):
    """Validates number of combinations in mult_tuple function."""
    expected_num = len(tuple1)*len(tuple2)*2
    actual_num = len(mult_tuple(tuple1, tuple2))
    return expected_num == actual_num

def main():
    first_tuple = (1, 2)
    second_tuple = (4, 5)
    result = mult_tuple(first_tuple, second_tuple)
    print(result)
    print(mult_tuple_length_predict(first_tuple, second_tuple))

    first_tuple = (1, 2, 3)
    second_tuple = (4, 5, 6)
    result = mult_tuple(first_tuple, second_tuple)
    print(result)
    print(mult_tuple_length_predict(first_tuple, second_tuple))

if __name__ == '__main__':
    main()