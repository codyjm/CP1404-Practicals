"""
Intermediate 1
"""
COUNT = 5

def main():
    numbers = []

    for number in range(COUNT):
        number = int(input("Number: "))
        numbers.append(number)

    print_list_functions(numbers)


def print_list_functions(numbers):
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))


main()
