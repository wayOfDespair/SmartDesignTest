from models import Item
from typing import List
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_create_item():
    item = {
        'name': 'test item',
        'description': 'item for test',
        'params': {
            'test': 'test'
        }
    }

    response = client.post('/items', json=item)
    assert response.status_code == 200
    assert response.json()['message'] == 'Item created'
    

def test_get_item_by_id():
    response = client.get('/items', json={'item_id': 1})
    print(response.json())
    assert response.status_code == 200
    assert response.json()['item']['item_id'] == 1 or response.json()['error'] == {'error': 'Id is greater than collection length'}


def test_get_items():
    response = client.get('/items', json={})
    print(response.json())
    assert response.status_code == 200
    assert response.json()['items'] is List or Item
