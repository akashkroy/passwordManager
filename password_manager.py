#! /usr/bin/python3

import sys
import argparse
from pmanager import view_data, add_data, generate_password, delete, edit

def parser():
    parser = argparse.ArgumentParser(description="A simple password manager")
    parser.add_argument("--add", nargs="+", type=str, help="Add data directly to the Manager")
    parser.add_argument("--view", type=str, help="View all entries in the Manager")
    parser.add_argument("--edit", type=str, help="Edit an enrty")
    parser.add_argument("--gen", type=int, help="Generate a password of length N (N is a integer)")
    parser.add_argument("--perform", choices=["add", "delete"], help="Add or Delete rows")
    return parser.parse_args()

"""def usage():
    print('''USAGE: password_manager [options]
          gen n     Generate a password of length n
          view      View all the entries in the manager
          add       Add Data to the Manager 
          del       Remove entry from the Manager
          help      View Usage
          ''')"""

user_input = parser()
if user_input.gen:
    print("Password of length: {length}".format(length=user_input.gen))
    generate_password.gen_pass(user_input.gen)
    
if user_input.view:
    view_data.view(user_input.view)
# print(parser())

if user_input.edit:
    edit.edit_data(user_input.edit)

if user_input.perform=='add':
    print("Add data to the Password Manager")
    add_data.add()
    
if user_input.perform=='delete':
    delete.del_row()
    
if user_input.add:
    title = user_input.add[0]
    description = user_input.add[1]
    username = user_input.add[2]
    password = user_input.add[3]
    url = user_input.add[4]
    add_data.add_to_db(title,description,username,password,url)