#! /usr/bin/python3

import sys
import argparse

def parser():
    parser = argparse.ArgumentParser(description="A simple password manager")
    parser.add_argument("--add", help="Add data to the Manager")
    parser.add_argument("--view", help="View all entries in the Manager")
    parser.add_argument("--perform", choices=["add", "remove", "delete"], help="An example of limits")
    return parser.parse_args()

def usage():
    print('''USAGE: password_manager [options]
          gen n     Generate a password of length n
          view      View all the entries in the manager
          add       Add Data to the Manager 
          del       Remove entry from the Manager
          help      View Usage
          ''')
    
# try:
#     if sys.argv[1] == 'help':
#         usage()
#     else:
#       print("Invalid Argument \n")
#       usage()
# except IndexError:
#     print("Invalid Argument \n")
#     usage()

user_input = parser()
if user_input.add:
    print("User tried to add: {add}".format(add=user_input.add))
# print(parser())