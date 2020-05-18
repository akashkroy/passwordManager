import peewee
from prettytable import PrettyTable
from pmanager.models import Credentials

def del_row():
    username = input("Enter username : ")
    url = input("Enter URL : http://")
    unique_id = username + "@" + url
    t = PrettyTable()
    t.field_names = ["Title","Description","Username","URL"]
    query = Credentials.select().where(Credentials.unique_id==unique_id).get()
    t.add_row([query.name, query.description,query.username,query.url])
    print(t)
    
    proceed = int(input("Enter 1 to proceed, any other key to abort"))
    if proceed:
        #del_query = Credentials.delete().where(Credentials.unique_id==unique_id)
        del_query = query.delete()
        del_query.execute()
        print("Selected Row Deleted")
        
    else:
        print("Program Aborted!")
      