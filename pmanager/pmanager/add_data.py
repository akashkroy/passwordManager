import peewee

from pmanager.models import Credentials

def add():
    title = input("Title: ").lower()
    description = input("Description: ")
    url = input("URL of the website: http://")
    username = input("Username: ")
    password = input("Password: ")
    unique_id = "{}@{}".format(username,url)

    Credentials.insert({Credentials.title: title,
                            Credentials.description: description,
                            Credentials.url: url,
                            Credentials.username: username,
                            Credentials.passphrase: password,
                            Credentials.unique_id: unique_id}).execute()
    
    print("Added")
    
def add_to_db(title, description, username, password, url):
    unique_id = "{}@{}".format(username,url)

    Credentials.insert({Credentials.title: title,
                            Credentials.description: description,
                            Credentials.url: url,
                            Credentials.username: username,
                            Credentials.passphrase: password,
                            Credentials.unique_id: unique_id}).execute()
    
    print("Added")
    
