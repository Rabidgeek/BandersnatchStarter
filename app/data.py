from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    '''
    Database class that connects and manages a MongoDB database and collection.

    Using load_dotenv() to access the URL with Username and Password in an .env
    file for security and privacy of account information.

    Parameters:

    :database: variable calling on pymongo package to access environment
    variables in the .env file.
    '''
    load_dotenv()
    database = MongoClient(getenv("MONGO_DB"), tlsCAFile=where())["Database"]

    def __init__(self, collection):
        '''
        Initializes the database object with desired collection name.

        Parameters:

        :collection (string): The name of the collection in the database
        '''
        self.collection = self.database[collection]

    def seed(self, amount: int):
        '''
        Inserts any number of monsters in the collection using list
        comprehension and the to_dict() method in the range of amount
        (int), using the insert_many() method.

        Parameters:

        :amount (integer): The number of monsters to insert in the
        collection.

        '''
        self.collection.insert_many(
            [Monster().to_dict() for _ in range(amount)])

    def reset(self):
        '''
        Resets the database to 0

        Parameters:

        :collection: Using delete_many() method removes all documents in the
        collection.
        '''
        self.collection.delete_many({})

    def count(self) -> int:
        '''
        Counts the number of documents in collection using the count_document()
        method. Using an empty query ({}) in the method to count any and all
        monsters in said collection.

        Parameters:

        :returns an integer: The sum of all monsters in the collection.
        '''
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        '''
        Using the find() method to retrieve all monsters and its attributes,
        gathered in a list and then transformed into a pandas DataFrame.

        Parameters:

        :returns a DataFrame: A DataFrame containing all of the monsters and
        attributes of each monsters.
        '''
        return DataFrame(self.collection.find({}, {"_id": 0}))

    def html_table(self) -> str:
        '''
        Using the to_html() method to transform the pandas DataFrame into a
        HTML table string using the dataframe() method, otherwise return
        None if no DataFrame exists, to be used in a web app.

        Parameters:

        :returns a string: A HTML Table in string format to visualize the
        DataFrame in a web app, showing each monsters and its attributes.
        '''
        return self.dataframe().to_html() if self.count() else None


if __name__ == '__main__':
    db = Database("Database")
    db.reset()
    db.seed(2048)
    print(db.count())
