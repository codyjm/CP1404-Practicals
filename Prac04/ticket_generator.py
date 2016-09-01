"""
Do from scratch - 1
Lottery Ticket Generator
"""
import random

MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    quick_picks = int(input("How many quick picks? "))
    for pick in range(quick_picks):
        ticket_numbers = get_random_numbers()
        print(ticket_numbers)


def get_random_numbers():
    numbers = []

    for number in range(6):
        rand_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while rand_number in numbers:
            rand_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        numbers.append(rand_number)

    numbers.sort()
    return numbers


main()
