"""
Intermediate 2
"""


def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
    'swei45','BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
    'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username_input = input("Enter username: ")
    if username_input in usernames:
        print("Access granted")
    else:
        print("Access denied")

main()
