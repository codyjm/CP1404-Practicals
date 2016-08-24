LOWER = 33
UPPER = 127
'''
character = input("Enter a character: ")
print("The ASCII code for {} is {}".format(character, ord(character)))

number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while number <= LOWER or number >= UPPER:
    print("Invalid number")
    number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))

print("The ASCII code for {} is {}".format(number, chr(number)))

for i in range(LOWER, UPPER):
    print("{:<5} {}".format(i, chr(i)))
'''


def get_number(lower, upper):
    valid_number = False
    while not valid_number:
        try:
            number = int(input("Enter a number between {} and {}: ".format(lower, upper)))
            if number <= lower or number >= upper:
                print("Invalid number ({} - {})".format(lower, upper))
            else:
                valid_number = True
        except ValueError:
            print("Invalid. Please enter a number.")
    return number


def main():
    number = get_number(LOWER, UPPER)
    print("The ASCII code for {} is {}".format(number, chr(number)))


main()
