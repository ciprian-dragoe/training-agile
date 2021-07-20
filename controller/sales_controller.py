from model.sales import sales
from model import data_manager
from view import terminal as view


def list_transactions():
    transactions = data_manager.read_table_from_file(sales.DATAFILE)
    view.print_table(transactions)


def add_transaction():
    fields = view.get_inputs(sales.HEADERS)
    data_manager.write_items_to_file(sales.DATAFILE, fields)


def update_transaction():
    transactions = data_manager.read_table_from_file(sales.DATAFILE)
    view.print_table(transactions)
    
    return True


def delete_transaction():
    to_delete_name = view.get_input("Enter the name of the person you wish to delete")
    transactions = data_manager.read_table_from_file(sales.DATAFILE)
    to_write = []
    for transaction in transactions:
        if transaction['Customer'] != to_delete_name:
            to_write.append(transaction)
    data_manager.write_items_to_file(sales.HEADERS, to_write)


def list_employes():
    employees = []
    print(employees)
    print("there are no emplyees now, this is a ghost company")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        list_employes()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "List emplyes"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation:  ")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
