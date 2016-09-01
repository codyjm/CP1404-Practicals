"""
Do from scratch exercise
Count words in string
"""

word_count = {}

text_input = input("Enter string: ").lower().split()
for word in text_input:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word in sorted(word_count):
    print("{} : {}".format(word, word_count[word]))

