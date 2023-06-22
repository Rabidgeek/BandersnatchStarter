from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    load_dotenv()
    client = MongoClient(getenv('MONGO_DB'), tlsCAFile=where())
    database = client['bandersnatch']

    def __init__(self, collection):
        self.collection = self.database["bandersnatch"]

    def seed(self, amount=1000):
        docs = [Monster().to_dict() for _ in range(amount)]
        self.collection.insert_many(docs)

    def reset(self):
        # Drop the database tables
        self.collection.delete_many({})

    def count(self) -> int:
        doc_count = self.collection.count_documents({})
        return doc_count

    def dataframe(self) -> DataFrame:
        documents = list(self.collection.find())
        df = DataFrame(documents)
        return df

    def html_table(self) -> str:
        df = self.dataframe()
        table = df.to_html(index=True)
        return table


if __name__ == '__main__':
    db = Database()
    db.seed(1000)
    print(db.count())
    print(list(db.collection.find({}, {"_id": 0})))
