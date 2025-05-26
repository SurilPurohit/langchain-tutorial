from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

class User(BaseModel):

    id: Annotated[str, Field(..., description='ID of the user', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the user')]
    city: Annotated[str, Field(..., description='City where the user is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the user')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the user')]
    height: Annotated[float, Field(..., gt=0, description='Height of the user in meter')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the user in kg')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'

class userUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]

def load_data():
    with open('users.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('users.json', 'w') as f:
        json.dump(data, f)

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
def view_user(user_id: str = Path(..., description='ID of the user in the DB', example='P001')):
    # load all the users
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

@app.post('/create')
def create_user(user: User):

    # load existing data
    data = load_data()

    # check if the user already exists
    if user.id in data:
        raise HTTPException(status_code=400, detail='user already exists')

    # new user add to the database
    data[user.id] = user.model_dump(exclude=['id'])

    # save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message':'user created successfully'})

@app.put('/edit/{user_id}')
def update_user(user_id: str, user_update: userUpdate):

    data = load_data()

    if user_id not in data:
        raise HTTPException(status_code=404, detail='user not found')
    
    existing_user_info = data[user_id]

    updated_user_info = user_update.model_dump(exclude_unset=True)

    for key, value in updated_user_info.items():
        existing_user_info[key] = value

    #existing_user_info -> pydantic object -> updated bmi + verdict
    existing_user_info['id'] = user_id
    user_pydandic_obj = User(**existing_user_info)
    #-> pydantic object -> dict
    existing_user_info = user_pydandic_obj.model_dump(exclude='id')

    # add this dict to data
    data[user_id] = existing_user_info

    # save data
    save_data(data)

    return JSONResponse(status_code=200, content={'message':'user updated'})


@app.delete('/delete/{user_id}')
def delete_user(user_id: str):

    # load data
    data = load_data()

    if user_id not in data:
        raise HTTPException(status_code=404, detail='user not found')
    
    del data[user_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'user deleted'})