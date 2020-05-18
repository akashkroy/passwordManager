import peewee
from pmanager.models import Credentials
from prettytable import PrettyTable

def edit_data(url):
    t = PrettyTable()
    t.field_names = ['Title','Description','Username','Password','URL']

    results = Credentials.select().where(Credentials.url==url)
    if results.count()>0:
        for result in results:
            t.add_row([result.title,result.description,result.username,result.passphrase,result.url])
        print(t)
        
        username = input("\n* Enter Username of the row you want to edit: ")
        unique_id = "{}@{}".format(username,url)
        try:
            row = Credentials.select().where(Credentials.unique_id==unique_id).get()
            t = PrettyTable()
            t.field_names = ['Title','Description','Username','Password','URL']
            t.add_row([row.title,row.description,row.username,row.passphrase,row.url])
            print(t)
            print("* Enter the name of field you want to change: Title, Description, Username, Password, URL: ")
            edit_field = input()
            print("* Enter the value : ")
            edit_value = input()
            t = PrettyTable()
            t.field_names = ['Title','Description','Username','Password','URL']
            
            if "title"==edit_field.lower():
                print("* Enter the value : ")
                edit_value = input()
                t.add_row([edit_value,row.description,row.username,row.passphrase,row.url])
                print(t)
                proceed = input("* Do you want to save changes (y/n)?")
                if proceed.lower()=='y':
                    query = Credentials.update(title=edit_value).where(Credentials.unique_id==unique_id)
                    query.execute()
                    print(t)
                else:
                    print("* Changes not saved. Program aborted!")
                
                
            elif "description"==edit_field.lower():
                print("* Enter the value : ")
                edit_value = input()
                t.add_row([row.title,edit_value,row.username,row.passphrase,row.url])
                print(t)
                proceed = input("* Do you want to save changes (y/n)?")
                if proceed.lower()=='y':
                    query = Credentials.update(description=edit_value).where(Credentials.unique_id==unique_id)
                    query.execute()
                    print(t)
                else:
                    print("* Changes not saved. Program aborted!")
                
            elif "username"==edit_field.lower():
                print("* Enter the value : ")
                edit_value = input()
                t.add_row([row.title,row.description,edit_value,row.passphrase,row.url])
                print(t)
                proceed = input("* Do you want to save changes (y/n)?")
                if proceed.lower()=='y':
                    query = Credentials.update(username=edit_value).where(Credentials.unique_id==unique_id)
                    query.execute()
                    print(t)
                else:
                    print("* Changes not saved. Program aborted!")
                
            elif "password"==edit_field.lower():
                print("* Enter the value : ")
                edit_value = input()
                t.add_row([row.title,row.description,row.username,edit_value,row.url])
                print(t)
                proceed = input("* Do you want to save changes (y/n)?")
                if proceed.lower()=='y':
                    query = Credentials.update(passphrase=edit_value).where(Credentials.unique_id==unique_id)
                    query.execute()
                    print(t)
                else:
                    print("* Changes not saved. Program aborted!")
            
            elif "url"==edit_field.lower():
                print("* Enter the value : ")
                edit_value = input()
                t.add_row([row.title,row.description,row.username,row.passphrase,edit_value])
                print(t)
                proceed = input("* Do you want to save changes (y/n)?")
                if proceed.lower()=='y':
                    query = Credentials.update(url=edit_value).where(Credentials.unique_id==unique_id)
                    query.execute()
                    print(t)
                else:
                    print("* Changes not saved. Program aborted!")
            
            else:
                print("* Incorrect Value: Program Aborted!")
        except:
            print("* Incorrect username : Username not found!")
        
    else:
        print("* URL not found! \n* Try Again :)")
            