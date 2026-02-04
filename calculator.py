"""This script simulating the fonctionnement of a calculator with some basics
operations like addition, subtraction, multiplication and division."""

from operations import operation


print("Give me two numbers, and I'll applicate operations on them")
print("Enter 'q' at anytime to quit.")

history = []
while True:
    number_one = input("\nGive me a number: ")

    #Test if the user wants to quit
    if number_one.lower().strip() == 'q':
        exit()

    #Test if the input is valid
    try:
        number_one = float(number_one)
    except ValueError:
        print("\nPlease, enter a valid number.")
        continue

    #Give the possibility to the user to enter a valid number
    while True:
        number_two = input("Give me a number: ")

        #Test if the user wants to quit
        if number_two.lower().strip() == 'q':
            exit()
        
        #Test if the input is valid
        try:
            number_two = float(number_two)
            break
        except ValueError:
            print("\nPlease, enter a valid number.")
    
    #Check and give at the user to enter a valid operator
    while True:
        operator = input("Enter an operator (+, -, *, /) to use: ")

        #Test if the user wants to quit
        if operator.lower().strip() == 'q':
            exit()

        #Test if the operation select by the user is valid
        operators = ["+", "-", "*", "/"]
        if operator not in operators:
            print("Sorry, this operation is not valid...")
        else:
            break
    
    #Operation
    try:
        calculation = operation(number_one, number_two, operator)
        print(f"\n{number_one:.2f} {operator} {number_two:.2f} = {calculation:.2f}")
        history.append(f"{number_one:.2f} {operator} {number_two:.2f} = {calculation:.2f}")
    except ZeroDivisionError:
        print("Oops! Division by 0 is not valid...")
    
    #Test if the user wants to make another calculation
    more_calculation = input("\nDo you want make another operation? (y/n) \n")
    if more_calculation.lower().strip() != 'y' and more_calculation.lower().strip() != 'yes':
        break

#History display
if history:
    history_list = input("Do you want your history calculation? (y/n) ")
    if history_list.lower().strip() in ["y", "yes"]:
        for calculation in history:
            print(calculation)



    

        



