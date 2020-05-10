import peewee

from models import Credentials

name = input("Title: ")
description = input("Description: ")
url = input("URL of the website: ")
username = input("Username: ")
password = input("Password: ")

data = Credentials.insert({Credentials.name: name,
                           Credentials.description: description,
                           Credentials.url: url,
                           Credentials.username: username,
                           Credentials.passphrase: password}).execute()
