import settings
import uvicorn

from fastapi import FastAPI
from models import Item
from typing import Dict
from pymongo import MongoClient


DB_USERNAME = settings.DB_PARAMS['db_username']
DB_PASSWORD = settings.DB_PARAMS['db_password']
DB_NAME = settings.DB_PARAMS['db_name']


app = FastAPI()
client = MongoClient(f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@cluster0.pgwbz.mongodb.net/{DB_NAME}?retryWrites=true&w=majority")
db = client.test_db


@app.get('/items')
async def get_items(filter: Dict):
    if 'item_id' in filter:
        if int(filter['item_id']) > db.items.estimated_document_count():
            return {'error': 'Id is greater than collection length'}
    
        result = db.items.find_one({'item_id': filter['item_id']})
        item = Item(**result)

        return {'item': item}


    items = []
    for item in db.items.find(filter):
        items.append(Item(**item).name)
    
    return {'items': items}


@app.post('/items',)
async def create_item(item: Item):
    if hasattr(item, 'id'):
        delattr(item, 'id')

    item.item_id = db.items.estimated_document_count() + 1
    ret = db.items.insert_one(item.dict(by_alias=True))
    item.id = ret.inserted_id
    return {
        'message': 'Item created',
        'item': item
    }


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8080)
