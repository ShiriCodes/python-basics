def are_files_equal(file1, file2) -> bool:
    """Returns True if two files have the same contents, line by line, in the same order."""
    for line1, line2 in zip(file1, file2):
        if line1 != line2:
            return False
    remaining1 = file1.readline()
    remaining2 = file2.readline()
    return remaining1 == remaining2 == ''

def are_files_equal_phrasing(file1, file2):
    """Prints output according to files being identical or not."""
    if are_files_equal(file1, file2):
        print("Files are identical.")
    else:
        print("First and second files are not identical.")


def main():
    from io import StringIO
    f1 = StringIO("test\nline")
    f2 = StringIO("test\nline")
    f3 = StringIO("test\nline")
    f4 = StringIO("test\nline")
    f5 = StringIO("test\ntest")
    f6 = StringIO("test\nline\nline")
    f7 = StringIO("")
    f8 = StringIO("test\nline")

    are_files_equal_phrasing(f1, f2)
    are_files_equal_phrasing(f3, f6)
    are_files_equal_phrasing(f4, f7)
    are_files_equal_phrasing(f5, f8)




if __name__ == '__main__':
    main()