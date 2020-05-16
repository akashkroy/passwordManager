#! /usr/bin/python3

import sys
import argparse
from pmanager import edit_data, add_data, generate_password

def parser():
    parser = argparse.ArgumentParser(description="A simple password manager")
    parser.add_argument("--add", type=str, help="Add data to the Manager")
    parser.add_argument("--view", type=str, help="View all entries in the Manager")
    parser.add_argument("--gen", type=int, help="Generate a password of length N")
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
if user_input.gen:
    print("Password of length: {add}".format(add=user_input.gen))
    generate_password.gen_pass(user_input.gen)
    
if user_input.view:
    edit_data.view_data(user_input.view)
# print(parser())

if user_input.perform=='add':
    print("Add data to the Password Manager")
    add_data.add()