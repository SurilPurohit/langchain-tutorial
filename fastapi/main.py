from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('users.json', 'r') as f:
        data = json.load(f)

    return data
        

@app.get("/")
def hello():
    return {'message':'User Management System API'}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your user records'}

@app.get('/view')
def view():
    data = load_data()

    return data

@app.get('/user/{user_id}')
def view_patient(user_id: str = Path(..., description='ID of the user in the DB', example='P001')):
    # load all the patients
    data = load_data()

    if user_id in data:
        return data[user_id]
    raise HTTPException(status_code=404, detail='User not found')

@app.get('/sort')
def sort_users(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data