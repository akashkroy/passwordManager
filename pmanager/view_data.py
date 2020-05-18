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
            t.add_row([res.name,res.description,res.username,res.passphrase,res.url])
        print(t)
        
    else:
        try:
            query = search_query.lower()
            results = Credentials.select().where(Credentials.name==query)
            for result in results:
                t.add_row([result.name,result.description,result.username,result.passphrase,result.url])
            print(t)
        except:
            print("No result found for {}.".format(search_query))
    
    
        