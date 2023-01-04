import sql_commands
import time

import os


def clr_screen():
    # Check if Operating System is Mac and Linux or Windows
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')


db = sql_commands.DataBase('Sale_DB.db')


def print_res(items):
    for item in items:
        print(item)
    input("\nPress Enter to continue...")


def view_categories():
    cats = db.view_categories()
    print_res(cats)


def view_brands():
    brands = db.view_brands()
    print_res(brands)


def view_customers():
    customers = db.view_customers()
    print_res(customers)


def view_sellers():
    sellers = db.view_sellers()
    print_res(sellers)


def view_wares():
    wares = db.view_all_wares()
    print_res(wares)


main_menu = "Please Select a Number:\n" \
            " 1: View Customers\n" \
            " 2: View Sellers\n" \
            " 3: View Brand\n" \
            " 4: View Categories\n" \
            " 5: View Wares\n" \
            " 0: Exit \n" \
            "Your choice -->: "
mainloop = True
while mainloop:
    clr_screen()
    res = input(main_menu)

    try:
        res = int(res)
    except ValueError:
        print("OOPS-->")
        time.sleep(0.5)
        print("Please Enter A Number")
        time.sleep(1.2)
    else:
        match res:
            case 0:
                mainloop = False
            case 1:
                view_customers()
            case 2:
                view_sellers()
            case 3:
                view_brands()
            case 4:
                view_categories()
            case 5:
                view_wares()
            case _:
                print("Please Choose From Menu ")
                time.sleep(1)
