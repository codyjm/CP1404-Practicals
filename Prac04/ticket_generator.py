"""
Do from scratch - 1
Lottery Ticket Generator
"""
import random

MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    ticket_numbers = get_random_numbers()
    quick_picks = input("How many quick picks? ")

    for line in quick_picks:


def get_random_numbers():
    numbers = []

    for number in range(6):
        numbers.append(random.randint(1, 45))
    numbers.sort()
    return numbers


main()