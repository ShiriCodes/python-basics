def sequence_del(my_str) -> str:

    """
    Returns a string with consecutive duplicate characters removed.
    """

    my_str = str(my_str)

    if not my_str:
        return ""

    result = [my_str[0]]
    for char in my_str[1:]:
        if char != result[-1]:
            result.append(char)

    return "".join(result)

def main():
    assert sequence_del("ppyyyyythhhhhooonnnnn") == 'python'
    assert sequence_del("SSSSsssshhhh") == 'Ssh'
    assert sequence_del("Heeyyy   yyouuuu!!!") == 'Hey you!'
    assert sequence_del("") == ''




if __name__ == '__main__':
    main()
