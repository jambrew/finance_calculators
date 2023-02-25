# A program that contains two financial calculators:
# an investment calculator and a home loan repayment calculator.

import math
# import only system from os
from os import system, name
# import colours for text, researched from
# https://www.geeksforgeeks.org/print-colors-python-terminal/
from colorama import Fore, Style

# Creates the 'investment' calculator as a function.
# Clears the screen, takes and stores the inputs as variables, validating the
# entries and then calculates and prints the result

# Script to clear screen taken from
# https://www.geeksforgeeks.org/clear-screen-python/
# define our clear function


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Investment Calculator function


def investment_calc():
    clear()
    # Gets the investment value; interest rate %; number of years to invest,
    # whether simple or compound interest and validates each entry using a loop
    while True:
        try:
            deposit = round(
                float(input("Enter the amount being invested: £")), 2)

        except ValueError:
            print("Sorry, that was not a valid entry. \
                Please enter an amount, and without any commas.")
            continue

        else:
            break

    while True:
        try:
            interest_rate_percentage = round(
                float(input("Enter the rate of interest (%): ")), 2)

        except ValueError:
            print(
                "Sorry, that was not a valid entry. Please enter a number, \
                    without the % sign.")
            continue

        else:
            break

    while True:
        try:
            years_invested = int(
                input("Enter the number of years the money is to be invested \
                    for: "))

        except ValueError:
            print("Sorry, that was not a valid entry. Please enter a whole \
                number.")
            continue

        else:
            break

    while True:
        interest = input(
            "Enter either 'simple' or 'compound' to calculate the correct rate \of interest: ")

        # Calculates simple interest
        if interest.lower() == "simple" or interest.lower() == "s":
            total_return = round(deposit * (interest_rate_percentage / 100)
                                 * years_invested + deposit, 2)
            interest = "simple"
            break

        # Calculates compound interest
        elif interest.lower() == "compound" or interest.lower() == "c":
            total_return = round(
                deposit * math.pow((1 + (interest_rate_percentage / 100)), years_invested), 2)
            interest = "compound"
            break

        else:
            continue

    # Print results
    clear()
    print(f'''If you invest £{deposit:,.2f} over {years_invested} years, with a {interest} rate of {interest_rate_percentage}% interest...
            The total amount you will receive back will be: £{total_return:,.2f}''')


# Bond Calculator function
def bond_calc():
    clear()

    # Gets present value of the house; the interest rate; and the term of loan in months - validating each entry
    while True:
        try:
            house_value = int(input("Enter the present value of the house: £"))

        except ValueError:
            print(
                "Sorry, that was not a valid entry. Please enter a whole number, and without any commas.")
            continue

        else:
            break

    while True:
        try:
            interest_rate_percentage = round(
                float(input("Enter the rate of interest (%): ")), 2)

        except ValueError:
            print(
                "Sorry, that was not a valid entry. Please enter a number, without the % sign.")
            continue

        else:
            break

    while True:
        try:
            term_in_months = int(
                input("Enter the number of months you plan to take to repay the bond: "))

        except ValueError:
            print("Sorry, that was not a valid entry. Please enter a whole number (please do not enter decimals or part months).")
            continue

        else:
            break

    # Calculate the monthly repayment
    monthly_interest = ((interest_rate_percentage / 100) / 12)
    monthly_repayment = (monthly_interest * house_value) / \
        (1 - (1 + monthly_interest) ** (-term_in_months))

    # Print results
    clear()
    print(f'''Based on taking a bond to cover a present house value of {house_value:,.2f} at an interest rate of {interest_rate_percentage}%, over a term of {term_in_months // 12} years {term_in_months % 12} months...
    Your monthly repayment would be: £{monthly_repayment:,.2f}''')


# Main Menu
invalid_entry = False    # If True, invalid entry message prints below

while True:
    clear()
    print('''
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
    ''')
    if invalid_entry == True:
        # Only prints if previously invalid entry
        print(Fore.RED + "Invalid entry, please try again" + Style.RESET_ALL)

    # Asks user for choice of program
    chosen_app = input(
        "Enter either 'investment' or 'bond' from the menu above to proceed: ")

    # If investment, runs the investment calculator function
    if chosen_app.lower() == "investment" or chosen_app.lower() == "i":
        investment_calc()
        break

    # If bond, runs the bond calculator function
    elif chosen_app.lower() == "bond" or chosen_app.lower() == "b":
        bond_calc()
        break

    else:
        invalid_entry = True
        continue
# End
