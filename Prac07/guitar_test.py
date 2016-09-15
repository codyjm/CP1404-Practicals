"""
Test guitar class
"""
from Prac07.guitar import Guitar


def main():
    guitar_one = Guitar("Gibson L-5 Ces", 1922, 10000)
    guitar_two = Guitar("Second Guitar", 2011, 50)

    print("{}\n{}".format(guitar_one, guitar_two))

    print("get_age() - Expected 94. Got {}".format(guitar_one.get_age()))
    print("get_age() - Expected 5. Got {}".format(guitar_two.get_age()))

    print("is_vintage() - Expected True. Got {}".format(guitar_one.is_vintage()))
    print("is_vintage() - Expected False. Got {}".format(guitar_two.is_vintage()))

main()
