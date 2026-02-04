"""This script simulating the fonctionnement of a calculator with some basics
operations like addition, subtraction, multiplication and division."""

from operations import addition, subtraction, multiplication, division





#Test if the user inputs are valid numbers
try:
    number_one = float(input("Please, enter a number: "))
except ValueError:
    print("Sorry, that's not a valid number...")

try:
    number_two = float(input("Please, enter now a second number: "))
except ValueError:
    print("Sorry, that's not a valid number...")

#Operation wished
operation = input("\nWhich operation (+, -, *, /) would you like make with this number? ")

#Test if the operation select by the user is valid
authorized_operations = ["+", "-", "*", "/"]
if operation not in authorized_operations:
    print("Sorry, this operation is not valid...")

#Operations
if operation == "+":
    add = addition(number_one, number_two)
    print(f"{number_one:.2f} + {number_two:.2f} = {add:.2f}")

if operation == "-":
    sub = subtraction(number_one, number_two)
    print(f"{number_one:.2f} - {number_two:.2f} = {sub:.2f}")

if operation == "*":
    mul = multiplication(number_one, number_two)
    print(f"{number_one:.2f} * {number_two:.2f} = {mul:.2f}")

try:
    if operation == "/":
        div = division(number_one, number_two)
        print(f"{number_one:.2f} / {number_two:.2f} = {div:.2f}")
except ZeroDivisionError:
    print("Oops! Division by 0 is not valid...")



