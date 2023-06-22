from os import getenv

from certifi import where
from dotenv import load_dotenv
# from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    load_dotenv()
    client = MongoClient(f'''mongodb+srv://rabidgeek:{getenv('PASSWORD')}@cluster0.swfbssk.mongodb.net/{getenv('DBNAME')}?retryWrites=true&w=majority''')
    database = client['bandersnatch']
    collection = database['bandersnatch']

    def seed(self, amount):
        docs = [{'field1': 'value1', 'field2': 'value2'} for _ in range(
            amount)]
        self.collection.insert_many(docs)

    def reset(self):
        # Drop the database tables
        self.collection.delete_many({})

    def count(self) -> int:
        doc_count = self.collection.count_documents({})
        print(f"Number of documents in the collection: {doc_count}")

    def dataframe(self) -> DataFrame:
        documents = list(self.collection.find())
        df = DataFrame(documents)
        print(df)

    def html_table(self) -> str:
        pass
