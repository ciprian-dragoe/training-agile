from view import terminal as view

def display_menu():
    options = ["Back to main menu",
               "Add employee",
               "List all employees",
               "Update employee by CNP",
               "List all employees with similar name",
               "Delete employee",
               "Get employees with birthdays this weeks"]
    view.print_menu("HR", options)
