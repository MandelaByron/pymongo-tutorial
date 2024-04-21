from pymongo import MongoClient
import pandas as pd
import json
from config import uri

def get_db():
    client = MongoClient(uri)
    
    return client['player_data']

database = get_db()

collection = database['player_data_collection']

dataframe = pd.read_json('player_data.json')

records =  dataframe.to_json(orient='records')

documents = json.loads(records)

results = collection.insert_many(documents)

print(results)
