import peewee
import sys 
from prettytable import PrettyTable
from pmanager.models import Credentials

t = PrettyTable()

def view(search_query):
    ### this will make the output look pretty and organised
    t = PrettyTable()
    t.field_names = ['Title','Description','Username','Password','URL']

    if search_query=='all':
        result = Credentials.select()
        for res in result:
            t.add_row([res.title,res.description,res.username,res.passphrase,res.url])
        print(t)
        
    else:
        query = search_query.lower()
        results = Credentials.select().where(Credentials.title==query)
        if results.count()>0:
            print("Number of queries found : {}\n".format(results.count()))
            for result in results:
                t.add_row([result.title,result.description,result.username,result.passphrase,result.url])
            print(t)
        else:
            print("No result found for {} \nTry Again :)".format(search_query))