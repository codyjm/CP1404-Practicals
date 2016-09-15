"""
Store all user guitars in list, print guitar details
"""
from Prac07.guitar import Guitar

def main():
    print("My guitars!")

    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")
    display_guitars(guitars)


def display_guitars(guitars):
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>18} ({}), worth ${:10,.2f} {}"
              .format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))

main()
