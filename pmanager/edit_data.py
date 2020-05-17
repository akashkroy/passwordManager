import peewee
import sys 
from prettytable import PrettyTable
from pmanager.models import Credentials

#print("Submit a Title query: ")
#print("Enter 'all' to view all entries")
#search_query = 'all'
def view_data(search_query):
    ### this will make the output look pretty and organised
    t = PrettyTable()
    t.field_names = ['Title','Description','Username','Password','URL']

    if search_query=='all':
        result = Credentials.select()
        for res in result:
            t.add_row([res.name,res.description,res.username,res.passphrase,res.url])
        print(t)
        #print(result)
    else:
        try:
            query = search_query.lower()
            result = Credentials.select().where(Credentials.name==query).get()
            t.add_row([result.name,result.description,result.username,result.passphrase,result.url])
            print(t)
        except:
            print("No result found for {}.".format(search_query))
    
    