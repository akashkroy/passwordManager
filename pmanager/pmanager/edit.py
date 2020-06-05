import peewee
from pmanager.models import Credentials
from prettytable import PrettyTable
from .helpers import create_table
from . import constants

def create_db_field(row, field):
    if field not in [x.lower() for x in constants]:
        print("* Incorrect Value: Program Aborted!")
        return

    edit_value = input("* Enter the value : ")

    table_row = [row.title, row.description, row.username, row.passphrase, row.url]
    for index, _field in enumerate(constants.FIELDS):
        if _field.lower() == field:
            table_row[index] = edit_value

    create_table([table_row], output=True)
    proceed = input("* Do you want to save changes (y/n)? ")

    if proceed.lower() != 'y':
        print("* Changes not saved. Program aborted!")
    
    unique_id = "{}@{}".format(row.username,row.url)
    query = Credentials.update({field:edit_value}).where(Credentials.unique_id==unique_id)
    query.execute()
    print("* Changes saved.")
        

def edit_data(url):
    results = Credentials.select().where(Credentials.url==url)

    if results.count()<0:
        print("* URL not found! \n* Try Again :)")
        return

    rows = list()
    for result in results:
        rows.append([result.title,result.description,result.username,result.passphrase,result.url])
    create_table(rows, output=True)
    
    username = input("\n* Enter Username of the row you want to edit: ")
    unique_id = "{}@{}".format(username,url)
    try:
        row = Credentials.select().where(Credentials.unique_id==unique_id).get()

        table_row = [row.title, row.description, row.username, row.passphrase, row.url]

        create_table([table_row], output=True)

        print("* Enter the name of field you want to change: {fields}".format(fields=", ".join(constants.FIELDS)))
        edit_field = input()
        create_db_field(row, edit_field.lower())
    
    except Exception as e:
        print("* Incorrect username : Username not found!", str(e))
