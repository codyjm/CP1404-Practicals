"""
Programming Language Comparison
"""
from Prac07.programminglanguage import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    languages = [ruby, python, vb]
    print("\nThe dynamically typed languages are:")
    for lang in languages:
        if lang.is_dynamic():
            print("{}".format(lang.name))

main()
