from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    load_dotenv()
    database = MongoClient(getenv("MONGO_DB"), tlsCAFile=where())["Database"]

    def __init__(self, collection):
        # Creates the collection in database
        self.collection = self.database[collection]

    def seed(self, amount: int):
        # Seeds the database with monsters
        self.collection.insert_many([Monster().to_dict() for _ in range(amount)])

    def reset(self):
        # Drop the database tables
        self.collection.delete_many({})

    def count(self) -> int:
        # Return a count of how many monsters are in the database
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        # Return a Dataframe of all monsters in this collection
        return DataFrame(self.collection.find({}, {"_id": 0}))

    def html_table(self) -> str:
        # returns a HTML table version of the Dataframe,
        # or None if collection is empty
        return self.dataframe().to_html() if self.count() else None


if __name__ == '__main__':
    db = Database("Database")
    db.reset()
    db.seed(2048)
    print(db.count())
