def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title)
    for index, option in enumerate(list_options):
        print(f"({index}) {option}")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    pass


def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    print("=======================")
    for item in table:
        for sub_item in item:
            print(sub_item)
        print("-----------------------")


def get_input(label):
    return input(label)
 

def get_inputs(fields):
    result = []
    for field in fields:
        result.append(get_input(f"{field}: "))
    return result
 

def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)
