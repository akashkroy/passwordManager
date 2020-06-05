from prettytable import PrettyTable
from . import constants

def create_table(rows, output=False):
    t = PrettyTable()
    t.field_names = constants.FIELDS
    for row in rows:
        t.add_row(row)
    if output:
        print(t)
    return t