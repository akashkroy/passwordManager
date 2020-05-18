import peewee

from pmanager.models import Credentials

def add():
    name = input("Title: ").lower()
    description = input("Description: ")
    url = input("URL of the website: http://")
    username = input("Username: ")
    password = input("Password: ")
    unique_id = "{}@{}".format(username,url)

    Credentials.insert({Credentials.name: name,
                            Credentials.description: description,
                            Credentials.url: url,
                            Credentials.username: username,
                            Credentials.passphrase: password,
                            Credentials.unique_id: unique_id}).execute()
    
    print("Added")
    
