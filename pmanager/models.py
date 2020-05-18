import peewee

database = peewee.SqliteDatabase("homework.db")

class Credentials(peewee.Model):
    title = peewee.CharField()
    description = peewee.CharField()
    url = peewee.CharField()
    username = peewee.CharField()
    passphrase = peewee.CharField()
    unique_id = peewee.CharField()
    class Meta:
        database = database
        
if __name__=="__main__":
    try:
        Credentials.create_table()
        print("Table Created!!")
    except peewee.OperationalError:
        print("Credentials Table already exists!")