BudgetApp.py
#register
#-first name, last name, password, email
#-generate useraccount

#login
#-account number and password

#bank operation

#initialization process
# register
# - first name, last name, password, email
# - generate user account details
# login
# - account number & password
# bank operations
# Initializing the system
import random
import validation
import database
from getpass import getpass


# database = {
#     3297628881: ['rex', 'eddy', 'ma@ma', 'pass', 10000]
# }  # dictionary


def init():
    print("Welcome to bankPHP")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()
    elif have_account == 2:

        register()
    else:
        print("You have selected an invalid option")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)
    if is_valid_account_number:

        password = getpass('what is your password \n')

        user = database.authenticated_user(account_number_from_user, password)
        if user:
            bank_operation(user)

        print('Invalid account or password')
        login()
    else:
        print('invalid account number: check that you have up to 10 digits and valid integers')
        init()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass('create a password for yourself \n')

    account_number = generation_account_number()

    # database[account_number] = [first_name, last_name, email, password]

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:
        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()
    else:
        print('Something went wrong, Please try again')
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation()

    elif selected_option == 2:

        withdrawal_operation()

    elif selected_option == 3:

        logout()

    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")

        bank_operation(user)


def withdrawal_operation():
    print("withdrawal")


def deposit_operation():
    print("Deposit Operations")


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def logout():
    login()


init()
