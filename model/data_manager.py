# Do not modify this file!


def read_table_from_file(file_name, separator=';'):
    """Read CSV file into a data table.

    Args:
        file_name: The name of the CSV data file.
        separator: The CSV separator character

    Returns:
        The data parsed into a list of lists.
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
        return [element.replace("\n", "").split(separator) for element in lines]
    except IOError:
        return []


def write_items_to_file(file_name, items, separator=';'):
    """Write tabular data into a CSV file.

    Args:
        file_name: The name of the file to write to.ff
        items: list of lists containing tabular data.dff
        separator: The CSV separator character
    """
    with open(file_name, "a+") as file:
        to_write = separator.join(items) + "\n"
        file.write(to_write)
