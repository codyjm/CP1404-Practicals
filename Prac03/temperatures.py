"""
CP1404/CP5632 - Practical
Temperature conversion
"""
__author__ = 'Cody Moxham'

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_input = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius_input)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit_input = float(input("Fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit_input)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def convert_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

main()
