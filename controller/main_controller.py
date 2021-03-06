from view import terminal as view
from controller import sales_controller


def load_module(option):
    if option == 1:
        sales_controller.menu()
    elif option == 0:
        return 0
    else:
        raise KeyError()


def display_menu():
    options = ["Exit program",
               "Sales"]
    view.print_menu("Main menu", options)


def menu():
    option = None
    while option != '0':
        display_menu()
        try:
            option = view.get_input("Select module: ")
            load_module(int(option))
        except KeyError:
            view.print_error_message("There is no such option!")
        except ValueError:
            view.print_error_message("Please enter a number!")
    view.print_message("Good-bye!")
