"""
File Services Interactive Menu

This Python program demonstrates the use of:
- File handling (reading text files)
- Input validation (menu options and numbers)
- Basic control flow with a looped service menu
- String operations (sorting words, reversing lines)
- Lists, sets, and simple iteration

Features:
- sort: print all unique words in the file as a sorted list
- rev: print each line from the file with characters reversed
- last: print the last N lines of the file (with N chosen by the user)
- Interactive menu with simple separators for clarity

Note:
This project was created as part of my Python learning journey.
It’s a practical way to practice working with files, strings,
and user interaction in Python.

GitHub: ShiriCodes
Date: 2025-08-29
"""
MENU_TEXT = ("Service menu:"
             "\nsort - print sorted unique words"
             "\nrev - reverse each line"
             "\nlast - print number of last lines based on your input"
             "\n0 - exit"
             "\nEnter a task: ")

VALID_OPTIONS = {'sort', 'rev', 'last', '0'}

def separate(my_string: str):
    """Return a simple separator line made of the given string."""
    return my_string*20

def service_input_validator(basic_service_input):
    """Validate menu input and return it s / r / v."""
    chosen_service = str(basic_service_input).lower()
    if chosen_service not in VALID_OPTIONS:
        raise ValueError ("\nInput must be from menu (sort / rev / last / 0). \n"
                          "Please try again:\n")
    return chosen_service

def menu_input():
    """Prompt the user to select a menu option and validate the input."""
    basic_service_input = input(MENU_TEXT)
    return service_input_validator(basic_service_input)

def process_sort_service(my_file_path):
    """Handle sort service - return sorted unique words."""
    words = set()
    with open(my_file_path, 'r') as f:
        for line in f:
            for word in line.split():
                words.add(str(word.strip()))
    sorted_words = sorted(words, key=lambda w: w.lower())
    return sorted_words

def process_reverse_service(my_file_path):
    """Handle reverse service - reverse each line."""
    reversed_lines = []
    with open(my_file_path, 'r') as f:
        for line in f:
            reversed_lines.append(line.rstrip()[::-1])
    return "\n".join(reversed_lines)

def get_number_of_rows_input(my_file_path):
    """Get number of lines from user input and validate it."""
    with open(my_file_path, 'r') as f:
        total_lines = sum(1 for _ in f)
    while True:
        try:
            num = int(input("Enter number: "))
            if num < 0 or num > total_lines:
                raise ValueError
            return num
        except ValueError:
            print(f"number of rows must be between 0 and {total_lines}.")
            continue

def process_last_lines_service(my_file_path):
    """Handle last lines service - return specified number of last lines."""
    num_rows = get_number_of_rows_input(my_file_path)
    with open(my_file_path, 'r') as f:
        lines = f.readlines()
    return "".join(lines[-num_rows:]) if num_rows > 0 else ""

def get_file_input():
    """Get file path from user input."""
    return input("Enter a file path: ")

def menu_options(my_file_path, chosen_service) :
    """Execute the menu option corresponding to the chosen service."""
    print(separate('-'))
    if chosen_service == 'sort':
        print(process_sort_service(my_file_path))
    elif chosen_service == 'rev':
        print(process_reverse_service(my_file_path))
    elif chosen_service == 'last':
        print(process_last_lines_service(my_file_path))
    else:
        print("\033[35mok. goodbye.\033[0m")
        return False
    print(separate('-'))
    if chosen_service != '0':
        print("now you're welcome to try a different option-\n")
    return True

def run_menu():
    """Run the main menu loop until the user chooses to exit."""
    my_file_path = get_file_input()
    print("You are welcomed to choose from the menu below-\n")
    while True:
        try:
            choice = menu_input()
        except ValueError as e:
            print(e)
            continue
        if not menu_options(my_file_path, choice):
            break

def main():
    run_menu()

if __name__ == '__main__':
    main()