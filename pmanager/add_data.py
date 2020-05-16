import peewee

from pmanager.models import Credentials

def add():
    name = input("Title: ")
    description = input("Description: ")
    url = input("URL of the website: ")
    username = input("Username: ")
    password = input("Password: ")
    #unique_id = username + url

    data = Credentials.insert({Credentials.name: name,
                            Credentials.description: description,
                            Credentials.url: url,
                            Credentials.username: username,
                            Credentials.passphrase: password}).execute()
    
    print("Added")
    
if __name__=="__main__":
    add()