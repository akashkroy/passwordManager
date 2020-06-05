import peewee
import sys 
from . import constants
from .helpers import create_table
from pmanager.models import Credentials

def view(search_query):
    rows = list()
    if search_query=='all':
        results = Credentials.select()
        #rows = list()
        for result in results:
            rows.append([result.title,result.description,result.username,result.passphrase,result.url])
        print(type(results))
        create_table(rows, output=True)
        
    else:
        query = search_query.lower()
        results = Credentials.select().where(Credentials.title==query)
        if results.count()== 0:
            print("No result found for {} \nTry Again :)".format(search_query))
            return

        for result in results:
            rows.append([result.title,result.description,result.username,result.passphrase,result.url])
        print("Number of queries found : {}\n".format(results.count()))
        create_table(rows,output=True)
