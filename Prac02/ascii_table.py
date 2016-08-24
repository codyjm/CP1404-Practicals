LOWER = 33
UPPER = 127

character = input("Enter a character: ")
print("The ASCII code for {} is {}".format(character, ord(character)))

number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while number <= LOWER or number >= UPPER:
    print("Invalid number")
    number = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))

print("The ASCII code for {} is {}".format(number, chr(number)))

for i in range(LOWER, UPPER):
    print("{:<5} {}".format(i, chr(i)))