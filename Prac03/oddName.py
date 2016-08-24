"""
Cody Moxham
print every second letter of name
"""


def main():
    name = get_name()
    letter_frequency = int(input("Enter frequency of letters: "))
    print_character(name, letter_frequency)


def print_character(name, frequency):
    for i in range(frequency - 1, len(name), frequency):
        print(name[i])


def get_name():
    name = input("Enter name: ")
    while len(name) == 0:
        name = input("Enter a name: ")
    return name


main()
